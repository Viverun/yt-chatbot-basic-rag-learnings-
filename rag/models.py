from langchain_ollama import ChatOllama, OllamaEmbeddings


def get_embeddings():
    return OllamaEmbeddings(
        model="embeddinggemma:latest"
    )

def get_llm():
    return ChatOllama(
        model="gemma4:e2b",
        temperature=0.2,
        reasoning=False,
    )