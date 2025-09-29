from typing import List, Dict, Any, Optional
from openai.resources.models import Models as OpenAIModels
from openai.resources.models import AsyncModels as OpenAIAsyncModels
import httpx
import logging

log = logging.getLogger(__name__)

class Models(OpenAIModels):
    """Models resource for CheckThat AI - provides access to available models."""
    
    def list(self, **kwargs) -> dict:
        """
        List all available models from the CheckThat AI backend.
        
        Returns:
            dict: Raw response from the backend
        """
        try:
            # Make request to backend models endpoint using httpx directly
            base_url = str(self._client.base_url).rstrip('/')
            with httpx.Client() as http_client:
                response = http_client.get(f"{base_url}/models", **kwargs)
                response.raise_for_status()
                return response.json()
            
        except httpx.HTTPStatusError as e:
            log.error(f"HTTP error listing models: {e}")
            raise
        except Exception as e:
            log.error(f"Error listing models: {e}")
            raise
    
    def retrieve(self, model_id: str, **kwargs) -> dict:
        """
        Retrieve information about a specific model.
        
        Args:
            model_id: The ID of the model to retrieve
            
        Returns:
            dict: Model information from the backend
        """
        try:
            # Get all models and find the specific one
            models_data = self.list(**kwargs)
            
            # Search through all providers and models
            for provider_data in models_data.get("models_list", []):
                for model_data in provider_data.get("available_models", []):
                    if model_data.get("model_id") == model_id:
                        return model_data
            
            # If model not found, raise an error
            raise ValueError(f"Model {model_id} not found")
            
        except Exception as e:
            log.error(f"Error retrieving model {model_id}: {e}")
            raise


class AsyncModels(OpenAIAsyncModels):
    """Async Models resource for CheckThat AI - provides async access to available models."""
    
    async def list(self, **kwargs) -> dict:
        """
        List all available models from the CheckThat AI backend (async).
        
        Returns:
            dict: Raw response from the backend
        """
        try:
            # Make async request to backend models endpoint using httpx directly
            base_url = str(self._client.base_url).rstrip('/')
            async with httpx.AsyncClient() as http_client:
                response = await http_client.get(f"{base_url}/models", **kwargs)
                response.raise_for_status()
                return response.json()
            
        except httpx.HTTPStatusError as e:
            log.error(f"HTTP error listing models: {e}")
            raise
        except Exception as e:
            log.error(f"Error listing models: {e}")
            raise
    
    async def retrieve(self, model_id: str, **kwargs) -> dict:
        """
        Retrieve information about a specific model (async).
        
        Args:
            model_id: The ID of the model to retrieve
            
        Returns:
            dict: Model information from the backend
        """
        try:
            # Get all models and find the specific one
            models_data = await self.list(**kwargs)
            
            # Search through all providers and models
            for provider_data in models_data.get("models_list", []):
                for model_data in provider_data.get("available_models", []):
                    if model_data.get("model_id") == model_id:
                        return model_data
            
            # If model not found, raise an error
            raise ValueError(f"Model {model_id} not found")
            
        except Exception as e:
            log.error(f"Error retrieving model {model_id}: {e}")
            raise