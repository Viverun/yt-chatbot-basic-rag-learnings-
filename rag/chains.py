from langchain_core.runnables import RunnablePassthrough


def build_rag_chain(retriver, prompt, llm):
    rag_chain = (
        {
            'context':retriver,
            'question':RunnablePassthrough()
        }
        | prompt
        | llm
    )
    return rag_chain
