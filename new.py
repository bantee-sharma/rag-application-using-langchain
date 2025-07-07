from langchain_google_genai import ChatGoogleGenerativeAI
from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled, NoTranscriptFound, VideoUnavailable



video_id = 'E3oG313_kps'

try:
    transcript_text = YouTubeTranscriptApi.get_transcript(video_id=video_id,languages=['hi'])

except TranscriptsDisabled:
    print("❌ Transcripts are disabled for this video.")
except NoTranscriptFound:
    print("❌ No English transcript found for this video.")
except VideoUnavailable:
    print("❌ The video is unavailable or private.")

