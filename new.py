from langchain_google_genai import ChatGoogleGenerativeAI
from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled


video_id = ""

try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id=video_id, languages=["en","hi"])
    print(transcript)
except Exception as e:
    print("No caption Available for this video")
