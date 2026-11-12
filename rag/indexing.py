from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter


def build_vector_store(transcript, embeddings):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
    )

    chunks = splitter.create_documents([transcript])

    print("Chunks created:", len(chunks))

    vector_store = FAISS.from_documents(
        chunks,
        embeddings,
    )

    print("FAISS vectors:", vector_store.index.ntotal)

    return vector_store