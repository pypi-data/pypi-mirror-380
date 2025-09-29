# Simple LLM API

A simple and easy-to-use Python wrapper for popular LLM APIs (OpenAI, Anthropic, and more).

## Installation

[uv](https://docs.astral.sh/uv/) is recommended for managing and installing packages in isolated environments.

```bash
uv add simple-llm-api
```

You can also install it using pip:

```bash
pip install simple-llm-api
```

## Features

- 🎯 Simple and consistent interface for multiple LLM providers
- 🤖 Support for OpenAI, Anthropic, Google Gemini, Mistral, DeepSeek, and local LLMs
- 🏠 Local LLM support (run locally hosted models on your own machine)
- 🚀 Easy to use with minimal configuration
- ⚙️ Customizable parameters for each provider
- 🔧 **kwargs support for additional API parameters

## Quick Start

### OpenAI

```python
from simple_llm_api import OpenAIAPI

openai = OpenAIAPI("YOUR_API_KEY")
response = openai.simple_request("Hi!")
print(response)
```

### Anthropic

```python
from simple_llm_api import AnthropicAPI

anthropic = AnthropicAPI("YOUR_API_KEY")
response = anthropic.simple_request("Hi!")
print(response)
```

### Google Gemini

```python
from simple_llm_api import GeminiAPI

gemini = GeminiAPI("YOUR_API_KEY")
response = gemini.simple_request("Hi!")
print(response)
```

### Mistral

```python
from simple_llm_api import MistralAPI

mistral = MistralAPI("YOUR_API_KEY")
response = mistral.simple_request("Hi!")
print(response)
```

### DeepSeek

```python
from simple_llm_api import DeepSeekAPI

deepseek = DeepSeekAPI("YOUR_API_KEY")
response = deepseek.simple_request("Hi!")
print(response)
```

### Local LLMs

Use locally hosted models on your computer that work like OpenAI's API (like LM Studio or Ollama).

```python
from simple_llm_api import OpenAIAPI

openai = OpenAIAPI(model="MODEL_NAME")
openai._openai_endpoint = "http://localhost:8080/v1/chat/completions"
response = openai.simple_request("Hi!")
print(response)
```

## Advanced Usage

Each API wrapper supports various parameters for customizing the response, plus **kwargs for additional API-specific parameters:

### OpenAI
```python
openai.simple_request(
    user_prompt="Your prompt here",
    system_prompt="Custom system prompt",
    temperature=1,
    top_p=1,
    max_completion_tokens=2048
)
```

### Anthropic
```python
anthropic.simple_request(
    user_prompt="Your prompt here",
    system_prompt="Custom system prompt",
    temperature=1,
    max_tokens=2048
)
```

### Gemini
```python
gemini.simple_request(
    user_prompt="Your prompt here",
    system_prompt="Custom system prompt",
    temperature=1,
    top_k=40,
    top_p=0.95,
    max_output_tokens=2048
)
```

### Mistral
```python
mistral.simple_request(
    user_prompt="Your prompt here",
    system_prompt="Custom system prompt",
    temperature=0.7,
    top_p=1,
    max_tokens=2048
)
```

### DeepSeek
```python
deepseek.simple_request(
    user_prompt="Your prompt here",
    system_prompt="Custom system prompt",
    temperature=1,
    top_p=1,
    max_tokens=2048
)
```

## Error Handling

The library includes custom exceptions for each API:

- `OpenAIError`: OpenAIAPI Error
- `AnthropicError`: AnthropicAPI Error
- `GeminiError`: GeminiAPI Error
- `MistralError`: MistralAPI Error
- `DeepSeekError`: DeepSeekAPI Error

## Disclaimer

This software is provided "as is" without any warranty. The authors are not responsible for any problems that may happen when you use this software.

This library connects to third-party LLM APIs (OpenAI, Anthropic, Google Gemini, Mistral, and DeepSeek). You must follow the rules of these APIs and manage any costs yourself.

You are responsible for how you use this software and what you do with it.

Using this software means you accept these terms.

## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License.

## Links

- [GitHub Repository](https://github.com/SoAp9035/simple-llm-api)
- [PyPI Package](https://pypi.org/project/simple-llm-api/)
- [Buy Me a Coffee](https://buymeacoffee.com/soap9035/)
- [Visit My Website](https://ahmetburhan.com/)