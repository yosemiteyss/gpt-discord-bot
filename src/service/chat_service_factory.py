from src.service.azure_openai_service import AzureOpenAIService
from src.service.chat_service import ChatServiceType, ChatService
from src.service.openai_service import OpenAIService
from src.service.genai_service import GenaiService


class ChatServiceFactory:
    @staticmethod
    def get_service_cls(service_type: ChatServiceType) -> ChatService:
        if service_type == ChatServiceType.OPENAI:
            return OpenAIService()

        if service_type == ChatServiceType.AZURE:
            return AzureOpenAIService()

        if service_type == ChatServiceType.GENAI:
            return GenaiService()

        raise ValueError(f'Unknown chat service type: {service_type}')
