from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from youtube_transcript_api import  YouTubeTranscriptApi, TranscriptsDisabled,NoTranscriptFound
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()

video_id = "E3oG313_kps"

try:
    transcript_text = YouTubeTranscriptApi.get_transcript(video_id=video_id,languages=["hi"])
    text = " ".join([i["text"] for i in transcript_text])
    

except NoTranscriptFound:
    print("No Captions found for this video.")

text_spiltter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=100)
chunks = text_spiltter.create_documents([text])
print(len(chunks))