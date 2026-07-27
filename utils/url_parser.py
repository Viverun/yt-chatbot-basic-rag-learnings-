from urllib.parse import urlparse, parse_qs

def extract_video_id(url_or_id: str) -> str:
    # Already a video ID
    if len(url_or_id) == 11 and "/" not in url_or_id:
        return url_or_id

    parsed = urlparse(url_or_id)

    if parsed.hostname in ("youtu.be", "www.youtu.be"):
        return parsed.path.lstrip("/")

    if parsed.hostname in (
        "youtube.com",
        "www.youtube.com",
        "m.youtube.com",
    ):
        if parsed.path == "/watch":
            query = parse_qs(parsed.query)
            if "v" in query:
                return query["v"][0]

        if parsed.path.startswith("/shorts/"):
            return parsed.path.split("/")[2]

        if parsed.path.startswith("/embed/"):
            return parsed.path.split("/")[2]

    raise ValueError("Invalid YouTube URL")