import os

from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from pydantic import SecretStr

load_dotenv()


def get_embeddings():
    api_key = os.getenv("AZURE_OPENAI_API_KEY")

    return AzureOpenAIEmbeddings(
        azure_deployment="text-embedding-3-small",
        api_version="2024-10-21",
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=SecretStr(api_key) if api_key else None,
    )


def get_llm():
    api_key = os.getenv("AZURE_OPENAI_API_KEY")

    return AzureChatOpenAI(
            azure_deployment="gpt-5-mini",
            api_version="2025-01-01-preview",
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=SecretStr(api_key) if api_key else None,
    )