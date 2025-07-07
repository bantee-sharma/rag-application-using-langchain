from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled, VideoUnavailable

video_id = "MdeQMVBuGgY"

try:
    # List all available transcripts
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

    print("✅ Available Transcripts:")
    for t in transcript_list:
        print(f"  - Language: {t.language_code}, Auto-generated: {t.is_generated}")

    # Try Hindi first
    try:
        transcript = transcript_list.find_transcript(['hi'])  # Hindi
    except NoTranscriptFound:
        print("⚠️ No Hindi transcript found. Trying English (manual or auto).")
        try:
            transcript = transcript_list.find_transcript(['en-IN'])  # Manual English
        except NoTranscriptFound:
            transcript = transcript_list.find_transcript(['en'])     # Auto English

    # Fetch and print
    transcript_data = transcript.fetch()
    full_text = " ".join([entry['text'] for entry in transcript_data])
    print("\n📝 Transcript:\n")
    print(full_text)

except TranscriptsDisabled:
    print("❌ Transcripts are disabled for this video.")
except VideoUnavailable:
    print("❌ The video is unavailable or private.")
except Exception as e:
    print(f"❌ Unexpected error: {e}")
