# Cliff: Generate Unix Commands in the Terminal

![CI](https://github.com/pkelaita/cliff/actions/workflows/ci.yml/badge.svg) [![codecov](https://codecov.io/gh/pkelaita/Cliff/graph/badge.svg?token=oQ9Jp8spXX)](https://codecov.io/gh/pkelaita/Cliff) [![PyPI Version](https://badge.fury.io/py/cliff-cli.svg?timestamp=1759276041)](https://pypi.org/project/cliff-cli/)

Cliff (**C**ommand **L**ine **I**nter**F**ace **F**riend) is an AI assistant that helps you come up with Unix commands. Given an objective (for example, "kill the process running on port 8080"), Cliff will generate a command that does the objective and add it to your paste buffer for you to easily paste into your terminal.

![demo](https://i.imgur.com/uer28Mi.gif)

Cliff is compatible with LLMs from closed-source providers (OpenAI, Anthropic etc.), inference providers (Groq, Cerebras, etc.), as well as local models running with [Ollama](https://ollama.com/).

## Why?

It's annoying having to open the browser when I forget how to do something in the terminal.

## Requirements

- At least one of the following:
  - A valid API key from [OpenAI](https://platform.openai.com/), [Anthropic](https://www.anthropic.com/api), [Google](https://ai.google.dev/), [Cohere](https://cohere.com/), [Groq](https://console.groq.com/login), [Replicate](https://replicate.com/), [Mistral](https://docs.mistral.ai/deployment/laplateforme/overview/), or [Cerebras](https://cloud.cerebras.ai/).
  - An LLM running locally with [Ollama](https://ollama.com/).
- A Unix-like operating system
- Python >= 3.9

## Installation

You can install Cliff with homebrew:

```bash
brew install pkelaita/tap/cliff
```

Or with pip:

```bash
pip install cliff-cli
```

If installing with pip, it's recommended to use [pipx](https://pipx.pypa.io/stable/) or another isolated environment manager since Cliff is a globally-installed application.

## Configuration

If you'd like to use models from an API-based provider, add its credentials as follows:

```
cliff --config add [provider] [api key]
```

The provider can be any of `openai`, `anthropic`, `google`, `cohere`, `groq`, `replicate`, `mistral`, or `cerebras`.

Otherwise if you want to use a local model, add it like this:

```
cliff --config add ollama [model]
```

For the full list of supported models and providers, see Cliff's [Supported Models](docs/supported_models.md).

_Configuration tips_

- In order to use local models, make sure you have Ollama installed and running and have the model loaded ([their docs](https://github.com/ollama/ollama#readme)).
- If you add multiple models, you can set your default model with: `cliff --config default-model [model]`.

For a full overview of the configuration system, run `cliff --config help`.

## Usage

Get started by running `cliff` with an objective.

```
cliff kill the process running on port 8080
```

Cliff will automatically add the command to your paste buffer, so no need to copy-paste it.

If needed (i.e., to avoid escaping special characters), you can use quotes.

```bash
cliff "kill the process that's running on port 8080"
```

If you want to specify which model to use, you can do so with the `--model` or `-m` flag.

```
cliff --model gpt-4o-mini kill the process running on port 8080
```

To view the man page, run `cliff` with no arguments.

### Chat Memory

By default, Cliff has chat memory enabled with a sliding window size of 10 turns. You can view your memory with `cliff --memory show` and clear it with `cliff --memory clear`.

If you'd like to change the window size, run `cliff --config memory-window [new size]`. If you want to disable memory, just set the window size to 0.

### Command Notepad

Cliff's chat memory does not have access to command outputs, but you can optionally share them with Cliff to help it debug and improve its responses via its command notepad.

- To run a command and store its output for Cliff, run `cliff --notepad run [command]`.
- To view your command notepad, run `cliff --notepad show`, and to clear it, run `cliff --notepad clear`.
- `-n` can be used as an alias for `--notepad`.

_Tip:_ You'll usually have to put quotes around your command if it contains special characters – e.g., `cliff --notepad run "ps ax | head -n 10"` – for Cliff to properly capture and execute it.

### Other Useful Features

- The default generation timeout is 20 seconds. You can change it by running `cliff --config timeout [new timeout]`.
- To view your configuration, run `cliff --config show`.
- You can run `cliff --clear` as a shortcut to clear both Cliff's chat memory and command notepad.

That's it! It's pretty simple which is the point.

## Planned Features

- Regular updates with new models, etc.
- UX improvements: cosmetic updates, model aliases, etc.
- Not sure what else this thing really needs, but open to suggestions!
