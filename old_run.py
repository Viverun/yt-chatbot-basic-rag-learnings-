# # import subprocess

# from langchain_community.vectorstores import FAISS
# from langchain_core.prompts import PromptTemplate
# from langchain_ollama import ChatOllama, OllamaEmbeddings
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# from youtube_transcript_api import TranscriptsDisabled, YouTubeTranscriptApi

# from utils.url_parser import extract_video_id

#     # Step 1a - Indexing(Document Ingestion)

# url = input("Enter YouTube URL: ")
# video_id = extract_video_id(url)
# transcript = ""

# try:
#     transcript_list = YouTubeTranscriptApi().fetch(
#         video_id,
#         languages=['en','hi']
#     )
#     transcript = " ".join(snippet.text for snippet in transcript_list)
#     # print(transcript)
# except TranscriptsDisabled:
#     print("Transcripts are disabled for this video.")

#     # Step 1b - Indexing(Text Splitting)

# splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
# chunks  = splitter.create_documents([transcript])

#     # Step 1c - Indexing(Embedding)

# embeddings = OllamaEmbeddings(model='embeddinggemma:latest')
# vector_store = FAISS.from_documents(chunks, embeddings)
# # print("Number of vectors:", vectorstore.index.ntotal)

#     # Step 1d - Indexing(Retrieval)

# retriever = vector_store.as_retriever(search_type='similarity', search_kwargs={'k':3})
# # vector_store.save_local("faiss_index")
# #Saving the vector store is not optimal in my case
# # print(retriever.invoke('What is the Big Blob of compute Hypthesis?'))

    
# # Step 2 - Setting up the Model

# llm = ChatOllama(
#     model='gemma4:e2b',
#     temperature=0.2,
#     reasoning = False
# )

# # Step 3 - Augmentation
# prompt = PromptTemplate(
#     input_variables=["context", "question"],
#     template="""
# You are a helpful assistant that answers questions about a YouTube video.

# Use only the information provided in the context below.
# If the answer cannot be found in the context, say:
# "I couldn't find that information in the transcript."

# Context:
# {context}

# Question:
# {question}

# Answer:
# """
# )

# while True:
#     question = input("\nAsk a question: ")
#     if question.lower() == 'exit':
#         break
#     if not question.strip():
#         continue
        
#     retriever_docs = retriever.invoke(question)
#     context_text = "\n\n".join([doc.page_content for doc in retriever_docs])
    
#     final_prompt = prompt.invoke({'context': context_text, 'question': question})
    

#     # Step 4 - Generation
#     for chunk in llm.stream(final_prompt):
#         print(chunk.content, end='', flush=True)
#     print() 



# #  # Unload the embedding model
# # subprocess.run(
# #  ["ollama", "stop", "embeddinggemma:latest"],
# #  stdout=subprocess.DEVNULL,
# #  stderr=subprocess.DEVNULL,
# #  check = False,
# # )