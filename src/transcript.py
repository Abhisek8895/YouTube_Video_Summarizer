from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api import YouTubeTranscriptApi
import requests
from urllib.parse import urlparse, parse_qs

def extract_video_id(url):
    parsed = urlparse(url)
    if parsed.hostname == "youtu.be":
        return parsed.path[1:]
    if parsed.hostname in ("www.youtube.com", "youtube.com"):
        return parse_qs(parsed.query).get("v", [None])[0]
    return None


def get_video_metadata(url):
    print("URL received:", url)

    video_id = extract_video_id(url)

    if not video_id:
        raise Exception("Invalid YouTube URL")

    oembed_url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json"

    response = requests.get(oembed_url)

    if response.status_code != 200:
        raise Exception(f"Metadata fetch failed with status {response.status_code}")

    data = response.json()

    return {
        "title": data["title"],
        "thumbnail": data["thumbnail_url"],
        "length": "N/A"
    }

def get_transcript(url: str) -> str:
    """
    Fetches full transcript as a single string.
    """
    video_id = extract_video_id(url)

    try:
        transcript_list = YouTubeTranscriptApi().fetch(video_id)
        full_text = " ".join(chunk.text for chunk in transcript_list)
        return full_text

    except Exception as e:
        print("Transcript error:", str(e))
        raise e