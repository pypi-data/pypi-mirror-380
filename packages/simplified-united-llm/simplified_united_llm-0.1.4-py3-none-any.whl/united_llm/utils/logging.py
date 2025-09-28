#!/usr/bin/env python3
"""
Logging utilities for Simplified United LLM

Provides comprehensive logging with per-file organization.
"""

import logging
import sys
import os
import json
import random
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, Any
from pydantic import BaseModel


def setup_logging(log_dir: Path, log_level: str = "INFO") -> tuple[logging.Logger, Path]:
    """
    Setup logging for the LLM client with per-file logging.
    
    Args:
        log_dir: Directory to store log files
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    
    Returns:
        Tuple of (configured logger instance, txt_log_folder path)
    
    The logging creates individual files for each request with:
    - Directory structure: logs/llm_calls/txt/YYYY-MM-DD/
    - File naming: YYYYMMDD-HH:MM:SS_random(0-9)_model_name.txt
    """
    # Create log directory if it doesn't exist
    log_dir = Path(log_dir)
    log_dir.mkdir(parents=True, exist_ok=True)
    
    # Create txt log folder structure
    txt_log_folder = log_dir / "txt"
    txt_log_folder.mkdir(parents=True, exist_ok=True)
    
    # Create logger
    logger = logging.getLogger("united_llm")
    logger.setLevel(getattr(logging, log_level.upper()))
    
    # Clear existing handlers to avoid duplicates
    logger.handlers.clear()
    
    # Create console handler for errors and warnings
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.WARNING)
    
    # Create console formatter
    console_formatter = logging.Formatter(
        '%(asctime)s | %(levelname)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Set formatter
    console_handler.setFormatter(console_formatter)
    
    # Add handler to logger
    logger.addHandler(console_handler)
    
    # Prevent propagation to root logger
    logger.propagate = False
    
    return logger, txt_log_folder


def get_logger() -> Optional[logging.Logger]:
    """
    Get the existing united_llm logger if it exists.
    
    Returns:
        Logger instance or None if not configured
    """
    return logging.getLogger("united_llm") if logging.getLogger("united_llm").handlers else None


def log_llm_call(
    txt_log_folder: Path,
    model: str,
    prompt: Any,
    response: Any = None,
    duration_ms: Optional[float] = None,
    token_usage: Optional[Dict[str, Any]] = None,
    cost_info: Optional[Dict[str, Any]] = None,
    error_info: Optional[str] = None,
    is_before_call: bool = False,
    txt_filepath: Optional[str] = None
) -> tuple[Optional[str], Optional[str]]:
    """
    Log LLM call to individual text file with specific naming convention.
    
    Args:
        txt_log_folder: Base directory for txt logs
        model: Model name used for the call
        prompt: The prompt/messages sent to the model
        response: The response from the model
        duration_ms: Duration of the call in milliseconds
        token_usage: Token usage information (prompt_tokens, completion_tokens, total_tokens)
        cost_info: Cost information from provider (cost, cost_details, etc.)
        error_info: Error information if any
        is_before_call: Whether this is logged before the call (for streaming)
        txt_filepath: Optional specific filepath to use
    
    Returns:
        Tuple of (txt_log_path, json_log_path) - json_log_path is always None
    
    File naming convention: YYYYMMDD-HH:MM:SS_random(0-9)_model_name.txt
    Directory structure: txt_log_folder/YYYY-MM-DD/
    """
    if not txt_log_folder:
        return None, None

    try:
        now = datetime.now()
        date_folder = now.strftime("%Y-%m-%d")
        # New format: YYYYMMDD-HH:MM:SS_random(0-9)_model_name
        timestamp = now.strftime("%Y%m%d-%H:%M:%S")
        random_digit = str(random.randint(0, 9))
        current_txt_log_dir = os.path.join(txt_log_folder, date_folder)
        os.makedirs(current_txt_log_dir, exist_ok=True)
        base_filename = f"{timestamp}_{random_digit}_{model.replace(':', '_').replace('/', '_')}"

        # Initialize log paths
        final_txt_log_path = txt_filepath or os.path.join(current_txt_log_dir, f"{base_filename}.txt")

        log_entry = f"Timestamp: {now.isoformat()}\nModel: {model}\n"
        if duration_ms:
            log_entry += f"Duration: {duration_ms}ms\n"
        log_entry += (
            f"Prompt/Messages:\n{json.dumps(prompt, indent=2, ensure_ascii=False) if isinstance(prompt, (dict, list)) else prompt}\n\n"
        )

        if is_before_call:
            log_entry += "--- Waiting for response ---\n"
        else:
            response_data = (
                response.model_dump() if isinstance(response, BaseModel) else response
                if response is not None
                else "N/A"
            )
            log_entry += f"Response:\n{json.dumps(response_data, indent=2, default=str, ensure_ascii=False)}\n\n"
            
            # Enhanced token and cost logging
            if token_usage:
                log_entry += "Token Usage:\n"
                log_entry += f"  Prompt tokens: {token_usage.get('prompt_tokens', 'N/A')}\n"
                log_entry += f"  Completion tokens: {token_usage.get('completion_tokens', 'N/A')}\n"
                log_entry += f"  Total tokens: {token_usage.get('total_tokens', 'N/A')}\n"
                
                # Additional token details if available
                if 'prompt_tokens_details' in token_usage and token_usage['prompt_tokens_details']:
                    details = token_usage['prompt_tokens_details']
                    # Handle both dict and object access patterns
                    if isinstance(details, dict):
                        log_entry += f"  Cached tokens: {details.get('cached_tokens', 'N/A')}\n"
                        log_entry += f"  Audio tokens: {details.get('audio_tokens', 'N/A')}\n"
                    else:
                        log_entry += f"  Cached tokens: {getattr(details, 'cached_tokens', 'N/A')}\n"
                        log_entry += f"  Audio tokens: {getattr(details, 'audio_tokens', 'N/A')}\n"
                
                if 'completion_tokens_details' in token_usage and token_usage['completion_tokens_details']:
                    details = token_usage['completion_tokens_details']
                    # Handle both dict and object access patterns
                    if isinstance(details, dict):
                        log_entry += f"  Reasoning tokens: {details.get('reasoning_tokens', 'N/A')}\n"
                        log_entry += f"  Image tokens: {details.get('image_tokens', 'N/A')}\n"
                    else:
                        log_entry += f"  Reasoning tokens: {getattr(details, 'reasoning_tokens', 'N/A')}\n"
                        log_entry += f"  Image tokens: {getattr(details, 'image_tokens', 'N/A')}\n"
            
            # Cost information logging
            if cost_info:
                log_entry += "Cost Information:\n"
                
                # Format cost with both credits and dollar notation
                total_cost = cost_info.get('cost', 'N/A')
                if total_cost != 'N/A' and total_cost is not None:
                    log_entry += f"  Total cost: {total_cost} credits (${total_cost:.6f})\n"
                else:
                    log_entry += f"  Total cost: {total_cost} credits\n"
                
                # Detailed cost breakdown if available
                if 'cost_details' in cost_info:
                    details = cost_info['cost_details']
                    
                    # Format upstream inference cost
                    upstream_cost = details.get('upstream_inference_cost', 'N/A')
                    if upstream_cost != 'N/A' and upstream_cost is not None:
                        log_entry += f"  Upstream inference cost: {upstream_cost} credits (${upstream_cost:.6f})\n"
                    else:
                        log_entry += f"  Upstream inference cost: {upstream_cost}\n"
                    
                    # Format upstream prompt cost
                    prompt_cost = details.get('upstream_inference_prompt_cost', 'N/A')
                    if prompt_cost != 'N/A' and prompt_cost is not None:
                        log_entry += f"  Upstream prompt cost: {prompt_cost} credits (${prompt_cost:.6f})\n"
                    else:
                        log_entry += f"  Upstream prompt cost: {prompt_cost}\n"
                    
                    # Format upstream completion cost
                    completion_cost = details.get('upstream_inference_completions_cost', 'N/A')
                    if completion_cost != 'N/A' and completion_cost is not None:
                        log_entry += f"  Upstream completion cost: {completion_cost} credits (${completion_cost:.6f})\n"
                    else:
                        log_entry += f"  Upstream completion cost: {completion_cost}\n"
                
                # Additional cost metadata
                if 'is_byok' in cost_info:
                    log_entry += f"  BYOK (Bring Your Own Key): {cost_info.get('is_byok', 'N/A')}\n"
            
            if error_info:
                log_entry += f"Error: {error_info}\n"

        # Write to txt file
        # Use "w" mode for final log (with response) to avoid duplicates, "a" for before_call
        write_mode = "w" if not is_before_call else "a"
        with open(final_txt_log_path, write_mode, encoding="utf-8") as f:
            f.write(log_entry + "------------------------------------\n")

        return final_txt_log_path, None  # JSON logging disabled

    except Exception as e:
        logger = get_logger()
        if logger:
            logger.error(f"Failed to write txt logs: {e}")
        return None, None