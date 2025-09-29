# Installation

## Basic Installation
```bash
pip install multi-agent-generator
```

## Development Installation
```bash
pip install multi-agent-generator[dev]
```

## Prerequisites

* At least one supported LLM provider (OpenAI, WatsonX, Ollama, etc.)
* Environment variables setup:

  * `OPENAI_API_KEY` (for OpenAI)
  * `WATSONX_API_KEY`, `WATSONX_PROJECT_ID`, `WATSONX_URL` (for WatsonX)
  * `OLLAMA_URL` (for Ollama)
  * Or a generic `API_KEY` / `API_BASE` if supported by LiteLLM

> ⚡ You can freely switch providers using `--provider` in CLI or by setting environment variables.
