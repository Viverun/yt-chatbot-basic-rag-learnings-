from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter


def build_vector_store(transcript, embeddings):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )
    chunks = splitter.create_documents([transcript])
    return FAISS.from_documents(
        chunks, 
        embeddings,
    )

