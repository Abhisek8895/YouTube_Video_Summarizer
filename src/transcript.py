from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube
import re

def extract_video_id(url: str) -> str:
    """
    Extracts Video Id from different YouTube URL format.
    """
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    if not match:
        raise ValueError("Invalid YouTube URL")
    return match.group(1)

def get_video_metadata(url: str) -> dict:
    """
    Fetches video title, length and thumbnail
    """
    yt = YouTube(url)
    return {
        "title": yt.title,
        "length": yt.length,
        "thumbnail": yt.thumbnail_url
    }

def get_transcript(url: str) -> str:
    """
    Fetches full transcript as a single string.
    """
    video_id = extract_video_id(url)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    full_text = " ".join(chunk["text"] for chunk in transcript)
    return full_text