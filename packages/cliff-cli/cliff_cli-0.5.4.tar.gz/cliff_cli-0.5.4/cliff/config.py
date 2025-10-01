from typing import Dict, Optional, List, Any
import os
import json

from pydantic import BaseModel, Field
from rich.table import Table
from rich import box
from l2m2.client import LLMClient

from cliff.console import cliff_print, console, resource_print


HOME_DIR = os.path.expanduser("~")
if os.getenv("CLIFF_ENV") == "development":  # pragma: no cover
    CONFIG_FILE = os.path.join(HOME_DIR, ".cliff", "config.dev.json")
else:
    CONFIG_FILE = os.path.join(HOME_DIR, ".cliff", "config.json")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
HELP_FILE = os.path.join(SCRIPT_DIR, "resources/config_help.txt")

HOSTED_PROVIDERS = {
    "groq",
    "cohere",
    "mistral",
    "replicate",
    "openai",
    "cerebras",
    "google",
    "anthropic",
}

DEFAULT_MODEL_MAPPING = {
    "groq": "llama-3.3-70b",
    "cohere": "command-a",
    "mistral": "codestral",
    "replicate": "llama-3-70b",
    "openai": "gpt-5",
    "cerebras": "llama-3.3-70b",
    "google": "gemini-2.5-flash",
    "anthropic": "claude-sonnet-4.5",
}


class Config(BaseModel):
    provider_credentials: Dict[str, str]
    default_model: Optional[str]
    preferred_providers: Dict[str, str]
    ollama_models: List[str]
    memory_window: int = Field(ge=0)
    timeout_seconds: int = Field(gt=0)


DEFAULT_CONFIG = Config(
    provider_credentials={},
    default_model=None,
    preferred_providers={},
    ollama_models=[],
    memory_window=10,
    timeout_seconds=20,
)


# -- Config Management -- #


def save_config(config: Config) -> None:
    with open(CONFIG_FILE, "w") as f:
        json.dump(config.model_dump(), f, indent=4)


def load_config() -> Config:
    if not os.path.exists(CONFIG_FILE):
        os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
        config = DEFAULT_CONFIG
    else:
        with open(CONFIG_FILE, "r") as f:
            try:
                loaded_json_data = json.load(f)
            except json.JSONDecodeError:
                loaded_json_data = {}

            data_to_merge = (
                loaded_json_data if isinstance(loaded_json_data, dict) else {}
            )

            default_data = DEFAULT_CONFIG.model_dump()
            merged_data: Dict[str, Any] = {**default_data, **data_to_merge}

            config = Config.model_validate(merged_data)

    save_config(config)
    return config


def apply_config(config: Config, llm: LLMClient) -> None:
    for provider in config.provider_credentials:
        llm.add_provider(provider, config.provider_credentials[provider])

    llm.set_preferred_providers(config.preferred_providers)

    for model in config.ollama_models:
        llm.add_local_model(model, "ollama")


# -- Validators -- #


def validate_provider(provider: str) -> bool:
    if provider not in HOSTED_PROVIDERS:
        cliff_print(f"Invalid provider: {provider}")
        return False
    return True


def validate_model(model: str, llm: LLMClient) -> bool:
    active_models = llm.get_active_models()
    if model not in active_models:
        cliff_print(f"Model {model} not found")
        return False
    return True


# -- Add/Update Functions -- #


def add_provider(provider: str, api_key: str) -> int:
    if not validate_provider(provider):
        return 1

    config = load_config()
    exists = provider in config.provider_credentials

    config.provider_credentials[provider] = api_key

    if config.default_model is None:
        config.default_model = DEFAULT_MODEL_MAPPING[provider]

    save_config(config)

    if exists:
        cliff_print(f"Updated provider {provider}")
        return 0
    else:
        cliff_print(f"Added provider {provider}")
        return 0


def add_ollama_model(model: str) -> int:
    config = load_config()
    config.ollama_models.append(model)
    if config.default_model is None:
        config.default_model = model
    save_config(config)
    cliff_print(f"Added local model {model}")
    return 0


def set_default_model(model: str, llm: LLMClient) -> int:
    if not validate_model(model, llm):
        return 1

    config = load_config()
    config.default_model = model
    save_config(config)

    cliff_print(f"Set default model to {model}")
    return 0


def prefer_add(model: str, provider: str, llm: LLMClient) -> int:
    if not validate_model(model, llm):
        return 1
    if not validate_provider(provider):
        return 1

    config = load_config()
    config.preferred_providers[model] = provider
    save_config(config)
    cliff_print(f"Added preferred provider {provider} for {model}")
    return 0


def update_memory_window(window: str) -> int:
    def handle_invalid():
        cliff_print("Memory window must be a non-negative integer")
        return 1

    try:
        int_value = int(window)
    except ValueError:
        return handle_invalid()
    if int_value < 0:
        return handle_invalid()

    config = load_config()
    config.memory_window = int_value
    save_config(config)
    cliff_print(f"Updated memory window size to {window}")
    return 0


def update_timeout(timeout: str) -> int:
    def handle_invalid():
        cliff_print("Timeout must be a positive integer")
        return 1

    try:
        int_value = int(timeout)
    except ValueError:
        return handle_invalid()
    if int_value <= 0:
        return handle_invalid()

    config = load_config()
    config.timeout_seconds = int_value
    save_config(config)
    cliff_print(f"Updated timeout to {timeout} seconds")
    return 0


# -- Remove Functions -- #


def remove_provider(provider: str) -> int:
    config = load_config()
    exists = provider in config.provider_credentials

    if not exists:
        cliff_print(f"Provider {provider} not found")
        return 1

    del config.provider_credentials[provider]
    save_config(config)

    cliff_print(f"Removed provider {provider}")
    return 0


def remove_ollama_model(model: str) -> int:
    config = load_config()
    if model not in config.ollama_models:
        cliff_print(f"local model {model} not found")
        return 1
    config.ollama_models.remove(model)
    save_config(config)
    cliff_print(f"Removed local model {model}")
    return 0


def prefer_remove(model: str) -> int:
    config = load_config()
    if model not in config.preferred_providers:
        cliff_print(f"Preferred provider for {model} not found")
        return 1

    del config.preferred_providers[model]
    save_config(config)
    cliff_print(f"Removed preferred provider for {model}")
    return 0


# -- Misc Functionality -- #


def reset_config() -> int:
    save_config(DEFAULT_CONFIG)
    cliff_print("Reset config to defaults")
    return 0


def show_config() -> int:
    config = load_config()

    table = Table(
        box=box.ROUNDED,
        show_header=False,
        show_lines=True,
    )
    table.add_column("Key", style="cyan")
    table.add_column("Value")

    default_model = config.default_model
    if default_model:
        table.add_row("Default Model", f"[magenta]{default_model}[/]")
    else:
        table.add_row("Default Model", "[italic red]Not set[/]")

    creds = config.provider_credentials
    if creds:
        cred_list = "\n".join(
            f"[green]{provider}[/]: [dim]{api_key[0]}{'...' if len(api_key) < 8 else api_key[1:4] + '...' + api_key[-4:]}[/]"
            for provider, api_key in creds.items()
        )
    else:
        cred_list = "[italic red]No providers added[/]"
    table.add_row("Provider Credentials", cred_list)

    prefs = config.preferred_providers
    if prefs:
        pref_list = "\n".join(
            f"[magenta]{model}[/] → [green]{provider}[/]"
            for model, provider in prefs.items()
        )
        table.add_row("Preferred Providers", pref_list)

    models = config.ollama_models
    if models:
        model_list = "\n".join(f"• [magenta]{model}[/]" for model in models)
        table.add_row("Ollama Models", model_list)

    memory_window = config.memory_window
    table.add_row("Memory Window", f"{memory_window} Turns")

    timeout = config.timeout_seconds
    table.add_row("Timeout", f"{timeout} Seconds")

    console.print(table)
    print()
    print(
        "For more information on the Cliff configuration system, run cliff --config help."
    )
    return 0


def process_config_command(command: List[str], llm: LLMClient) -> int:
    if len(command) == 0 or command[0] == "help":
        resource_print(HELP_FILE)
        return 0

    elif command[0] == "add":
        if len(command) != 3:
            cliff_print("Usage: add [provider] [api-key] or add ollama [model]")
            return 1
        if command[1] == "ollama":
            return add_ollama_model(command[2])
        else:
            return add_provider(command[1], command[2])

    elif command[0] == "remove":
        if len(command) < 2:
            cliff_print("Usage: remove [provider] or remove ollama [model]")
            return 1
        if command[1] == "ollama":
            if len(command) != 3:
                cliff_print("Usage: remove ollama [model]")
                return 1
            return remove_ollama_model(command[2])
        else:
            return remove_provider(command[1])

    elif command[0] == "default-model":
        if len(command) != 2:
            cliff_print("Usage: default-model [model]")
            return 1
        return set_default_model(command[1], llm)

    elif command[0] == "prefer":
        if len(command) != 3:
            cliff_print("Usage: prefer [model] [provider] or prefer remove [model]")
            return 1
        if command[1] == "remove":
            return prefer_remove(command[2])
        else:
            return prefer_add(command[1], command[2], llm)

    elif command[0] == "memory-window":
        if len(command) != 2:
            cliff_print("Usage: memory-window [window-size]")
            return 1
        return update_memory_window(command[1])

    elif command[0] == "timeout":
        if len(command) != 2:
            cliff_print("Usage: timeout [seconds]")
            return 1
        return update_timeout(command[1])

    elif command[0] == "reset":
        return reset_config()

    elif command[0] == "show":
        return show_config()

    else:
        cliff_print(
            f"Unrecognized config command: {command[0]}. For usage, run cliff --config help"
        )
        return 1
