# CheapAIModel Python SDK

Lightweight Python client for the [CheapAIModel](https://cheapaimodel.com) API.

CheapAIModel is OpenAI-compatible, so this SDK extends the official `openai` package — every method you know from OpenAI works the same way.

## Install

```bash
pip install cheapaimodel
```

## Usage

```python
from cheapaimodel import CheapAIModel

client = CheapAIModel()  # reads CHEAPAIMODEL_API_KEY

res = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Hello!"}],
)
print(res.choices[0].message.content)

# Shortcut for one-off prompts
print(client.chat_text("Summarize the plot of Romeo and Juliet in one line."))
```

### Streaming

```python
stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Tell me a joke"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```

### Async

```python
import asyncio
from cheapaimodel import AsyncCheapAIModel

async def main():
    client = AsyncCheapAIModel()
    print(await client.chat_text("Hello from async!"))

asyncio.run(main())
```

## Configuration

| Option | Env variable | Default |
| --- | --- | --- |
| `api_key` | `CHEAPAIMODEL_API_KEY` | — (required) |
| `base_url` | `CHEAPAIMODEL_BASE_URL` | `https://api.cheapaimodel.com/v1` |

Any other argument (`timeout`, `max_retries`, ...) is passed straight to the OpenAI client.

## Development

```bash
pip install -e ".[dev]"
pytest
```

## License

MIT
