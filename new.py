from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from youtube_transcript_api import  YouTubeTranscriptApi, TranscriptsDisabled

load_dotenv()

video_id = "E3oG313_kps"

transcript_text = YouTubeTranscriptApi.get_transcript(video_id=video_id,languages=["hi"])
print(transcript_text)