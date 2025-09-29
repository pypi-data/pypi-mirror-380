# WeyCP Python Client# WeyCP Python Client



[![PyPI version](https://badge.fury.io/py/weycop.svg)](https://badge.fury.io/py/weycop)Official Python client for WeyCP API - OpenAI-compatible chat completions using Ollama.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)## Installation



The official Python client for WeyCP API - OpenAI-compatible chat completions powered by Ollama.```bash

pip install weycop

## Features```



- 🚀 **OpenAI-compatible API** - Drop-in replacement for OpenAI client## Quick Start

- 🔄 **Sync & Async support** - Use synchronous or asynchronous clients

- 🛡️ **Built-in error handling** - Comprehensive exception handling### Synchronous Usage

- 📊 **Usage tracking** - Monitor token usage and costs

- 🎯 **Type hints** - Full type annotation support```python

- ⚡ **High performance** - Optimized for concurrent requestsimport weycop



## Installation# Initialize client

client = weycop.WeycopClient(api_key="your-api-key-here")

```bash

pip install weycop# Simple chat

```response = client.chat("Hello, how are you?")

print(response)

## Quick Start

# Advanced chat completion

### Synchronous Clientfrom weycop import Message



```pythoncompletion = client.chat_completions_create(

from weycop import WeycopClient    model="llama3.2:3b",

    messages=[

# Initialize client        Message("system", "You are a helpful assistant."),

client = WeycopClient(api_key="your-api-key")        Message("user", "Explain quantum computing in simple terms.")

    ],

# Simple chat    temperature=0.7,

response = client.chat(    max_tokens=150

    message="Hello, how are you?",)

    model="llama3.2:3b",

    system_prompt="You are a helpful assistant"print(completion.choices[0].message.content)

)print(f"Used {completion.usage.total_tokens} tokens")

print(response)```



# Advanced usage### Asynchronous Usage

completion = client.chat_completions_create(

    model="llama3.2:3b",```python

    messages=[import asyncio

        {"role": "system", "content": "You are a helpful assistant"},import weycop

        {"role": "user", "content": "Explain quantum computing"}

    ],async def main():

    temperature=0.7,    async with weycop.AsyncWeycopClient(api_key="your-api-key-here") as client:

    max_tokens=500        response = await client.chat("What's the weather like?")

)        print(response)

print(completion.choices[0].message.content)

```asyncio.run(main())

```

### Asynchronous Client

## Configuration

```python

import asyncio### Environment Variables

from weycop import AsyncWeycopClient

You can set your API key using environment variables:

async def main():

    async with AsyncWeycopClient(api_key="your-api-key") as client:```bash

        response = await client.chat(export WEYCOP_API_KEY="your-api-key-here"

            message="What is machine learning?",export WEYCOP_BASE_URL="https://api.weycop.com"  # Optional

            model="llama3.1:8b-8k"```

        )

        print(response)### Client Configuration



asyncio.run(main())```python

```client = weycop.WeycopClient(

    api_key="your-api-key-here",

## Supported Models    base_url="https://api.weycop.com",  # Optional

    timeout=120.0  # Optional, request timeout in seconds

- `llama3.2:3b` - Fast, lightweight model (4GB VRAM))

- `llama3.1:8b-8k` - Advanced model with 8K context (8.5GB VRAM)```



## Error Handling## Available Models



```python- `llama3.2:3b` - Fast model for general chat and small tasks

from weycop import WeycopClient, AuthenticationError, RateLimitError, APIError- `llama3.1:8b` - More powerful model for complex reasoning and SQL tasks



client = WeycopClient(api_key="your-key")## API Reference



try:### WeycopClient Methods

    response = client.chat("Hello", model="llama3.2:3b")

except AuthenticationError:#### `chat_completions_create()`

    print("Invalid API key")

except RateLimitError:Create a chat completion with full control over parameters.

    print("Rate limit exceeded")

except APIError as e:```python

    print(f"API error: {e}")completion = client.chat_completions_create(

```    model="llama3.2:3b",

    messages=[Message("user", "Hello!")],

## Advanced Usage    temperature=0.7,        # Optional: 0-2, controls randomness

    top_p=0.9,             # Optional: 0-1, nucleus sampling

### Custom Parameters    max_tokens=500,        # Optional: max tokens to generate

    stop=["\\n\\n"],        # Optional: stop sequences

```python)

response = client.chat_completions_create(```

    model="llama3.2:3b",

    messages=[{"role": "user", "content": "Write a short story"}],#### `chat()`

    temperature=0.8,

    max_tokens=1000,Simplified chat interface for quick interactions.

    top_p=0.9,

    stop=["END", "###"]```python

)response = client.chat(

```    message="Explain photosynthesis",

    model="llama3.1:8b",           # Optional, default: "llama3.2:3b"

### Health Check    system_prompt="Be concise",    # Optional

    temperature=0.5                # Optional

```python)

health = client.health_check()```

print(f"Status: {health.status}")

print(f"Models: {len(health.ollama_models)}")#### `health_check()`

```

Check API status and available models.

## Examples

```python

Check the `examples/` directory for more usage examples:health = client.health_check()

- `basic_usage.py` - Simple chat completionsprint(health.status)

- `error_handling.py` - Comprehensive error handlingprint(health.ollama_models)

```

## API Documentation

### Data Models

Visit [https://api.weycop.com/docs](https://api.weycop.com/docs) for complete API documentation.

#### Message

## Support

```python

- 📧 Email: [dev@weycop.com](mailto:dev@weycop.com)from weycop import Message

- 🐛 Issues: [GitHub Issues](https://github.com/weycop/weycop-python/issues)

- 📖 Docs: [https://docs.weycop.com](https://docs.weycop.com)msg = Message(role="user", content="Hello!")

# Roles: "system", "user", "assistant"

## License```



MIT License - see [LICENSE](LICENSE) file for details.#### ChatCompletion

Response object containing the completion result:

```python
completion = client.chat_completions_create(...)

print(completion.id)              # Unique request ID
print(completion.model)           # Model used
print(completion.usage.total_tokens)  # Token usage
print(completion.choices[0].message.content)  # Response text
```

## Error Handling

```python
import weycop
from weycop import AuthenticationError, RateLimitError, APIError

try:
    client = weycop.WeycopClient(api_key="invalid-key")
    response = client.chat("Hello")
except AuthenticationError:
    print("Invalid API key")
except RateLimitError:
    print("Rate limit exceeded")
except APIError as e:
    print(f"API error: {e}")
except weycop.WeycopError as e:
    print(f"Client error: {e}")
```

## Examples

### System Prompts

```python
completion = client.chat_completions_create(
    model="llama3.1:8b",
    messages=[
        Message("system", "You are a SQL expert. Only respond with SQL code."),
        Message("user", "Get all users created in the last 30 days")
    ]
)
```

### Multi-turn Conversation

```python
messages = [
    Message("system", "You are a helpful math tutor."),
    Message("user", "What is 15 + 27?"),
]

# First response
completion = client.chat_completions_create(model="llama3.2:3b", messages=messages)
assistant_response = completion.choices[0].message.content
messages.append(Message("assistant", assistant_response))

# Follow-up question
messages.append(Message("user", "Now multiply that by 3"))
completion = client.chat_completions_create(model="llama3.2:3b", messages=messages)
print(completion.choices[0].message.content)
```

### Context Management

```python
# Use with statement for automatic cleanup
with weycop.WeycopClient(api_key="your-key") as client:
    response = client.chat("Hello!")
    print(response)
# Client is automatically closed
```

## License

MIT License - see LICENSE file for details.

## Support

- Documentation: https://docs.weycop.com
- GitHub Issues: https://github.com/weycop/weycop-python/issues  
- Email: dev@weycop.com