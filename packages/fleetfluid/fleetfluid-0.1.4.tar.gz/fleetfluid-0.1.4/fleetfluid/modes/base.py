"""
Abstract base classes for FleetFluid operations.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Union
from ..models import SingleLabelResult, MultipleLabelResult


class LabelOperation(ABC):
    """Abstract base class for labeling operations."""
    
    @abstractmethod
    async def label_single(self, text: str, labels: List[str]) -> SingleLabelResult:
        """Label text with single label selection."""
        pass
    
    @abstractmethod
    async def label_multiple(self, text: str, labels: List[str]) -> MultipleLabelResult:
        """Label text with multiple label selection."""
        pass


class AIOperation(ABC):
    """Abstract base class for AI transformation operations."""
    
    @abstractmethod
    async def ai(self, prompt: str, data: str) -> str:
        """Apply AI transformation to data."""
        pass


class ExtractOperation(ABC):
    """Abstract base class for extraction operations."""
    
    @abstractmethod
    async def extract(self, extraction_type: str, text: str) -> List[str]:
        """Extract specific information from text."""
        pass


class AnonymizeOperation(ABC):
    """Abstract base class for anonymization operations."""
    
    @abstractmethod
    async def anonymize(self, text: str) -> str:
        """Anonymize personal information in text."""
        pass


class DescribeOperation(ABC):
    """Abstract base class for description generation operations."""
    
    @abstractmethod
    async def describe(self, features: Dict[str, Any], style: str) -> str:
        """Generate description from features."""
        pass
