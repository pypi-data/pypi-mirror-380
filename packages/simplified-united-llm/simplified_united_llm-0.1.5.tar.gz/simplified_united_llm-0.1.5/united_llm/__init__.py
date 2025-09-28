#!/usr/bin/env python3
"""
Simplified United LLM - A streamlined LLM client library

This package provides unified access to OpenRouter and Ollama providers
with structured output generation and comprehensive logging capabilities.

Main Methods:
- gen_text(model, prompt, images=None, **kwargs): Generate plain text output
- gen_dict(model, prompt, schema, images=None, **kwargs): Generate dictionary output using string schema
- gen_pydantic(model, prompt, response_model, images=None, **kwargs): Generate structured output using Pydantic models

All methods support vision-capable models when images parameter is provided.
"""

from .client import LLMClient

__version__ = "0.1.0"
__author__ = "United LLM Team"
__email__ = "team@united-llm.com"

# Public API
__all__ = [
    "LLMClient",
]

# Package metadata
__title__ = "simplified-united-llm"
__description__ = "A streamlined, lightweight LLM client library for OpenRouter and Ollama providers"
__url__ = "https://github.com/united-llm/simplified-united-llm"
__license__ = "MIT"