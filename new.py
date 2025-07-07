from langchain_google_genai import ChatGoogleGenerativeAI
from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled, NoTranscriptFound, VideoUnavailable



video_id = ""

try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id=video_id, languages=["en"])
    print(transcript)

except TranscriptsDisabled:
    print("❌ Transcripts are disabled for this video.")
except NoTranscriptFound:
    print("❌ No English transcript found for this video.")
except VideoUnavailable:
    print("❌ The video is unavailable or private.")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
