#!/usr/bin/env python3
"""
Schema parsing utilities for Simplified United LLM

Integrates with string-schema package for Pydantic model generation.
"""

from typing import Type, Any
from pydantic import BaseModel

try:
    from string_schema import string_to_model
except ImportError:
    raise ImportError(
        "string-schema package is required. Install it with: pip install string-schema"
    )


class SchemaParser:
    """
    Parser for converting string schemas to Pydantic models.
    
    Uses the string-schema package to convert simple string definitions
    into Pydantic models for structured LLM output validation.
    """
    
    def __init__(self):
        """
        Initialize the schema parser.
        """
        self._model_cache = {}
    
    def parse_schema(self, schema: str) -> Type[BaseModel]:
        """
        Parse a string schema into a Pydantic model.
        
        Args:
            schema: String schema definition (e.g., "{name, age:int, city}")
        
        Returns:
            Pydantic model class for the schema
        
        Raises:
            ValueError: If schema is invalid
            RuntimeError: If string-schema parsing fails
        
        Examples:
            # Simple object schema
            model = parser.parse_schema("{name, age:int, city}")
            
            # Array schema
            model = parser.parse_schema("[{name, score:float}]")
            
            # Nested schema
            model = parser.parse_schema("{user: {name, email}, posts: [{title, content}]}")
        """
        if not schema or not isinstance(schema, str):
            raise ValueError("Schema must be a non-empty string")
        
        # Check cache first
        if schema in self._model_cache:
            return self._model_cache[schema]
        
        try:
            # Use string-schema to convert to Pydantic model
            model_class = string_to_model(schema)
            
            # Cache the model for reuse
            self._model_cache[schema] = model_class
            
            return model_class
            
        except Exception as e:
            raise RuntimeError(f"Failed to parse schema '{schema}': {str(e)}") from e
    
    def validate_schema(self, schema: str) -> bool:
        """
        Validate if a string schema is parseable.
        
        Args:
            schema: String schema definition
        
        Returns:
            True if schema is valid, False otherwise
        """
        try:
            self.parse_schema(schema)
            return True
        except (ValueError, RuntimeError):
            return False
    
    def clear_cache(self) -> None:
        """
        Clear the model cache.
        
        Useful for memory management in long-running applications.
        """
        self._model_cache.clear()
    
    def get_cache_size(self) -> int:
        """
        Get the number of cached models.
        
        Returns:
            Number of models in cache
        """
        return len(self._model_cache)