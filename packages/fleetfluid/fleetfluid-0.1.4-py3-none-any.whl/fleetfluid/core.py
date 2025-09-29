"""
Core FleetFluid implementation with dual-mode support:
- Open Source Mode: Uses PydanticAI agents directly
- Cloud Mode: Uses cloud computation for enterprise-grade performance and reliability
"""

import asyncio
import os
from typing import Any, Dict, List, Optional, Union

from .modes.factory import ModeFactory
from .models import SingleLabelResult, MultipleLabelResult


class FleetFluid:
    """Main FleetFluid class with dual-mode support for open source and cloud."""
    
    def __init__(self, 
                 model: str = "openai:gpt-4",
                 api_key: Optional[str] = None,
                 api_endpoint: Optional[str] = None,
                 **kwargs):
        """
        Initialize FleetFluid with dual-mode support.
        
        Args:
            model: Model identifier for PydanticAI (open source mode only)
            api_key: API key for cloud mode
            api_endpoint: API endpoint for cloud mode
            **kwargs: Additional configuration for PydanticAI agents (open source mode only)
        """
        # Detect mode and configure accordingly
        self.mode = self._detect_mode(api_key)
        
        if self.mode == "cloud":
            self._configure_cloud_mode(api_key, api_endpoint)
        else:
            self._configure_open_source_mode(model, kwargs)
    
    def _detect_mode(self, api_key: Optional[str] = None) -> str:
        """Detect execution mode based on available configuration."""
        # Explicit API key takes precedence
        if api_key:
            return "cloud"
        
        # Check environment variable
        if os.getenv("FLEETFLUID-API-KEY"):
            return "cloud"
        
        # Default to open source mode
        return "open_source"
    
    def _configure_cloud_mode(self, api_key: Optional[str], api_endpoint: Optional[str]):
        """Configure for cloud mode."""
        self.api_key = api_key or os.getenv("FLEETFLUID-API-KEY")
        self.api_endpoint = api_endpoint or os.getenv("FLEETFLUID_API_ENDPOINT", "https://api.fleetfluid.io")
        
        if not self.api_key:
            raise ValueError("API key required for cloud mode. Set FLEETFLUID-API-KEY environment variable or pass api_key parameter.")
        
        # Initialize cloud operation handlers using factory
        operations = ModeFactory.create_cloud_operations(self.api_key, self.api_endpoint)
        self._label_operation = operations['label_operation']
        self._ai_operation = operations['ai_operation']
        self._extract_operation = operations['extract_operation']
        self._anonymize_operation = operations['anonymize_operation']
        self._describe_operation = operations['describe_operation']
        
        # Clear open source mode attributes
        self.model = None
        self.agent_config = {}
    
    def _configure_open_source_mode(self, model: str, kwargs: Dict[str, Any]):
        """Configure for open source mode."""
        self.model = model
        self.agent_config = kwargs
        
        # Initialize open source operation handlers using factory
        operations = ModeFactory.create_open_source_operations(model, **kwargs)
        self._label_operation = operations['label_operation']
        self._ai_operation = operations['ai_operation']
        self._extract_operation = operations['extract_operation']
        self._anonymize_operation = operations['anonymize_operation']
        self._describe_operation = operations['describe_operation']
        
        # Clear cloud mode attributes
        self.api_key = None
        self.api_endpoint = None
    
    def switch_to_cloud_mode(self, api_key: str, api_endpoint: str):
        """Switch to cloud mode at runtime."""
        self._configure_cloud_mode(api_key, api_endpoint)
    
    def switch_to_open_source_mode(self, model: str = "openai:gpt-4", **kwargs):
        """Switch to open source mode at runtime."""
        self._configure_open_source_mode(model, kwargs)
    
    @property
    def is_cloud_mode(self) -> bool:
        """Check if currently in cloud mode."""
        return self.mode == "cloud"
    
    @property
    def is_open_source_mode(self) -> bool:
        """Check if currently in open source mode."""
        return self.mode == "open_source"
    
    def label(self, text: str, labels: List[str], multiple: bool = False) -> Union[SingleLabelResult, MultipleLabelResult]:
        """
        Label text using the appropriate backend (open source or cloud).
        
        Args:
            text: Input text to label
            labels: List of possible labels to choose from
            multiple: If True, select multiple labels; if False, select single best label
            
        Returns:
            Structured result with selected label(s) and confidence scores
        """
        return asyncio.run(self._label_async(text, labels, multiple))
    
    async def _label_async(self, text: str, labels: List[str], multiple: bool = False) -> Union[SingleLabelResult, MultipleLabelResult]:
        """Async implementation of labeling."""
        if multiple:
            return await self._label_operation.label_multiple(text, labels)
        else:
            return await self._label_operation.label_single(text, labels)
    
    def ai(self, prompt: str, data: str) -> str:
        """
        Apply AI transformation to data using the appropriate backend.
        
        Args:
            prompt: Instruction for the AI
            data: Input data to transform
            
        Returns:
            Transformed data as string
        """
        return asyncio.run(self._ai_async(prompt, data))
    
    async def _ai_async(self, prompt: str, data: str) -> str:
        """Async implementation of AI transformation."""
        return await self._ai_operation.ai(prompt, data)
    
    def extract(self, extraction_type: str, text: str) -> List[str]:
        """
        Extract specific types of information from text using the appropriate backend.
        
        Args:
            extraction_type: Type of information to extract
            text: Input text to extract information from
            
        Returns:
            List of extracted items
        """
        return asyncio.run(self._extract_async(extraction_type, text))
    
    async def _extract_async(self, extraction_type: str, text: str) -> List[str]:
        """Async implementation of information extraction."""
        return await self._extract_operation.extract(extraction_type, text)
    
    def anonymize(self, text: str) -> str:
        """
        Anonymize personal information in text using the appropriate backend.
        
        Args:
            text: Input text containing personal information to anonymize
            
        Returns:
            Anonymized text with personal information replaced by placeholders
        """
        return asyncio.run(self._anonymize_async(text))
    
    async def _anonymize_async(self, text: str) -> str:
        """Async implementation of text anonymization."""
        return await self._anonymize_operation.anonymize(text)
    
    def describe(self, features: Dict[str, Any], style: str = "natural") -> str:
        """
        Generate a meaningful text description from features using the appropriate backend.
        
        Args:
            features: Dictionary of product/object features
            style: Description style ("natural", "marketing", "technical", "casual")
            
        Returns:
            Natural language description of the features
        """
        return asyncio.run(self._describe_async(features, style))
    
    async def _describe_async(self, features: Dict[str, Any], style: str) -> str:
        """Async implementation of feature description generation."""
        return await self._describe_operation.describe(features, style)
    
    # Async versions for use in async contexts
    async def label_async(self, text: str, labels: List[str], multiple: bool = False) -> Union[SingleLabelResult, MultipleLabelResult]:
        """Async version of label() method."""
        return await self._label_async(text, labels, multiple)
    
    async def ai_async(self, prompt: str, data: str) -> str:
        """Async version of ai() method."""
        return await self._ai_async(prompt, data)
    
    async def extract_async(self, extraction_type: str, text: str) -> List[str]:
        """Async version of extract() method."""
        return await self._extract_async(extraction_type, text)
    
    async def anonymize_async(self, text: str) -> str:
        """Async version of anonymize() method."""
        return await self._anonymize_async(text)
    
    async def describe_async(self, features: Dict[str, Any], style: str = "natural") -> str:
        """Async version of describe() method."""
        return await self._describe_async(features, style)
    