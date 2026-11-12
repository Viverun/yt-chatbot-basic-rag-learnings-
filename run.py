from yaspin import yaspin

from rag.chains import build_rag_chain
from rag.indexing import build_vector_store
from rag.ingestion import load_transcript
from rag.models import get_embeddings, get_llm
from rag.prompts import prompt

url = input("Enter YouTube URL: ")

with yaspin(text="Loading transcript..."):
    transcript = load_transcript(url)

with yaspin(text="Creating embeddings and vector store..."):
    embeddings = get_embeddings()

    vector_store = build_vector_store(
        transcript,
        embeddings,
    )

retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3},
)

llm = get_llm()

chain = build_rag_chain(
    retriever,
    prompt,
    llm,
)

while True:
    question = input("\nAsk a question: ")

    if question.lower() == "exit":
        break
        
    if not question.strip():
        continue
    
    print("\nAnswer: ")
    
    for chunk in chain.stream(question):
        print(chunk.content, end='', flush=True)
    print() 