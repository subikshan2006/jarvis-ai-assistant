from youtube_transcript_api import YouTubeTranscriptApi
from brain import ask_brain

def get_video_id(url):
    import re
    pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(pattern, url)
    return match.group(1) if match else None

def learn_from_youtube(url):
    try:
        video_id = get_video_id(url)
        if not video_id:
            return "Sorry, I couldn't extract the video ID."

        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = " ".join([entry['text'] for entry in transcript])
        summary = ask_brain(f"Summarize this YouTube video:\n{text[:3000]}")
        return summary
    except Exception as e:
        return f"Failed to learn from YouTube: {e}"
