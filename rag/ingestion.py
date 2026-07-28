from youtube_transcript_api import (
    TranscriptsDisabled,
    YouTubeTranscriptApi,
)

from utils.url_parser import extract_video_id


def load_transcript(url: str) -> str:
    video_id = extract_video_id(url)

    try:
        transcript_list = YouTubeTranscriptApi().fetch(
            video_id,
            languages=["en", "hi"],
        )

        return " ".join(
            snippet.text
            for snippet in transcript_list
        )

    except TranscriptsDisabled:
        print('Transcripts are disabled for video ')
        return ""