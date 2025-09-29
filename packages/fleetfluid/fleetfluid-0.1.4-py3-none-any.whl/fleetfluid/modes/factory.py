"""
Factory for creating FleetFluid operation implementations.
"""

from typing import Dict, Any
from .base import (
    LabelOperation,
    AIOperation,
    ExtractOperation,
    AnonymizeOperation,
    DescribeOperation
)
from .opensource import (
    OpenSourceLabelOperation,
    OpenSourceAIOperation,
    OpenSourceExtractOperation,
    OpenSourceAnonymizeOperation,
    OpenSourceDescribeOperation
)
from .cloud import (
    CloudLabelOperation,
    CloudAIOperation,
    CloudExtractOperation,
    CloudAnonymizeOperation,
    CloudDescribeOperation
)


class ModeFactory:
    """Factory for creating operation implementations based on mode."""
    
    @staticmethod
    def create_open_source_operations(model: str, **kwargs) -> Dict[str, Any]:
        """Create open source mode operation implementations."""
        return {
            'label_operation': OpenSourceLabelOperation(model, **kwargs),
            'ai_operation': OpenSourceAIOperation(model, **kwargs),
            'extract_operation': OpenSourceExtractOperation(model, **kwargs),
            'anonymize_operation': OpenSourceAnonymizeOperation(model, **kwargs),
            'describe_operation': OpenSourceDescribeOperation(model, **kwargs)
        }
    
    @staticmethod
    def create_cloud_operations(api_key: str, api_endpoint: str) -> Dict[str, Any]:
        """Create cloud mode operation implementations."""
        return {
            'label_operation': CloudLabelOperation(api_key, api_endpoint),
            'ai_operation': CloudAIOperation(api_key, api_endpoint),
            'extract_operation': CloudExtractOperation(api_key, api_endpoint),
            'anonymize_operation': CloudAnonymizeOperation(api_key, api_endpoint),
            'describe_operation': CloudDescribeOperation(api_key, api_endpoint)
        }
