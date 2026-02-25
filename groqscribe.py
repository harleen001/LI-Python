import streamlit as st
import assemblyai as aai
import yt_dlp
import os
from groq import Groq

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="Universal Groqscribe", page_icon="🔥", layout="wide")

# Paths & Keys (Consider using st.secrets for keys in production)
FFMPEG_DIR = "./"  # Ensure ffmpeg.exe and ffprobe.exe are in this folder
aai.settings.api_key = "##"
groq_client = Groq(api_key="##")

def download_audio(url):
    output_filename = "temp_audio"
    # Post-processor handles the .m4a extension automatically
    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'outtmpl': output_filename,
        'ffmpeg_location': FFMPEG_DIR,
        'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'm4a'}],
        'quiet': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return output_filename + ".m4a"

# --- 2. INTERFACE ---
st.title("🔥 Universal Groqscribe Pro Max")
url = st.text_input("YouTube URL:", placeholder="https://www.youtube.com/watch?v=...")

if st.button("Generate Article"):
    if not url:
        st.warning("Please enter a URL first.")
    else:
        try:
            # All steps must stay INSIDE this 'with' block to show progress
            with st.status("🏗️ Engine Running...", expanded=True) as status:
                
                # STEP 1: Download Audio
                st.write("📥 Downloading audio stream...")
                audio_path = download_audio(url)
                
                # STEP 2: Transcribe
                st.write("🎙️ AI is listening (this can take a minute)...")
                config = aai.TranscriptionConfig(
                    speech_models=["universal-3-pro", "universal-2"], 
                    language_detection=True
                )
                transcriber = aai.Transcriber()
                transcript = transcriber.transcribe(audio_path, config=config)

                # Safety check
                if transcript.status == aai.TranscriptStatus.error:
                    st.error(f"Transcription Error: {transcript.error}")
                    st.stop()
                
                if not transcript.text:
                    st.warning("No speech detected in this video.")
                    st.stop()

                # STEP 3: Groq Article Generation
                st.write("✍️ Drafting article with Llama 3.3...")
                response = groq_client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": "You are a professional blog writer."},
                        {"role": "user", "content": f"Write a structured article with headers from this transcript: {transcript.text[:15000]}"}
                    ]
                )
                
                # Cleanup local file
                if os.path.exists(audio_path):
                    os.remove(audio_path)
                
                status.update(label="✅ Success!", state="complete", expanded=False)

            # --- DISPLAY OUTPUT ---
            article_content = response.choices[0].message.content
            st.markdown("---")
            st.markdown(article_content)
            st.download_button("💾 Download Article", article_content, file_name="article.md")

        except Exception as e:
            st.error(f"System Error: {str(e)}")