# WeyCP Python Client

[![PyPI version](https://badge.fury.io/py/weycop.svg)](https://badge.fury.io/py/weycop)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

The official Python client for **WeyCP API** chat completions created by Weycop.

---

## 🚀 Features

* **Familiar API Interface** – Easy-to-use chat completions API.
* **Sync & Async support** – Use synchronous or asynchronous clients.
* **Built-in error handling** – Comprehensive exception handling.
* **Usage tracking** – Monitor token usage and costs.
* **Type hints** – Full type annotation support.
* **High performance** – Optimized for concurrent requests.

---

## 📦 Installation

```bash
pip install weycop
```

---

## ⚡ Quick Start

### Synchronous Client

```python
from weycop import WeycopClient

# Initialize client
client = WeycopClient(api_key="your-api-key")

# Simple chat
response = client.chat(
    message="Hello, how are you?",
    model="llama3.2:3b",
    system_prompt="You are a helpful assistant"
)
print(response)
```

### Asynchronous Client

```python
import asyncio
from weycop import AsyncWeycopClient

async def main():
    async with AsyncWeycopClient(api_key="your-api-key") as client:
        response = await client.chat(
            message="What is machine learning?",
            model="llama3.1:8b-8k"
        )
        print(response)

asyncio.run(main())
```

---

## 🧠 Supported Models

* `llama3.2:3b` – Fast, lightweight model (~4 GB VRAM).
* `llama3.1:8b-8k` – Advanced model with 8K context (~8.9 GB VRAM).

---

## 🛡️ Error Handling

```python
from weycop import WeycopClient, AuthenticationError, RateLimitError, APIError

client = WeycopClient(api_key="your-key")

try:
    response = client.chat("Hello", model="llama3.2:3b")
    print(response)
except AuthenticationError:
    print("Invalid API key")
except RateLimitError:
    print("Rate limit exceeded")
except APIError as e:
    print(f"API error: {e}")
```

---

## 🔄 Examples

### System Prompts

```python
from weycop import Message

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

completion = client.chat_completions_create(model="llama3.2:3b", messages=messages)
assistant_response = completion.choices[0].message.content
messages.append(Message("assistant", assistant_response))

messages.append(Message("user", "Now multiply that by 3"))
completion = client.chat_completions_create(model="llama3.2:3b", messages=messages)
print(completion.choices[0].message.content)
```

### Context Management

```python
with WeycopClient(api_key="your-key") as client:
    response = client.chat("Hello!")
    print(response)
# Client is automatically closed
```

---

---

## Support

* Email: [apps@weycop.com](mailto:apps@weycop.com)

---

## 📜 License

MIT License - see [LICENSE](LICENSE) file for details.