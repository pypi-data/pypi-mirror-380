# Simplified United LLM

A streamlined, lightweight LLM client library that provides unified access to OpenRouter and Ollama providers with structured output generation and comprehensive logging capabilities.

## Features

- **Unified Interface**: Single client for both OpenRouter and Ollama providers
- **Structured Output**: Generate structured data using string-schema definitions
- **Comprehensive Logging**: Daily organized logs with detailed request/response tracking
- **Simple Configuration**: Dictionary-based configuration from JSON files
- **Provider Auto-Detection**: Automatic provider selection based on model prefixes
- **Pydantic Integration**: Built-in validation using Pydantic models

## Installation

```bash
pip install simplified-united-llm
```

### Dependencies

- Python 3.8+
- pydantic>=2.0.0
- string-schema>=0.1.0
- requests>=2.25.0
- openai>=1.0.0

## Quick Start

### 1. Create Configuration File

Create a `united_llm.json` file with your API keys and settings:

```json
{
  "api_keys": {
    "openrouter": "sk-or-v1-your-openrouter-key",
    "ollama": null
  },
  "base_urls": {
    "openrouter": "https://openrouter.ai/api/v1",
    "ollama": "http://localhost:11434/v1"
  },
  "log_dir": "logs/llm_calls"
}
```

### 2. Initialize Client

```python
import json
from united_llm import LLMClient

# Load configuration
with open('united_llm.json', 'r') as f:
    config = json.load(f)

# Initialize client
client = LLMClient(config_dict=config)
```

### 3. Generate Structured Output

```python
# Extract structured data using OpenRouter
result = client.generate_dict(
    prompt="Extract info: John Doe, 30, from NYC, works as engineer",
    schema="{name, age:int, city, job}",
    model="openrouter:google/gemini-2.5-flash-lite"
)
print(result)
# Output: {"name": "John Doe", "age": 30, "city": "NYC", "job": "engineer"}

# Generate using local Ollama model
result = client.generate_dict(
    prompt="Analyze sentiment: This product is amazing!",
    schema="{sentiment, confidence:float}",
    model="ollama:qwen2.5:3b"
)
print(result)
# Output: {"sentiment": "positive", "confidence": 0.95}
```

## Schema Syntax

The library uses [string-schema](https://github.com/unaidedelf87/string-schema) for defining structured output formats:

### Basic Types
```python
# Simple object
"{name, age:int, email}"

# With arrays
"{name, hobbies: [string]}"

# Nested objects
"{user: {name, email}, posts: [{title, content}]}"

# Different data types
"{score:float, active:bool, count:int}"
```

### Array Schemas
```python
# Array of objects
"[{name, score:float}]"

# Array of primitives
"[string]"
"[int]"
```

## Supported Providers

### OpenRouter
- **Prefix**: `openrouter:`
- **Example**: `openrouter:google/gemini-2.5-flash-lite`
- **Requirements**: API key required
- **Models**: All OpenRouter supported models

### Ollama
- **Prefix**: `ollama:`
- **Example**: `ollama:qwen2.5:3b`
- **Requirements**: Local Ollama server running
- **Models**: Any model available in your Ollama installation

## Configuration

### Required Configuration Keys

- `api_keys`: Dictionary with provider API keys
- `base_urls`: Dictionary with provider base URLs

### Optional Configuration Keys

- `log_dir`: Directory for log files (default: "logs/llm_calls")

### Example Configuration

```json
{
  "api_keys": {
    "openrouter": "sk-or-v1-...",
    "ollama": null
  },
  "base_urls": {
    "openrouter": "https://openrouter.ai/api/v1",
    "ollama": "http://localhost:11434/v1"
  },
  "log_dir": "logs/llm_calls"
}
```

## Logging

The library automatically logs all requests and responses to daily log files:

```
logs/llm_calls/2025-01-23.log
```

Log format:
```
2025-01-23 10:30:15 | openrouter:google/gemini-2.5-flash-lite | openrouter | Extract info: John... | {name, age:int, city} | {"name": "John Doe", "age": 30, "city": "NYC"} | 1.25s
```

## Testing

Run the included test program:

```bash
python examples/test_models.py
```

This will test both OpenRouter and Ollama providers with sample prompts.

## Error Handling

The library provides clear error messages for common issues:

- **Configuration errors**: Invalid or missing configuration keys
- **Provider errors**: API failures, network issues, authentication problems
- **Schema errors**: Invalid string-schema definitions
- **Model errors**: Unsupported models or provider prefixes

## Development

### Project Structure

```
simplified-united-llm/
├── setup.py
├── requirements.txt
├── README.md
├── united_llm/
│   ├── __init__.py
│   ├── client.py
│   ├── providers/
│   │   ├── __init__.py
│   │   ├── openrouter.py
│   │   └── ollama.py
│   └── utils/
│       ├── __init__.py
│       ├── logging.py
│       └── schema_parser.py
├── tests/
│   ├── __init__.py
│   └── test_client.py
├── examples/
│   └── test_models.py
└── united_llm.json
```

### Running Tests

```bash
pip install pytest
pytest tests/
```

## License

MIT License - see LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.