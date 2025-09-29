"""
Open Source Mode implementations using PydanticAI agents directly.
"""

from typing import Any, Dict, List, Optional
from pydantic_ai import Agent

from .base import (
    LabelOperation,
    AIOperation,
    ExtractOperation,
    AnonymizeOperation,
    DescribeOperation
)
from ..models import SingleLabelResult, MultipleLabelResult


class OpenSourceLabelOperation(LabelOperation):
    """Open source labeling implementation using PydanticAI."""
    
    def __init__(self, model: str, **kwargs):
        self.model = model
        self.agent_config = kwargs
        self._label_agent: Optional[Agent] = None
    
    def _get_label_agent(self) -> Agent:
        """Lazy initialization of the labeling agent."""
        if self._label_agent is None:
            # Extract model settings from agent_config
            model_settings = {}
            agent_kwargs = {}
            
            for key, value in self.agent_config.items():
                if key in ['temperature', 'max_tokens', 'top_p', 'frequency_penalty', 'presence_penalty']:
                    model_settings[key] = value
                else:
                    agent_kwargs[key] = value
            
            # Create ModelSettings if we have model-specific parameters
            if model_settings:
                from pydantic_ai.models import ModelSettings
                agent_kwargs['model_settings'] = ModelSettings(model_settings)
            
            self._label_agent = Agent(
                model=self.model,
                system_prompt=(
                    "You are a specialized AI assistant for text classification and labeling. "
                    "You will receive text content and a list of possible labels. "
                    "Your task is to select the most appropriate label(s) based on the content. "
                    "Be precise and thoughtful in your selection, considering the context and meaning of the text. "
                    "Always follow the exact output format specified in the prompt. "
                    "Ensure confidence scores are between 0.0 and 1.0. "
                    "Provide clear, concise reasoning for your choices."
                ),
                **agent_kwargs
            )
        return self._label_agent
    
    async def label_single(self, text: str, labels: List[str]) -> SingleLabelResult:
        """Open source implementation of single label classification."""
        agent = self._get_label_agent()
        
        labels_str = ", ".join(labels)
        prompt = f"""
        You are a text classification expert. Analyze the following text and select the single most appropriate label from the provided options.

        Text to classify: "{text}"
        
        Available labels: {labels_str}
        
        Instructions:
        1. Read the text carefully
        2. Consider the overall sentiment, topic, and intent
        3. Select exactly ONE label that best describes the text
        4. Provide a confidence score between 0.0 and 1.0
        5. Give a brief explanation for your choice
        
        Return your response in the exact format:
        - label: [selected label from the list]
        - confidence: [number between 0.0 and 1.0]
        - reasoning: [brief explanation]
        """
        
        try:
            result = await agent.run(prompt, output_type=SingleLabelResult)
            return result.output
        except Exception as e:
            # Add debugging information
            print(f"Debug - Single label classification failed:")
            print(f"Text: {text}")
            print(f"Labels: {labels}")
            print(f"Error: {str(e)}")
            raise RuntimeError(f"Open source labeling failed: {str(e)}") from e
    
    async def label_multiple(self, text: str, labels: List[str]) -> MultipleLabelResult:
        """Open source implementation of multiple label classification."""
        agent = self._get_label_agent()
        
        labels_str = ", ".join(labels)
        prompt = f"""
        You are a text classification expert. Analyze the following text and select ALL appropriate labels from the provided options.

        Text to classify: "{text}"
        
        Available labels: {labels_str}
        
        Instructions:
        1. Read the text carefully
        2. Consider all aspects: sentiment, topic, intent, and specific issues mentioned
        3. Select ALL labels that apply to the text (can be one or more)
        4. Provide a confidence score for each selected label between 0.0 and 1.0
        5. Give a brief explanation for your choices
        
        Return your response in the exact format:
        - labels: [list of selected labels from the available options]
        - confidence_scores: [dictionary with label as key and confidence as value]
        - reasoning: [brief explanation of why these labels were chosen]
        """
        
        try:
            result = await agent.run(prompt, output_type=MultipleLabelResult)
            return result.output
        except Exception as e:
            # Add debugging information
            print(f"Debug - Multiple label classification failed:")
            print(f"Text: {text}")
            print(f"Labels: {labels}")
            print(f"Error: {str(e)}")
            raise RuntimeError(f"Open source labeling failed: {str(e)}") from e


class OpenSourceAIOperation(AIOperation):
    """Open source AI transformation implementation using PydanticAI."""
    
    def __init__(self, model: str, **kwargs):
        self.model = model
        self.agent_config = kwargs
        self._ai_agent: Optional[Agent] = None
    
    def _get_ai_agent(self) -> Agent:
        """Lazy initialization of the AI transformation agent."""
        if self._ai_agent is None:
            # Extract model settings from agent_config
            model_settings = {}
            agent_kwargs = {}
            
            for key, value in self.agent_config.items():
                if key in ['temperature', 'max_tokens', 'top_p', 'frequency_penalty', 'presence_penalty']:
                    model_settings[key] = value
                else:
                    agent_kwargs[key] = value
            
            # Create ModelSettings if we have model-specific parameters
            if model_settings:
                from pydantic_ai.models import ModelSettings
                agent_kwargs['model_settings'] = ModelSettings(model_settings)
            
            self._ai_agent = Agent(
                model=self.model,
                system_prompt=(
                    "You are a helpful AI assistant specialized in text transformation and processing. "
                    "You will receive a transformation prompt and input data. "
                    "Apply the requested transformation accurately and return only the transformed result. "
                    "Do not include explanations, markdown formatting, or additional text unless specifically requested."
                ),
                **agent_kwargs
            )
        return self._ai_agent
    
    async def ai(self, prompt: str, data: str) -> str:
        """Open source implementation of AI transformation."""
        agent = self._get_ai_agent()
        
        # Combine the transformation prompt with the data
        full_prompt = f"{prompt}\n\nInput data: {data}"
        
        try:
            result = await agent.run(full_prompt)
            return str(result.output)
        except Exception as e:
            raise RuntimeError(f"Open source AI transformation failed: {str(e)}") from e


class OpenSourceExtractOperation(ExtractOperation):
    """Open source extraction implementation using PydanticAI."""
    
    def __init__(self, model: str, **kwargs):
        self.model = model
        self.agent_config = kwargs
        self._ai_agent: Optional[Agent] = None
    
    def _get_ai_agent(self) -> Agent:
        """Lazy initialization of the AI agent."""
        if self._ai_agent is None:
            # Extract model settings from agent_config
            model_settings = {}
            agent_kwargs = {}
            
            for key, value in self.agent_config.items():
                if key in ['temperature', 'max_tokens', 'top_p', 'frequency_penalty', 'presence_penalty']:
                    model_settings[key] = value
                else:
                    agent_kwargs[key] = value
            
            # Create ModelSettings if we have model-specific parameters
            if model_settings:
                from pydantic_ai.models import ModelSettings
                agent_kwargs['model_settings'] = ModelSettings(model_settings)
            
            self._ai_agent = Agent(
                model=self.model,
                system_prompt=(
                    "You are a helpful AI assistant specialized in information extraction. "
                    "Extract the requested information accurately and return only the extracted items."
                ),
                **agent_kwargs
            )
        return self._ai_agent
    
    async def extract(self, extraction_type: str, text: str) -> List[str]:
        """Open source implementation of information extraction."""
        agent = self._get_ai_agent()
        
        prompt = f"""
        Extract {extraction_type} from the following text.
        
        Text: {text}
        
        Return only a list of {extraction_type}, one per line, without explanations or additional formatting.
        If no {extraction_type} are found, return an empty list.
        Be thorough and extract both explicit and implicit {extraction_type} mentioned in the text.
        """
        
        try:
            result = await agent.run(prompt)
            # Parse the result to extract individual items
            extracted_text = str(result.output).strip()
            
            if not extracted_text:
                return []
            
            # Split by newlines and clean up each item
            items = [item.strip() for item in extracted_text.split('\n') if item.strip()]
            
            # Remove any bullet points or numbering if present
            cleaned_items = []
            for item in items:
                # Remove common list markers
                cleaned = item.lstrip('•-*0123456789. ')
                if cleaned:
                    cleaned_items.append(cleaned)
            
            return cleaned_items
            
        except Exception as e:
            raise RuntimeError(f"Open source information extraction failed: {str(e)}") from e


class OpenSourceAnonymizeOperation(AnonymizeOperation):
    """Open source anonymization implementation using PydanticAI."""
    
    def __init__(self, model: str, **kwargs):
        self.model = model
        self.agent_config = kwargs
        self._ai_agent: Optional[Agent] = None
    
    def _get_ai_agent(self) -> Agent:
        """Lazy initialization of the AI agent."""
        if self._ai_agent is None:
            # Extract model settings from agent_config
            model_settings = {}
            agent_kwargs = {}
            
            for key, value in self.agent_config.items():
                if key in ['temperature', 'max_tokens', 'top_p', 'frequency_penalty', 'presence_penalty']:
                    model_settings[key] = value
                else:
                    agent_kwargs[key] = value
            
            # Create ModelSettings if we have model-specific parameters
            if model_settings:
                from pydantic_ai.models import ModelSettings
                agent_kwargs['model_settings'] = ModelSettings(model_settings)
            
            self._ai_agent = Agent(
                model=self.model,
                system_prompt=(
                    "You are a helpful AI assistant specialized in text anonymization. "
                    "Replace personal information with appropriate placeholders."
                ),
                **agent_kwargs
            )
        return self._ai_agent
    
    async def anonymize(self, text: str) -> str:
        """Open source implementation of text anonymization."""
        agent = self._get_ai_agent()
        
        prompt = f"""
        Anonymize the following text by replacing personal information with appropriate placeholders.
        
        Replace:
        - Names with [NAME]
        - Email addresses with [EMAIL]
        - Phone numbers with [PHONE]
        - Addresses with [ADDRESS]
        - Social security numbers with [SSN]
        - Credit card numbers with [CARD_NUMBER]
        - Any other personally identifiable information with appropriate placeholders
        
        Input text: {text}
        
        Return only the anonymized text without explanations or additional formatting.
        """
        
        try:
            result = await agent.run(prompt)
            return str(result.output)
        except Exception as e:
            raise RuntimeError(f"Open source anonymization failed: {str(e)}") from e


class OpenSourceDescribeOperation(DescribeOperation):
    """Open source description generation implementation using PydanticAI."""
    
    def __init__(self, model: str, **kwargs):
        self.model = model
        self.agent_config = kwargs
        self._ai_agent: Optional[Agent] = None
    
    def _get_ai_agent(self) -> Agent:
        """Lazy initialization of the AI agent."""
        if self._ai_agent is None:
            # Extract model settings from agent_config
            model_settings = {}
            agent_kwargs = {}
            
            for key, value in self.agent_config.items():
                if key in ['temperature', 'max_tokens', 'top_p', 'frequency_penalty', 'presence_penalty']:
                    model_settings[key] = value
                else:
                    agent_kwargs[key] = value
            
            # Create ModelSettings if we have model-specific parameters
            if model_settings:
                from pydantic_ai.models import ModelSettings
                agent_kwargs['model_settings'] = ModelSettings(model_settings)
            
            self._ai_agent = Agent(
                model=self.model,
                system_prompt=(
                    "You are a helpful AI assistant specialized in generating natural language descriptions. "
                    "Create coherent, flowing descriptions based on provided features."
                ),
                **agent_kwargs
            )
        return self._ai_agent
    
    async def describe(self, features: Dict[str, Any], style: str) -> str:
        """Open source implementation of feature description generation."""
        agent = self._ai_agent
        
        # Convert features dict to a readable format
        features_str = ", ".join([f"{key}: {value}" for key, value in features.items()])
        
        prompt = f"""
        Create a meaningful text description based on the following features.
        
        Features: {features_str}
        Style: Write that text in {style} style.
        
        Combine the features into a coherent, natural sentence that flows well.
        Do not list the features separately - integrate them naturally.
        Return only the description without explanations or additional formatting.
        """
        
        try:
            result = await agent.run(prompt)
            return str(result.output)
        except Exception as e:
            raise RuntimeError(f"Open source description generation failed: {str(e)}") from e
