#!/usr/bin/env python3
"""
Ollama Provider for Simplified United LLM

Handles communication with local Ollama server for LLM generation.
"""

from typing import Any, Type, List, Optional, Dict, Tuple
import json
import requests
from pydantic import BaseModel
import base64
import io


class OllamaProvider:
    """
    Provider for local Ollama server integration.
    
    Communicates with Ollama's OpenAI-compatible API endpoint.
    """
    
    def __init__(self, base_url: str = "http://localhost:11434/v1"):
        """
        Initialize Ollama provider.
        
        Args:
            base_url: Ollama API base URL (default: http://localhost:11434/v1)
        """
        self.base_url = base_url.rstrip('/')
        self.chat_url = f"{self.base_url}/chat/completions"
    
    def _check_connection(self) -> bool:
        """
        Check if Ollama server is accessible.
        
        Returns:
            True if server is accessible, False otherwise
        """
        try:
            response = requests.get(f"{self.base_url.replace('/v1', '')}/api/tags", timeout=5)
            return response.status_code == 200
        except requests.RequestException:
            return False
    
    def generate_text(self, prompt: str, model: str) -> str:
        """
        Generate plain text response using Ollama API.

        Args:
            prompt: Input prompt for generation
            model: Model name (without provider prefix)

        Returns:
            Plain text response

        Raises:
            RuntimeError: If API call fails or server is not accessible
        """
        # Check if Ollama server is accessible
        if not self._check_connection():
            raise RuntimeError(
                f"Cannot connect to Ollama server at {self.base_url}. "
                "Please ensure Ollama is running and accessible."
            )

        try:
            # Prepare request payload for plain text generation
            payload = {
                "model": model,
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "temperature": 0.7,  # Higher temperature for creative text
                "max_tokens": 2000,
                "stream": False
            }

            # Make API call
            response = requests.post(
                self.chat_url,
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=60  # Longer timeout for local generation
            )

            if response.status_code != 200:
                raise RuntimeError(
                    f"Ollama API returned status {response.status_code}: {response.text}"
                )

            # Parse response
            response_data = response.json()

            if "choices" not in response_data or not response_data["choices"]:
                raise RuntimeError("Invalid response format from Ollama API")

            content = response_data["choices"][0]["message"]["content"]
            if not content:
                raise RuntimeError("Empty response from Ollama API")

            return content.strip()

        except requests.RequestException as e:
            raise RuntimeError(f"Ollama API request failed: {str(e)}") from e
        except Exception as e:
            if isinstance(e, RuntimeError):
                raise
            raise RuntimeError(f"Ollama text generation failed: {str(e)}") from e

    def generate(self, prompt: str, model: str, response_model: Type[BaseModel]) -> BaseModel:
        """
        Generate structured response using Ollama API.
        
        Args:
            prompt: Input prompt for generation
            model: Model name (without provider prefix)
            response_model: Pydantic model for structured output
        
        Returns:
            Instance of response_model with generated data
        
        Raises:
            RuntimeError: If API call fails or server is not accessible
        """
        # Check if Ollama server is accessible
        if not self._check_connection():
            raise RuntimeError(
                f"Cannot connect to Ollama server at {self.base_url}. "
                "Please ensure Ollama is running and accessible."
            )
        
        try:
            # Get JSON schema from Pydantic model
            schema = response_model.model_json_schema()
            
            # Create system message with schema instructions
            system_message = (
                "You are a helpful assistant that extracts structured data. "
                "Respond with valid JSON that matches the provided schema exactly. "
                "Do not include any additional text or formatting."
            )
            
            # Add schema information to the prompt
            enhanced_prompt = (
                f"{prompt}\n\n"
                f"Please respond with JSON that matches this schema:\n"
                f"{json.dumps(schema, indent=2)}"
            )
            
            # Prepare request payload
            payload = {
                "model": model,
                "messages": [
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": enhanced_prompt}
                ],
                "temperature": 0.1,  # Low temperature for consistent structured output
                "max_tokens": 2000,
                "stream": False
            }
            
            # Make API call
            response = requests.post(
                self.chat_url,
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=60  # Longer timeout for local generation
            )
            
            if response.status_code != 200:
                raise RuntimeError(
                    f"Ollama API returned status {response.status_code}: {response.text}"
                )
            
            # Parse response
            response_data = response.json()
            
            if "choices" not in response_data or not response_data["choices"]:
                raise RuntimeError("Invalid response format from Ollama API")
            
            content = response_data["choices"][0]["message"]["content"]
            if not content:
                raise RuntimeError("Empty response from Ollama API")
            
            # Parse JSON response
            try:
                json_data = json.loads(content.strip())
            except json.JSONDecodeError as e:
                # Try to extract JSON from response if it contains extra text
                import re
                # Look for JSON objects in the content
                json_matches = re.findall(r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}', content, re.DOTALL)
                if json_matches:
                    # Try each match until we find valid JSON
                    for match in json_matches:
                        try:
                            json_data = json.loads(match)
                            break
                        except json.JSONDecodeError:
                            continue
                    else:
                        raise RuntimeError(f"No valid JSON found in response: {content}") from e
                else:
                    raise RuntimeError(f"Invalid JSON response: {content}") from e

            # Handle complex JSON structure that Ollama sometimes returns
            json_data = self._extract_values_from_complex_json(json_data)

            # Validate and create Pydantic model instance
            return response_model(**json_data)
            
        except requests.RequestException as e:
            raise RuntimeError(f"Ollama API request failed: {str(e)}") from e
        except Exception as e:
            if isinstance(e, RuntimeError):
                raise
            raise RuntimeError(f"Ollama generation failed: {str(e)}") from e
    
    def generate_with_metadata(self, prompt: str, model: str, response_model: Type[BaseModel]) -> Tuple[BaseModel, Optional[Dict[str, Any]]]:
        """
        Generate structured response using Ollama API with usage metadata.
        
        Args:
            prompt: Input prompt for generation
            model: Model name (without provider prefix)
            response_model: Pydantic model for structured output
        
        Returns:
            Tuple of (response_model instance, usage_metadata dict or None)
        
        Raises:
            RuntimeError: If API call fails or server is not accessible
        """
        # Check if Ollama server is accessible
        if not self._check_connection():
            raise RuntimeError(
                f"Cannot connect to Ollama server at {self.base_url}. "
                "Please ensure Ollama is running and accessible."
            )
        
        try:
            # Get JSON schema from Pydantic model
            schema = response_model.model_json_schema()
            
            # Create system message with schema instructions
            system_message = (
                "You are a helpful assistant that extracts structured data. "
                "Respond with valid JSON that matches the provided schema exactly. "
                "Do not include any additional text or formatting."
            )
            
            # Add schema information to the prompt
            enhanced_prompt = (
                f"{prompt}\n\n"
                f"Please respond with JSON that matches this schema:\n"
                f"{json.dumps(schema, indent=2)}"
            )
            
            # Prepare request payload
            payload = {
                "model": model,
                "messages": [
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": enhanced_prompt}
                ],
                "temperature": 0.1,  # Low temperature for consistent structured output
                "max_tokens": 2000,
                "stream": False
            }
            
            # Make API call
            response = requests.post(
                self.chat_url,
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=60  # Longer timeout for local generation
            )
            
            if response.status_code != 200:
                raise RuntimeError(
                    f"Ollama API returned status {response.status_code}: {response.text}"
                )
            
            # Parse response
            response_data = response.json()
            
            # Extract usage metadata if available
            usage_metadata = None
            if 'usage' in response_data:
                usage = response_data['usage']
                usage_metadata = {
                    'prompt_tokens': usage.get('prompt_tokens', 0),
                    'completion_tokens': usage.get('completion_tokens', 0),
                    'total_tokens': usage.get('total_tokens', 0)
                }
                
                # Add Ollama-specific metrics if available
                if 'eval_count' in usage:
                    usage_metadata['eval_count'] = usage['eval_count']
                if 'prompt_eval_count' in usage:
                    usage_metadata['prompt_eval_count'] = usage['prompt_eval_count']
                if 'eval_duration' in usage:
                    usage_metadata['eval_duration'] = usage['eval_duration']
                if 'prompt_eval_duration' in usage:
                    usage_metadata['prompt_eval_duration'] = usage['prompt_eval_duration']
            
            if "choices" not in response_data or not response_data["choices"]:
                raise RuntimeError("Invalid response format from Ollama API")
            
            content = response_data["choices"][0]["message"]["content"]
            if not content:
                raise RuntimeError("Empty response from Ollama API")
            
            # Parse JSON response
            try:
                json_data = json.loads(content.strip())
            except json.JSONDecodeError as e:
                # Try to extract JSON from response if it contains extra text
                import re
                # Look for JSON objects in the content
                json_matches = re.findall(r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}', content, re.DOTALL)
                if json_matches:
                    # Try each match until we find valid JSON
                    for match in json_matches:
                        try:
                            json_data = json.loads(match)
                            break
                        except json.JSONDecodeError:
                            continue
                    else:
                        raise RuntimeError(f"No valid JSON found in response: {content}") from e
                else:
                    raise RuntimeError(f"Invalid JSON response: {content}") from e
            
            # Validate and create Pydantic model instance
            result = response_model(**json_data)
            
            return result, usage_metadata
            
        except requests.RequestException as e:
            raise RuntimeError(f"Ollama API request failed: {str(e)}") from e
        except Exception as e:
            if isinstance(e, RuntimeError):
                raise
            raise RuntimeError(f"Ollama generation with metadata failed: {str(e)}") from e
    
    def _prepare_image_content(self, images) -> List[str]:
        """
        Convert ImageInput objects to base64 strings for Ollama API.
        
        Args:
            images: List of ImageInput objects or single ImageInput object
            
        Returns:
            List of base64 encoded image strings
        """
        try:
            # Handle single image input
            if not isinstance(images, list):
                images = [images]
            
            base64_images = []
            for image_input in images:
                base64_data = image_input.to_base64()
                base64_images.append(base64_data)
            
            return base64_images
        except Exception as e:
            raise RuntimeError(f"Failed to prepare image content: {str(e)}") from e
    
    def generate_with_vision(
        self, 
        prompt: str, 
        model: str, 
        response_model: Type[BaseModel],
        images: List,
        temperature: float = 0.0,
        max_retries: int = 1
    ) -> BaseModel:
        """
        Generate structured response with vision support using Ollama API.
        
        Args:
            prompt: Input prompt for generation
            model: Model name (without provider prefix)
            response_model: Pydantic model for structured output
            images: List of ImageInput objects
            temperature: Sampling temperature
            max_retries: Maximum number of retries
        
        Returns:
            Instance of response_model with generated data
        
        Raises:
            RuntimeError: If API call fails or server is not accessible
        """
        result, _ = self.generate_with_vision_metadata(
            prompt, model, response_model, images, temperature, max_retries
        )
        return result
    
    def generate_with_vision_metadata(
        self, 
        prompt: str, 
        model: str, 
        response_model: Type[BaseModel],
        images: List,
        temperature: float = 0.0,
        max_retries: int = 1
    ) -> Tuple[BaseModel, Optional[Dict[str, Any]]]:
        """
        Generate structured response with vision support and metadata using Ollama API.
        
        Args:
            prompt: Input prompt for generation
            model: Model name (without provider prefix)
            response_model: Pydantic model for structured output
            images: List of ImageInput objects
            temperature: Sampling temperature
            max_retries: Maximum number of retries
        
        Returns:
            Tuple of (response_model instance, usage_metadata dict or None)
        
        Raises:
            RuntimeError: If API call fails or server is not accessible
        """
        # Check if Ollama server is accessible
        if not self._check_connection():
            raise RuntimeError(
                f"Cannot connect to Ollama server at {self.base_url}. "
                "Please ensure Ollama is running and accessible."
            )
        
        try:
            # Get JSON schema from Pydantic model
            schema = response_model.model_json_schema()
            
            # Create system message with schema instructions
            system_message = (
                "You are a helpful assistant that extracts structured data from images and text. "
                "Respond with valid JSON that matches the provided schema exactly. "
                "Do not include any additional text or formatting."
            )
            
            # Enhanced prompt with schema
            enhanced_prompt = (
                f"{prompt}\n\n"
                f"Please respond with valid JSON matching this schema:\n"
                f"{json.dumps(schema, indent=2)}"
            )
            
            # Prepare images for Ollama API
            image_data = self._prepare_image_content(images)
            
            # Prepare request payload with images
            payload = {
                "model": model,
                "messages": [
                    {"role": "system", "content": system_message},
                    {
                        "role": "user", 
                        "content": enhanced_prompt,
                        "images": image_data  # Ollama expects images as base64 strings in array
                    }
                ],
                "temperature": max(0.1, temperature),  # Ollama needs minimum temperature
                "max_tokens": 2000,
                "stream": False
            }
            
            # Make API call
            response = requests.post(
                self.chat_url,
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=120  # Longer timeout for vision processing
            )
            
            if response.status_code != 200:
                raise RuntimeError(f"Ollama API error: {response.status_code} - {response.text}")
            
            response_data = response.json()
            
            # Extract usage metadata if available
            usage_metadata = None
            if 'usage' in response_data:
                usage = response_data['usage']
                usage_metadata = {
                    'prompt_tokens': usage.get('prompt_tokens', 0),
                    'completion_tokens': usage.get('completion_tokens', 0),
                    'total_tokens': usage.get('total_tokens', 0),
                    'eval_count': usage.get('eval_count', 0),
                    'prompt_eval_count': usage.get('prompt_eval_count', 0),
                    'eval_duration': usage.get('eval_duration', 0),
                    'prompt_eval_duration': usage.get('prompt_eval_duration', 0)
                }
            
            # Extract content from response
            if 'choices' not in response_data or not response_data['choices']:
                raise RuntimeError("No choices in Ollama response")
            
            content = response_data['choices'][0]['message']['content']
            if not content:
                raise RuntimeError("Empty content in Ollama response")
            
            # Parse JSON response
            try:
                json_data = json.loads(content.strip())
            except json.JSONDecodeError as e:
                # Try to extract JSON from response if it contains extra text
                import re
                json_match = re.search(r'\{.*\}', content, re.DOTALL)
                if json_match:
                    json_data = json.loads(json_match.group())
                else:
                    raise RuntimeError(f"Invalid JSON response: {content}") from e
            
            # Validate and create Pydantic model instance
            result = response_model(**json_data)
            return result, usage_metadata
            
        except requests.RequestException as e:
            raise RuntimeError(f"Ollama vision API request failed: {str(e)}") from e
        except Exception as e:
            if isinstance(e, RuntimeError):
                raise
            raise RuntimeError(f"Ollama vision generation failed: {str(e)}") from e