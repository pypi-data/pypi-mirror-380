import logging
from typing import Any, AsyncGenerator

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_aws import ChatBedrock
from langchain_ibm import ChatWatsonx

logger = logging.getLogger("CustomLangchainClient")

class CustomLangchainClient:
    """
    Unified LangChain client that receives the provider and creates the appropriate model.
    """

    def __init__(self, provider: str, **kwargs):
        """
        Args:
            provider: string indicating the provider ("openai", "anthropic", "bedrock"...)
            kwargs: extra arguments (like api_key, model, etc.)
        """
        self.provider = provider.lower()
        self.kwargs = kwargs
        self.model = self._init_model()

    def _init_model(self):
        if self.provider == "openai":
            return ChatOpenAI(**self.kwargs)
        elif self.provider == "anthropic":
            return ChatAnthropic(**self.kwargs)
        elif self.provider == "bedrock":
            return ChatBedrock(**self.kwargs)
        elif self.provider == "watsonx":
            return ChatWatsonx(**self.kwargs)
        else:
            raise ValueError(f"Unsupported provider: {self.provider}")

    def generate(self, messages: list, **kwargs):
        """
        Executes text generation with LangChain.
        """
        try:
            response = self.model.invoke(messages, **kwargs)
            # injects the flashquery field
            setattr(response, "flashquery", {})
            return response
        except Exception as ex:
            logger.error(f"Error generating response with {self.provider}: {ex}")
            raise
    
    async def astream(self, messages: list, **kwargs) -> AsyncGenerator[Any, None]:
        """
        Async streaming with .flashquery in each chunk.
        """
        async for chunk in self.model.astream(messages, **kwargs):
            # Some providers deliver a list of parts in chunk.content
            setattr(chunk, "flashquery", {})
            yield chunk

    async def ainvoke(self, messages: list, **kwargs):
        """
        Single async call (no streaming).
        """
        try:
            response = await self.model.ainvoke(messages, **kwargs)
            setattr(response, "flashquery", {})
            return response
        except Exception as ex:
            logger.error(f"Error in ainvoke with {self.provider}: {ex}")
            raise