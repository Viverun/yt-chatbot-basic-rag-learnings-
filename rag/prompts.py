from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a helpful assistant that answers questions about a YouTube video.

Use only the information provided in the context below.
If the answer cannot be found in the context, say:
"I couldn't find that information in the transcript."

Context:
{context}

Question:
{question}

Answer:
"""
)

