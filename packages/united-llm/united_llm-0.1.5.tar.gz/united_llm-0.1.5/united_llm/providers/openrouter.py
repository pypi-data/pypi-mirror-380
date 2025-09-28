#!/usr/bin/env python3
"""
OpenRouter Provider for Simplified United LLM

Handles communication with OpenRouter API for LLM generation.
"""

from typing import Any, Optional, Type, Dict, Tuple, List
import json
from openai import OpenAI
from pydantic import BaseModel
import instructor
import base64
import io
from PIL import Image


class OpenRouterProvider:
    """
    Provider for OpenRouter API integration.
    
    Uses OpenAI-compatible client to communicate with OpenRouter's API.
    """
    
    def __init__(self, api_key: Optional[str], base_url: str = "https://openrouter.ai/api/v1"):
        """
        Initialize OpenRouter provider.
        
        Args:
            api_key: OpenRouter API key (required)
            base_url: OpenRouter API base URL
        
        Raises:
            ValueError: If API key is not provided
        """
        if not api_key:
            raise ValueError("OpenRouter API key is required")
        
        self.api_key = api_key
        self.base_url = base_url
        
        # Initialize OpenAI client with OpenRouter configuration
        openai_client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )
        
        # Patch with Instructor for structured outputs
        self.client = instructor.from_openai(openai_client)

        # Keep reference to direct client for text generation
        self.direct_client = openai_client

    def generate_text(self, prompt: str, model: str) -> str:
        """
        Generate plain text response using OpenRouter API.

        Args:
            prompt: Input prompt for generation
            model: Model name (without provider prefix)

        Returns:
            Plain text response

        Raises:
            RuntimeError: If API call fails
        """
        try:
            # Use direct client for plain text generation
            response = self.direct_client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=2000
            )

            content = response.choices[0].message.content
            if not content:
                raise RuntimeError("Empty response from OpenRouter API")

            return content.strip()

        except Exception as e:
            if isinstance(e, RuntimeError):
                raise
            raise RuntimeError(f"OpenRouter text generation failed: {str(e)}") from e

    def generate(self, prompt: str, model: str, response_model: Type[BaseModel]) -> BaseModel:
        """
        Generate structured response using OpenRouter API.
        
        Args:
            prompt: Input prompt for generation
            model: Model name (without provider prefix)
            response_model: Pydantic model for structured output
        
        Returns:
            Instance of response_model with generated data
        
        Raises:
            RuntimeError: If API call fails
        """
        result, _ = self.generate_with_metadata(prompt, model, response_model)
        return result
    
    def generate_with_metadata(self, prompt: str, model: str, response_model: Type[BaseModel]) -> Tuple[BaseModel, Optional[Dict[str, Any]]]:
        """
        Generate structured response using OpenRouter API with usage metadata.
        
        Args:
            prompt: Input prompt for generation
            model: Model name (without provider prefix)
            response_model: Pydantic model for structured output
        
        Returns:
            Tuple of (response_model instance, usage_metadata dict or None)
        
        Raises:
            RuntimeError: If API call fails
        """
        try:
            # First make a direct API call to get full metadata including cost information
            # Create a temporary non-Instructor client for metadata extraction
            direct_client = OpenAI(
                api_key=self.api_key,
                base_url=self.base_url
            )
            
            # Make direct API call to preserve cost metadata
            direct_response = direct_client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,
                max_tokens=2000,
                extra_body={"usage": {"include": True}}
            )
            
            # Extract usage metadata from direct response (includes cost info)
            usage_metadata = None
            if hasattr(direct_response, 'usage') and direct_response.usage:
                usage_metadata = {
                    'prompt_tokens': getattr(direct_response.usage, 'prompt_tokens', 0),
                    'completion_tokens': getattr(direct_response.usage, 'completion_tokens', 0),
                    'total_tokens': getattr(direct_response.usage, 'total_tokens', 0),
                    'prompt_tokens_details': getattr(direct_response.usage, 'prompt_tokens_details', None),
                    'completion_tokens_details': getattr(direct_response.usage, 'completion_tokens_details', None)
                }
                
                # Extract cost information if available (OpenRouter specific)
                if hasattr(direct_response.usage, 'cost'):
                    usage_metadata['total_cost'] = direct_response.usage.cost
                
                # Extract detailed cost information
                if hasattr(direct_response.usage, 'cost_details'):
                    cost_details = direct_response.usage.cost_details
                    if cost_details:
                        # Handle both dict and object access patterns
                        if isinstance(cost_details, dict):
                            usage_metadata['upstream_inference_cost'] = cost_details.get('upstream_inference_cost')
                            usage_metadata['upstream_inference_prompt_cost'] = cost_details.get('upstream_inference_prompt_cost')
                            usage_metadata['upstream_inference_completions_cost'] = cost_details.get('upstream_inference_completions_cost')
                        else:
                            usage_metadata['upstream_inference_cost'] = getattr(cost_details, 'upstream_inference_cost', None)
                            usage_metadata['upstream_inference_prompt_cost'] = getattr(cost_details, 'upstream_inference_prompt_cost', None)
                            usage_metadata['upstream_inference_completions_cost'] = getattr(cost_details, 'upstream_inference_completions_cost', None)
            
            # Now use Instructor to get structured output from the same response content
            content = direct_response.choices[0].message.content
            if not content:
                raise RuntimeError("Empty response from OpenRouter API")
            
            # Parse the response content using Instructor for structured output
            # Use a simple completion to parse the existing content
            result = self.client.chat.completions.create(
                model=model,
                response_model=response_model,
                messages=[
                    {"role": "user", "content": f"Parse this response into the required format: {content}"}
                ],
                temperature=0.0,  # Very low temperature for parsing
                max_tokens=500
            )
            
            return result, usage_metadata
            
        except Exception as e:
            if isinstance(e, RuntimeError):
                raise
            raise RuntimeError(f"OpenRouter API call failed: {str(e)}") from e
    
    def _prepare_image_content(self, images) -> List[Dict[str, Any]]:
        """
        Convert ImageInput objects to OpenAI-compatible image content format.
        
        Args:
            images: List of ImageInput objects or single ImageInput object
            
        Returns:
            List of dicts with image content for OpenAI API
        """
        try:
            # Handle single image input
            if not isinstance(images, list):
                images = [images]
            
            content = []
            for image_input in images:
                # Get base64 data from ImageInput
                base64_data = image_input.to_base64()
                mime_type = image_input.get_mime_type()
                
                content.append({
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:{mime_type};base64,{base64_data}"
                    }
                })
            
            return content
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
        Generate structured response with vision support using OpenRouter API.
        
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
            RuntimeError: If API call fails
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
        Generate structured response with vision support and metadata using OpenRouter API.
        
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
            RuntimeError: If API call fails
        """
        try:
            # Prepare message content with images
            content = [{"type": "text", "text": prompt}]
            
            # Add images to content
            image_contents = self._prepare_image_content(images)
            content.extend(image_contents)
            
            # First make a direct API call to get full metadata including cost information
            direct_client = OpenAI(
                api_key=self.api_key,
                base_url=self.base_url
            )
            
            # Make direct API call with vision content
            direct_response = direct_client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": content}
                ],
                temperature=temperature,
                max_tokens=2000
            )
            
            # Extract usage metadata
            usage_metadata = None
            if hasattr(direct_response, 'usage') and direct_response.usage:
                usage_metadata = {
                    'prompt_tokens': getattr(direct_response.usage, 'prompt_tokens', 0),
                    'completion_tokens': getattr(direct_response.usage, 'completion_tokens', 0),
                    'total_tokens': getattr(direct_response.usage, 'total_tokens', 0),
                    'prompt_tokens_details': getattr(direct_response.usage, 'prompt_tokens_details', None),
                    'completion_tokens_details': getattr(direct_response.usage, 'completion_tokens_details', None)
                }
                
                # Extract cost information if available (OpenRouter specific)
                if hasattr(direct_response.usage, 'cost'):
                    usage_metadata['total_cost'] = direct_response.usage.cost
                
                # Extract detailed cost information
                if hasattr(direct_response.usage, 'cost_details'):
                    cost_details = direct_response.usage.cost_details
                    if cost_details:
                        if isinstance(cost_details, dict):
                            usage_metadata['upstream_inference_cost'] = cost_details.get('upstream_inference_cost')
                            usage_metadata['upstream_inference_prompt_cost'] = cost_details.get('upstream_inference_prompt_cost')
                            usage_metadata['upstream_inference_completions_cost'] = cost_details.get('upstream_inference_completions_cost')
                        else:
                            usage_metadata['upstream_inference_cost'] = getattr(cost_details, 'upstream_inference_cost', None)
                            usage_metadata['upstream_inference_prompt_cost'] = getattr(cost_details, 'upstream_inference_prompt_cost', None)
                            usage_metadata['upstream_inference_completions_cost'] = getattr(cost_details, 'upstream_inference_completions_cost', None)
            
            # Get response content
            content_text = direct_response.choices[0].message.content
            if not content_text:
                raise RuntimeError("Empty response from OpenRouter API")
            
            # Parse the response content using Instructor for structured output
            result = self.client.chat.completions.create(
                model=model,
                response_model=response_model,
                messages=[
                    {"role": "user", "content": f"Parse this response into the required format: {content_text}"}
                ],
                temperature=0.0,
                max_tokens=500
            )
            
            return result, usage_metadata
            
        except Exception as e:
            if isinstance(e, RuntimeError):
                raise
            raise RuntimeError(f"OpenRouter vision API call failed: {str(e)}") from e