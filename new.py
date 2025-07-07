from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound, VideoUnavailable

video_id = 'E3oG313_kps'

try:
    transcript_text = YouTubeTranscriptApi.get_transcript(video_id, languages=['hi'])
except TranscriptsDisabled:
    print("❌ Transcripts are disabled for this video.")
except NoTranscriptFound:
    print("❌ No transcript found for the specified language.")
except VideoUnavailable:
    print("❌ Video is unavailable.")
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")


