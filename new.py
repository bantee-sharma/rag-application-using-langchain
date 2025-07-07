from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound, VideoUnavailable

video_id = "MdeQMVBuGgY"

try:
    # List available transcripts
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

    print("✅ Available Transcripts:")
    for t in transcript_list:
        print(f"  - Language: {t.language_code}, Auto-generated: {t.is_generated}")

    # Try to get English transcript (manually or auto-generated)
    transcript = transcript_list.find_transcript(['en'])

    # Fetch and convert to plain text
    transcript_data = transcript.fetch()
    full_text = " ".join([item['text'] for item in transcript_data])

    print("\n📝 Transcript:\n")
    print(full_text)

except TranscriptsDisabled:
    print("❌ Transcripts are disabled for this video.")
except NoTranscriptFound:
    print("❌ No transcript found for this video.")
except VideoUnavailable:
    print("❌ The video is unavailable or private.")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
