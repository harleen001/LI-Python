import io
import streamlit as st
import speech_recognition as sr
import yt_dlp
from pydub import AudioSegment

# ─────────────────────────────────────────────
# NLP: extract keywords from spoken text
# ─────────────────────────────────────────────
STOP_WORDS = {
    "play", "search", "find", "i", "want", "to", "listen", "hear",
    "song", "music", "please", "the", "a", "an", "me", "some", "put",
    "on", "give", "let", "ok", "okay", "hey", "now"
}

def extract_keywords(text: str) -> str:
    words = text.lower().split()
    keywords = [w for w in words if w not in STOP_WORDS]
    return " ".join(keywords) if keywords else text.lower()

# ─────────────────────────────────────────────
# Page config
# ─────────────────────────────────────────────
st.set_page_config(page_title="🎵 Voice Music", page_icon="🎵", layout="centered")

st.markdown("""
    <h1 style='text-align:center; font-size:2.5rem;'>🎵 Voice Music Search</h1>
    <p style='text-align:center; color:gray;'>Record your voice → keywords extracted → music plays</p>
    <hr>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# Step 1: Record voice using built-in widget
# ─────────────────────────────────────────────
st.subheader("Step 1 — Speak a song name")
audio_input = st.audio_input("🎤 Press to record")

if audio_input:
    audio_bytes = audio_input.read()

    # ── Step 2: Speech → Text ──────────────────
    st.subheader("Step 2 — Converting speech to text...")
    try:
        buf = io.BytesIO(audio_bytes)
        segment = AudioSegment.from_file(buf)
        wav_buf = io.BytesIO()
        segment.export(wav_buf, format="wav")
        wav_buf.seek(0)

        r = sr.Recognizer()
        with sr.AudioFile(wav_buf) as source:
            audio = r.record(source)
        spoken_text = r.recognize_google(audio)

    except sr.UnknownValueError:
        st.error("❌ Couldn't understand. Please speak clearly and try again.")
        st.stop()
    except Exception as e:
        st.error(f"❌ Error: {e}")
        st.stop()

    st.success(f"🗣️ You said: **\"{spoken_text}\"**")

    # ── Step 3: NLP keyword extraction ────────
    st.subheader("Step 3 — Extracting keywords")
    keywords = extract_keywords(spoken_text)
    st.info(f"🔍 Search keywords: **{keywords}**")

    # ── Step 4: Search & stream music + video ─────────
    st.subheader("Step 4 — Searching music...")
    try:
        ydl_opts = {"format": "bestaudio", "noplaylist": True, "quiet": True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch1:{keywords}", download=False)
    except Exception as e:
        st.error(f"❌ Search failed: {e}")
        st.stop()

    entries = info.get("entries") or []
    if not entries:
        st.error("No results found. Try saying a different song.")
        st.stop()

    entry      = entries[0]
    title      = entry["title"]
    audio_url  = entry["url"]
    video_id   = entry.get("id", "")
    thumbnail  = entry.get("thumbnail", "")

    st.success(f"🎶 Found: **{title}**")

    # ── Video embed (YouTube iframe) ───────────────────
    if video_id:
        st.subheader("🎬 Video")
        st.markdown(
            f"""
            <iframe
                width="100%" height="400"
                src="https://www.youtube.com/embed/{video_id}?autoplay=1"
                frameborder="0"
                allow="autoplay; encrypted-media"
                allowfullscreen>
            </iframe>
            """,
            unsafe_allow_html=True,
        )

    # ── Audio-only player ──────────────────────────────
    st.subheader("🎵 Audio only")
    with st.spinner("Loading audio..."):
        try:
            import requests
            resp = requests.get(audio_url, timeout=30)
            resp.raise_for_status()
            st.audio(io.BytesIO(resp.content))
        except Exception as e:
            st.error(f"❌ Could not load audio: {e}")