"""
Data models for FleetFluid.
"""

from pydantic import BaseModel, Field
from typing import List, Dict


class SingleLabelResult(BaseModel):
    """Result for single label classification."""
    label: str = Field(description="The selected label from the provided options")
    confidence: float = Field(description="Confidence score between 0 and 1", ge=0, le=1)
    reasoning: str = Field(description="Brief explanation of why this label was chosen")


class MultipleLabelResult(BaseModel):
    """Result for multiple label classification."""
    labels: List[str] = Field(description="List of selected labels from the provided options")
    confidence_scores: Dict[str, float] = Field(description="Confidence score for each selected label")
    reasoning: str = Field(description="Brief explanation of why these labels were chosen")
