#!/usr/bin/env python3
"""
Main LLM Client for Simplified United LLM

Provides unified access to OpenRouter and Ollama providers with structured output generation.
"""

from typing import Dict, Any, Optional, List, Type, TypeVar, Tuple
from pathlib import Path
from pydantic import BaseModel

from .providers.openrouter import OpenRouterProvider
from .providers.ollama import OllamaProvider
from .utils.logging import setup_logging, log_llm_call
from .utils.schema_parser import SchemaParser
from .utils.image_input import ImageInput

# Import string-schema for direct dict validation
try:
    from string_schema import validate_to_dict
except ImportError:
    validate_to_dict = None

T = TypeVar('T')


class LLMClient:
    """
    Simplified LLM Client for OpenRouter and Ollama providers.
    
    This client provides a unified interface for generating structured outputs
    from LLM providers using string-schema definitions.
    """
    
    def __init__(self, config_dict: Dict[str, Any]):
        """
        Initialize the LLM Client with configuration dictionary.
        
        Args:
            config_dict: Configuration dictionary containing:
                - api_keys: Dict with provider API keys
                - base_urls: Dict with provider base URLs
                - log_dir: Directory for log files
        
        Example:
            config = {
                "api_keys": {
                    "openrouter": "sk-or-v1-...",
                    "ollama": None
                },
                "base_urls": {
                    "openrouter": "https://openrouter.ai/api/v1",
                    "ollama": "http://localhost:11434/v1"
                },
                "log_dir": "logs/llm_calls"
            }
            client = LLMClient(config_dict=config)
        """
        self.config = config_dict
        self._validate_config()
        
        # Setup logging
        log_dir = Path(self.config.get("log_dir", "logs/llm_calls"))
        self.logger, self.txt_log_folder = setup_logging(log_dir)
        
        # Initialize providers
        self.providers = {
            "openrouter": OpenRouterProvider(
                api_key=self.config["api_keys"].get("openrouter"),
                base_url=self.config["base_urls"].get("openrouter", "https://openrouter.ai/api/v1")
            ),
            "ollama": OllamaProvider(
                base_url=self.config["base_urls"].get("ollama", "http://localhost:11434/v1")
            )
        }
        
        # Initialize schema parser
        self.schema_parser = SchemaParser()
        
        self.logger.info("LLMClient initialized successfully")
    
    def _validate_config(self) -> None:
        """
        Validate the configuration dictionary.
        
        Raises:
            ValueError: If configuration is invalid
        """
        if not isinstance(self.config, dict):
            raise ValueError("config_dict must be a dictionary")
        
        required_keys = ["api_keys", "base_urls"]
        for key in required_keys:
            if key not in self.config:
                raise ValueError(f"Missing required configuration key: {key}")
        
        # Validate API keys structure
        api_keys = self.config["api_keys"]
        if not isinstance(api_keys, dict):
            raise ValueError("api_keys must be a dictionary")
        
        # Validate base URLs structure
        base_urls = self.config["base_urls"]
        if not isinstance(base_urls, dict):
            raise ValueError("base_urls must be a dictionary")
    
    def _detect_provider(self, model: str) -> tuple[str, str]:
        """
        Detect provider from model string.
        
        Args:
            model: Model string with provider prefix (e.g., "openrouter:google/gemini-2.5-flash-lite")
        
        Returns:
            Tuple of (provider_name, actual_model_name)
        
        Raises:
            ValueError: If provider prefix is not recognized
        """
        if ":" not in model:
            raise ValueError(f"Model must include provider prefix (openrouter: or ollama:): {model}")
        
        provider, actual_model = model.split(":", 1)
        
        if provider not in ["openrouter", "ollama"]:
            raise ValueError(f"Unsupported provider: {provider}. Supported providers: openrouter, ollama")
        
        return provider, actual_model
    
    def _generate_base(self, prompt: str, model: str, response_format: str = "text", schema: Optional[str] = None, response_model: Optional[Type[BaseModel]] = None, images: Optional[List] = None) -> Tuple[Any, Optional[Dict[str, Any]]]:
        """
        Base generation method that handles all types of output formats.
        
        Args:
            prompt: Input prompt for generation
            model: Model identifier (e.g., "openrouter:google/gemini-2.0-flash-exp", "ollama:llama3.2")
            response_format: Type of response ("text", "dict", "pydantic")
            schema: JSON schema as string for dict output
            response_model: Pydantic model class for structured output
            images: Optional list of images for vision models
        
        Returns:
            Tuple of (result, metadata)
        
        Raises:
            ValueError: If inputs are invalid
            RuntimeError: If generation fails
        """
        import time
        import json
        start_time = time.time()
        
        try:
            # Validate inputs
            if not prompt or not isinstance(prompt, str):
                raise ValueError("prompt must be a non-empty string")
            if not model or not isinstance(model, str):
                raise ValueError("model must be a non-empty string")
            
            if response_format == "dict" and (not schema or not isinstance(schema, str)):
                raise ValueError("schema must be a non-empty string for dict format")
            if response_format == "pydantic" and not response_model:
                raise ValueError("response_model must be provided for pydantic format")
            
            # Detect provider
            provider_name, actual_model = self._detect_provider(model)
            
            # Get provider instance
            provider = self.providers[provider_name]
            
            # Prepare the model for structured output
            if response_format == "dict":
                # For dict format, we'll use a different approach
                # First get text output, then validate with string-schema
                pydantic_model = None
            elif response_format == "pydantic":
                pydantic_model = response_model
            else:  # text format
                pydantic_model = None
            
            # Generate response using provider with metadata if available
            usage_metadata = None
            if response_format == "text":
                # For text generation, we need to handle it differently
                if images:
                    # Use vision API but extract text content
                    from pydantic import BaseModel
                    class TextResponse(BaseModel):
                        text: str

                    if hasattr(provider, 'generate_with_vision_metadata'):
                        result, usage_metadata = provider.generate_with_vision_metadata(
                            prompt=prompt,
                            model=actual_model,
                            response_model=TextResponse,
                            images=images
                        )
                        result = result.text
                    elif hasattr(provider, 'generate_with_vision'):
                        result = provider.generate_with_vision(
                            prompt=prompt,
                            model=actual_model,
                            response_model=TextResponse,
                            images=images
                        )
                        result = result.text
                    else:
                        raise ValueError(f"Provider {provider_name} does not support vision generation")
                else:
                    # Direct text generation
                    if hasattr(provider, 'generate_text'):
                        # Use direct text generation method if available (e.g., Ollama)
                        result = provider.generate_text(
                            prompt=prompt,
                            model=actual_model
                        )
                    else:
                        # Fallback to structured output with a simple text wrapper
                        from pydantic import BaseModel
                        class TextResponse(BaseModel):
                            text: str

                        if hasattr(provider, 'generate_with_metadata'):
                            result, usage_metadata = provider.generate_with_metadata(
                                prompt=prompt,
                                model=actual_model,
                                response_model=TextResponse
                            )
                            result = result.text
                        else:
                            result = provider.generate(
                                prompt=prompt,
                                model=actual_model,
                                response_model=TextResponse
                            )
                            result = result.text
            elif response_format == "dict":
                # For dict format, generate text and then validate with string-schema
                enhanced_prompt = f"{prompt}\n\nPlease respond with a JSON object that matches this schema: {schema}"

                if images:
                    if hasattr(provider, 'generate_text_with_vision'):
                        raw_result = provider.generate_text_with_vision(
                            prompt=enhanced_prompt,
                            model=actual_model,
                            images=images
                        )
                    else:
                        # Fallback to text response model for vision
                        from pydantic import BaseModel
                        class TextResponse(BaseModel):
                            text: str

                        if hasattr(provider, 'generate_with_vision_metadata'):
                            text_result, usage_metadata = provider.generate_with_vision_metadata(
                                prompt=enhanced_prompt,
                                model=actual_model,
                                response_model=TextResponse,
                                images=images
                            )
                            raw_result = text_result.text
                        elif hasattr(provider, 'generate_with_vision'):
                            text_result = provider.generate_with_vision(
                                prompt=enhanced_prompt,
                                model=actual_model,
                                response_model=TextResponse,
                                images=images
                            )
                            raw_result = text_result.text
                        else:
                            raise ValueError(f"Provider {provider_name} does not support vision generation")
                else:
                    if hasattr(provider, 'generate_text'):
                        raw_result = provider.generate_text(
                            prompt=enhanced_prompt,
                            model=actual_model
                        )
                    else:
                        # Fallback to text response model
                        from pydantic import BaseModel
                        class TextResponse(BaseModel):
                            text: str

                        if hasattr(provider, 'generate_with_metadata'):
                            text_result, usage_metadata = provider.generate_with_metadata(
                                prompt=enhanced_prompt,
                                model=actual_model,
                                response_model=TextResponse
                            )
                            raw_result = text_result.text
                        else:
                            text_result = provider.generate(
                                prompt=enhanced_prompt,
                                model=actual_model,
                                response_model=TextResponse
                            )
                            raw_result = text_result.text

                # Parse JSON from the raw result
                import json
                import re
                try:
                    # Try to parse as JSON directly
                    json_data = json.loads(raw_result.strip())
                except json.JSONDecodeError:
                    # Try to extract JSON from the response with better regex
                    # Look for JSON objects, handling nested braces
                    json_matches = re.findall(r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}', raw_result, re.DOTALL)
                    if json_matches:
                        # Try each match until we find valid JSON
                        for match in json_matches:
                            try:
                                json_data = json.loads(match)
                                break
                            except json.JSONDecodeError:
                                continue
                        else:
                            # If no valid JSON found, raise error with truncated output for security
                            truncated_result = raw_result[:200] + "..." if len(raw_result) > 200 else raw_result
                            raise RuntimeError(f"Could not extract valid JSON from response: {truncated_result}")
                    else:
                        truncated_result = raw_result[:200] + "..." if len(raw_result) > 200 else raw_result
                        raise RuntimeError(f"Could not extract valid JSON from response: {truncated_result}")

                # Use string-schema to validate and clean the result
                if validate_to_dict:
                    result = validate_to_dict(json_data, schema)
                else:
                    # Fallback if string-schema is not available
                    result = json_data
            else:
                # Pydantic structured output generation
                if images:
                    if hasattr(provider, 'generate_with_vision_metadata'):
                        result, usage_metadata = provider.generate_with_vision_metadata(
                            prompt=prompt,
                            model=actual_model,
                            response_model=pydantic_model,
                            images=images
                        )
                    elif hasattr(provider, 'generate_with_vision'):
                        result = provider.generate_with_vision(
                            prompt=prompt,
                            model=actual_model,
                            response_model=pydantic_model,
                            images=images
                        )
                    else:
                        raise ValueError(f"Provider {provider_name} does not support vision generation")
                else:
                    if hasattr(provider, 'generate_with_metadata'):
                        result, usage_metadata = provider.generate_with_metadata(
                            prompt=prompt,
                            model=actual_model,
                            response_model=pydantic_model
                        )
                    else:
                        result = provider.generate(
                            prompt=prompt,
                            model=actual_model,
                            response_model=pydantic_model
                        )
            
            # Prepare cost and token information for logging
            cost_info = None
            token_usage = None
            if usage_metadata:
                # Extract cost information
                cost_info = {
                    'cost': usage_metadata.get('total_cost'),  # Main cost field expected by logger
                    'cost_details': {
                        'upstream_inference_cost': usage_metadata.get('upstream_inference_cost'),
                        'upstream_inference_prompt_cost': usage_metadata.get('upstream_inference_prompt_cost'),
                        'upstream_inference_completions_cost': usage_metadata.get('upstream_inference_completions_cost')
                    },
                    'is_byok': usage_metadata.get('is_byok')
                }
                
                # Extract token usage information
                token_usage = {
                    'prompt_tokens': usage_metadata.get('prompt_tokens'),
                    'completion_tokens': usage_metadata.get('completion_tokens'),
                    'total_tokens': usage_metadata.get('total_tokens'),
                    'prompt_tokens_details': usage_metadata.get('prompt_tokens_details'),
                    'completion_tokens_details': usage_metadata.get('completion_tokens_details')
                }
            
            # Prepare result for logging and return
            if response_format == "text":
                log_response = result
                return_value = result
            elif response_format == "dict":
                # Result should already be a dict
                log_response = result
                return_value = result
            else:
                # Convert Pydantic model to dictionary for logging
                result_dict = result.dict() if hasattr(result, 'dict') else result.model_dump()
                log_response = result_dict
                return_value = result
            
            # Log the request and response using per-file logging
            duration_ms = (time.time() - start_time) * 1000
            
            # Include image info in logging
            prompt_with_images = prompt
            if images:
                image_info = f" [Images: {len(images)} attached]"
                prompt_with_images += image_info
            
            log_llm_call(
                txt_log_folder=self.txt_log_folder,
                model=model,
                prompt=prompt_with_images,
                response=log_response,
                duration_ms=duration_ms,
                token_usage=token_usage,
                cost_info=cost_info
            )
            
            return return_value, usage_metadata
            
        except Exception as e:
            duration_ms = (time.time() - start_time) * 1000
            
            # Include image info in error logging
            prompt_with_images = prompt
            if images:
                image_info = f" [Images: {len(images)} attached]"
                prompt_with_images += image_info
            
            # Log the error using per-file logging
            log_llm_call(
                txt_log_folder=self.txt_log_folder,
                model=model,
                prompt=prompt_with_images,
                response=None,
                duration_ms=duration_ms,
                token_usage=None,
                cost_info=None,
                error_info=str(e)
            )
            self.logger.error(
                f"Error generating with {model}: {str(e)} | Duration: {duration_ms:.2f}ms"
            )
            raise RuntimeError(f"Failed to generate structured output: {str(e)}") from e
    
    def gen_text(self, model: str, prompt: str, images: Optional[List] = None) -> str:
        """
        Generate plain text output without structured formatting.
        
        Args:
            model: Model identifier (e.g., "openrouter:google/gemini-2.0-flash-exp", "ollama:llama3.2")
            prompt: Input prompt for generation
            images: Optional list of images for vision models
        
        Returns:
            Plain text response from the model
        
        Raises:
            ValueError: If model format is invalid or provider is unsupported
            RuntimeError: If generation fails
        
        Example:
            text = client.gen_text(
                model="openrouter:google/gemini-2.0-flash-exp",
                prompt="Write a short story about a robot"
            )
        """
        result, _ = self._generate_base(
            prompt=prompt,
            model=model,
            response_format="text",
            images=images
        )
        return result
    
    def gen_dict(self, model: str, prompt: str, schema: str, images: Optional[List] = None, add_schema_to_prompt: bool = False) -> Dict[str, Any]:
        """
        Generate dictionary output using string schema.

        Args:
            model: Model identifier (e.g., "openrouter:google/gemini-2.0-flash-exp", "ollama:llama3.2")
            prompt: Input prompt for generation
            schema: JSON schema as string for structured output
            images: Optional list of images for vision models
            add_schema_to_prompt: If True, adds schema information to the prompt for better compliance

        Returns:
            Dictionary containing the structured output

        Raises:
            ValueError: If model format is invalid or provider is unsupported
            RuntimeError: If generation fails

        Example:
            result = client.gen_dict(
                model="openrouter:google/gemini-2.0-flash-exp",
                prompt="Extract info: John Doe, 30, from NYC",
                schema="{name, age:int, city}"
            )
            # Returns: {"name": "John Doe", "age": 30, "city": "NYC"}
        """
        # Enhance prompt with schema information if requested
        enhanced_prompt = prompt
        if add_schema_to_prompt:
            enhanced_prompt = f"{prompt}\n\nPlease generate output to exactly follow the following structure: {schema}"

        result, _ = self._generate_base(
            prompt=enhanced_prompt,
            model=model,
            response_format="dict",
            schema=schema,
            images=images
        )
        return result
    
    def gen_pydantic(self, model: str, prompt: str, response_model: Type[BaseModel], images: Optional[List] = None, add_schema_to_prompt: bool = False) -> BaseModel:
        """
        Generate structured output using Pydantic models.

        Args:
            model: Model identifier (e.g., "openrouter:google/gemini-2.0-flash-exp", "ollama:llama3.2")
            prompt: Input prompt for generation
            response_model: Pydantic model class for structured output
            images: Optional list of images for vision models
            add_schema_to_prompt: If True, adds schema information to the prompt for better compliance

        Returns:
            Instance of the provided Pydantic model

        Raises:
            ValueError: If model format is invalid or provider is unsupported
            RuntimeError: If generation fails

        Example:
            from pydantic import BaseModel

            class Person(BaseModel):
                name: str
                age: int
                city: str

            result = client.gen_pydantic(
                model="openrouter:google/gemini-2.0-flash-exp",
                prompt="Extract info: John Doe, 30, from NYC",
                response_model=Person
            )
            # Returns: Person(name="John Doe", age=30, city="NYC")
        """
        # Enhance prompt with schema information if requested
        enhanced_prompt = prompt
        if add_schema_to_prompt:
            try:
                # Convert Pydantic model to string schema using string-schema
                from string_schema import model_to_string
                schema_str = model_to_string(response_model)
                enhanced_prompt = f"{prompt}\n\nPlease generate output to exactly follow the following structure: {schema_str}"
            except ImportError:
                # Fallback to basic JSON schema description if string-schema not available
                schema_description = f"JSON object matching {response_model.__name__} model"
                enhanced_prompt = f"{prompt}\n\nPlease generate output as a {schema_description}"
            except Exception as e:
                # If conversion fails, log warning and continue without schema enhancement
                self.logger.warning(f"Failed to convert Pydantic model to string schema: {e}")

        result, _ = self._generate_base(
            prompt=enhanced_prompt,
            model=model,
            response_format="pydantic",
            response_model=response_model,
            images=images
        )
        return result
    

    
    def is_vision_capable(self, model: str) -> bool:
        """
        Check if a model supports vision/image inputs.
        
        Args:
            model: Model string with provider prefix
            
        Returns:
            True if model supports vision, False otherwise
        """
        try:
            provider_name, actual_model = self._detect_provider(model)
            
            # Define vision-capable models for each provider
            vision_models = {
                "openrouter": [
                    # Google models
                    "google/gemini-2.0-flash-exp",
                    "google/gemini-2.5-flash-lite",
                    "google/gemini-2.5-flash", 
                    "google/gemini-1.5-flash",
                    "google/gemini-1.5-pro",
                    "google/gemini-pro-vision",
                    "google/gemini-flash-1.5",
                    "google/gemini-pro-1.5",
                    # OpenAI models
                    "openai/gpt-4o",
                    "openai/gpt-4o-mini",
                    "openai/gpt-4-vision-preview",
                    "openai/gpt-4-turbo",
                    # Anthropic models
                    "anthropic/claude-3-5-sonnet",
                    "anthropic/claude-3-opus",
                    "anthropic/claude-3-sonnet",
                    "anthropic/claude-3-haiku",
                ],
                "ollama": [
                    # Vision-capable Ollama models
                    "llava:7b",
                    "llava:13b",
                    "llava:34b",
                    "llava-llama3:8b",
                    "llava-phi3:3.8b",
                    "moondream:1.8b",
                    "bakllava:7b",
                    "qwen2-vl:7b",
                    "qwen2-vl:2b",
                    # Note: qwen3:8b typically doesn't support vision
                ]
            }
            
            provider_vision_models = vision_models.get(provider_name, [])
            
            # Check exact match or partial match for model names
            for vision_model in provider_vision_models:
                if actual_model == vision_model or actual_model.startswith(vision_model.split(':')[0]):
                    return True
            
            return False
            
        except Exception:
            # If we can't determine, assume no vision support
            return False