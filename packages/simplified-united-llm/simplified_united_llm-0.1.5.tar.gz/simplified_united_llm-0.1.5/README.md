# Simplified United LLM

[![PyPI version](https://badge.fury.io/py/simplified-united-llm.svg)](https://badge.fury.io/py/simplified-united-llm)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A streamlined, lightweight LLM client library that provides unified access to **OpenRouter** and **Ollama** providers with structured output generation, multi-image vision processing, and schema prompt enhancement.

## ✨ Key Features

- **🤖 Three Generation Methods**: `gen_text()`, `gen_dict()`, `gen_pydantic()`
- **🔌 Dual Provider Support**: OpenRouter (cloud) + Ollama (local)
- **👁️ Multi-Image Vision**: Process multiple images simultaneously
- **🎯 Schema Enhancement**: Optional prompt enhancement for better compliance
- **🔗 String-Schema Integration**: Automatic validation and conversion
- **📝 Comprehensive Logging**: Daily organized logs with detailed tracking
- **⚙️ Simple Configuration**: JSON-based configuration
- **🔍 Provider Auto-Detection**: Automatic provider selection from model prefixes

## 📦 Installation

```bash
pip install simplified-united-llm
```

### Requirements

- **Python**: 3.8+
- **Dependencies**: `instructor>=1.3.0`, `pydantic>=2.0.0`, `string-schema>=0.1.0`, `openai>=1.0.0`

## 🚀 Quick Start

### 1. Configuration Setup

Copy the example configuration and add your API keys:

```bash
cp united_llm.json.example united_llm.json
```

Edit `united_llm.json`:
```json
{
  "api_keys": {
    "openrouter": "your-openrouter-api-key-here",
    "ollama": null
  },
  "base_urls": {
    "openrouter": "https://openrouter.ai/api/v1",
    "ollama": "http://localhost:11434/v1"
  },
  "log_dir": "logs/llm_calls"
}
```

### 2. Basic Usage

```python
from united_llm import LLMClient
from pydantic import BaseModel
from typing import List

# Initialize client (auto-loads united_llm.json)
client = LLMClient()

# 1. Text Generation
text = client.gen_text(
    model="ollama:qwen3:8b",
    prompt="Explain quantum computing in simple terms."
)

# 2. Dictionary Generation with Schema Enhancement
data = client.gen_dict(
    model="ollama:qwen3:8b",
    prompt="Extract: John Smith, 30, Engineer in Boston",
    schema="{name: str, age: int, job: str, city: str}",
    add_schema_to_prompt=True  # 🎯 Enhanced compliance!
)
# Output: {"name": "John Smith", "age": 30, "job": "Engineer", "city": "Boston"}

# 3. Pydantic Model Generation
class Person(BaseModel):
    name: str
    age: int
    occupation: str
    city: str

person = client.gen_pydantic(
    model="ollama:qwen3:8b",
    prompt="Extract: Alice Johnson, 25, Designer in Seattle",
    response_model=Person,
    add_schema_to_prompt=True  # 🎯 Enhanced compliance!
)
# Output: Person(name="Alice Johnson", age=25, occupation="Designer", city="Seattle")
```

### 3. Multi-Image Vision Processing

```python
from united_llm.utils.image_input import ImageInput

# Load multiple images
images = [
    ImageInput("image1.jpg", name="first"),
    ImageInput("image2.png", name="second")
]

# Analyze multiple images with structured output
class ImageAnalysis(BaseModel):
    description: str
    text_content: str
    objects_detected: List[str]
    image_type: str

result = client.gen_pydantic(
    model="openrouter:google/gemini-2.5-flash-lite",
    prompt="Analyze these images and extract key information",
    response_model=ImageAnalysis,
    images=images,
    add_schema_to_prompt=True
)
```

## 🎯 Core Methods

### `gen_text(model, prompt, images=None)`
Generate plain text responses.

### `gen_dict(model, prompt, schema, images=None, add_schema_to_prompt=False)`
Generate structured dictionaries with schema validation.

### `gen_pydantic(model, prompt, response_model, images=None, add_schema_to_prompt=False)`
Generate validated Pydantic model instances.

## 📋 Schema Syntax

Uses [string-schema](https://github.com/unaidedelf87/string-schema) format:

```python
# Basic types
"{name: str, age: int, active: bool, score: float}"

# Arrays
"{tags: [str], scores: [float]}"

# Nested objects
"{user: {name: str, email: str}, posts: [{title: str, content: str}]}"
```

## 🔌 Supported Providers

### OpenRouter (Cloud)
- **Prefix**: `openrouter:`
- **Example**: `openrouter:google/gemini-2.5-flash-lite`
- **Requirements**: API key required
- **Vision Support**: ✅ (with compatible models)
- **Models**: All OpenRouter supported models

### Ollama (Local)
- **Prefix**: `ollama:`
- **Example**: `ollama:qwen3:8b`
- **Requirements**: Local Ollama server running
- **Vision Support**: ❌ (text only)
- **Models**: Any model available in your Ollama installation

## ⚙️ Configuration

### Required Keys
- `api_keys`: Provider API keys
- `base_urls`: Provider endpoints

### Optional Keys
- `log_dir`: Log directory (default: "logs/llm_calls")

### Provider Setup

#### OpenRouter Setup
1. Sign up at [OpenRouter](https://openrouter.ai/)
2. Get your API key
3. Add to `united_llm.json`

#### Ollama Setup
```bash
# Install Ollama
curl -fsSL https://ollama.ai/install.sh | sh

# Pull a model
ollama pull qwen3:8b

# Start server (runs on localhost:11434)
ollama serve
```

## 📝 Logging

Automatic logging to daily files:
```
logs/llm_calls/2024-12-27.log
```

Log format:
```
2024-12-27 10:30:15 | ollama:qwen3:8b | gen_dict | Extract: John... | {"name": "John", "age": 30} | 1.25s
```

## 🧪 Testing

Run the comprehensive test suite:

```bash
# Basic unit tests
python -m pytest tests/test_basic.py -v

# Integration tests (requires API keys and running services)
python -m pytest tests/ -v
```

## 📚 Examples

Comprehensive examples available in the `examples/` directory:

- **`basic_usage.py`** - Perfect starting point for new users
- **`advanced_features.py`** - Complex use cases and schema enhancement
- **`vision_examples.py`** - Multi-image processing examples

```bash
cd examples
python basic_usage.py
```

## 🔧 Advanced Features

### Schema Prompt Enhancement

The `add_schema_to_prompt=True` parameter significantly improves structured output compliance:

```python
# Without enhancement
result = client.gen_dict(
    model="ollama:qwen3:8b",
    prompt="Complex extraction task...",
    schema="{complex: {nested: {schema: str}}}"
)

# With enhancement - better compliance!
result = client.gen_dict(
    model="ollama:qwen3:8b", 
    prompt="Complex extraction task...",
    schema="{complex: {nested: {schema: str}}}",
    add_schema_to_prompt=True  # 🎯 Adds schema to prompt
)
```

### Vision Capabilities

Process multiple images with structured output:

```python
# Single image
image = ImageInput("document.jpg")
text = client.gen_text(
    model="openrouter:google/gemini-2.5-flash-lite",
    prompt="Extract all text from this document",
    images=[image]
)

# Multiple images with comparison
images = [ImageInput("before.jpg"), ImageInput("after.jpg")]
comparison = client.gen_dict(
    model="openrouter:google/gemini-2.5-flash-lite",
    prompt="Compare these two images",
    schema="{similarities: [str], differences: [str], summary: str}",
    images=images,
    add_schema_to_prompt=True
)
```

## 🤝 Contributing

Contributions welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🔗 Links

- **PyPI Package**: https://pypi.org/project/simplified-united-llm/
- **GitHub Repository**: https://github.com/xychenmsn/simplified-united-llm
- **String-Schema Library**: https://github.com/unaidedelf87/string-schema
