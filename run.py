from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from utils.url_parser import extract_video_id


    # Step 1a - Indexing(Document Ingestion)

url = input("Enter YouTube URL: ")
video_id = extract_video_id(url)
try:
    transcript_list = YouTubeTranscriptApi().fetch(
        video_id,
        languages=['en','hi']
    )
    transcript = " ".join(snippet.text for snippet in transcript_list)
    print(transcript)
except TranscriptsDisabled:
    print("Transcripts are disabled for this video.")

    # Step 1b - Indexing(Text Splitting)
