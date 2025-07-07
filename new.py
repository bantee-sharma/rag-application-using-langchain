from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound, VideoUnavailable

video_id = 'MdeQMVBuGgY'

try:
    transcript_text = YouTubeTranscriptApi.get_transcript(video_id, languages=['hi',"en"])
    text = "".join([i["text"] for i in transcript_text])
    print(text)
except TranscriptsDisabled:
    print("❌ Transcripts are disabled for this video.")
except NoTranscriptFound:
    print("❌ No transcript found for the specified language.")
except VideoUnavailable:
    print("❌ Video is unavailable.")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")


