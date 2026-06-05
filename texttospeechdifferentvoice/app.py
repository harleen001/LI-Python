import streamlit as st
import asyncio
import edge_tts
import tempfile
import os

st.set_page_config(page_title="Voice Studio", page_icon="🎙️", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body, [data-testid="stAppViewContainer"], [data-testid="stAppViewBlockContainer"] {
    background: #f7f8fc !important; font-family: 'Inter', sans-serif !important;
}
[data-testid="stHeader"] { background: transparent !important; }
.main .block-container { padding: 2rem 2rem; max-width: 700px; }
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stDecoration"] { display: none; }

.hero { text-align: center; padding: 1.2rem 0 1.8rem; }
.hero-title { font-size: 1.8rem; font-weight: 700; color: #111; letter-spacing: -0.03em; }
.hero-sub { font-size: 0.8rem; color: #aaa; margin-top: 0.3rem; }

.section-label {
    font-size: 0.68rem; font-weight: 600; color: #aaa;
    letter-spacing: 0.12em; text-transform: uppercase; margin-bottom: 0.8rem;
}
.div { height: 1px; background: #efefef; margin: 1.4rem 0; }

/* Gender cards */
.gcard {
    border-radius: 18px; overflow: hidden;
    border: 2.5px solid #ebebeb; background: #fff;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05); transition: all 0.2s;
}
.gcard img { width: 100%; height: 190px; object-fit: cover; object-position: center top; display: block; }
.gcard-footer { padding: 0.8rem 1rem; text-align: center; }
.gcard-name { font-size: 0.92rem; font-weight: 600; color: #555; }
.gcard.male-active   { border-color: #6366f1; box-shadow: 0 0 0 4px rgba(99,102,241,0.12); }
.gcard.female-active { border-color: #ec4899; box-shadow: 0 0 0 4px rgba(236,72,153,0.1); }
.gcard.male-active   .gcard-name { color: #6366f1; }
.gcard.female-active .gcard-name { color: #ec4899; }

/* Voice style grid */
.vstyle-grid {
    display: grid; grid-template-columns: repeat(5, 1fr);
    gap: 10px; margin-bottom: 1rem;
}
.vcard {
    border-radius: 14px; overflow: hidden;
    border: 2px solid #ebebeb; background: #fff;
    box-shadow: 0 1px 4px rgba(0,0,0,0.05); transition: all 0.18s;
}
.vcard img { width: 100%; aspect-ratio: 1/1; object-fit: cover; object-position: center top; display: block; }
.vcard-label {
    padding: 6px 4px 7px; font-size: 0.62rem; font-weight: 600;
    color: #666; text-align: center; line-height: 1.25;
}
.vcard.v-active  { border-color: #6366f1; box-shadow: 0 0 0 3px rgba(99,102,241,0.13); }
.vcard.v-active  .vcard-label { color: #6366f1; }
.vcard.fv-active { border-color: #ec4899; box-shadow: 0 0 0 3px rgba(236,72,153,0.1); }
.vcard.fv-active .vcard-label { color: #ec4899; }

/* Detail card */
.vdetail {
    display: flex; align-items: center; gap: 1rem;
    background: #fff; border: 1.5px solid #ebebeb; border-radius: 16px;
    padding: 0.9rem 1rem; margin-bottom: 1.2rem;
    box-shadow: 0 1px 4px rgba(0,0,0,0.05);
}
.vdetail img { width: 52px; height: 52px; border-radius: 12px; object-fit: cover; object-position: top; flex-shrink: 0; }
.vdetail-text h4 { font-size: 0.88rem; font-weight: 600; color: #222; margin-bottom: 0.2rem; }
.vdetail-text p  { font-size: 0.73rem; color: #999; }
.vdot { width: 9px; height: 9px; border-radius: 50%; margin-left: auto; flex-shrink: 0; }

/* Text area */
[data-testid="stTextArea"] label { display: none !important; }
[data-testid="stTextArea"] textarea {
    background: #fff !important; border: 2px solid #ebebeb !important;
    border-radius: 14px !important; color: #222 !important;
    font-family: 'Inter', sans-serif !important; font-size: 0.92rem !important;
    padding: 1rem !important; resize: none !important;
    box-shadow: 0 1px 4px rgba(0,0,0,0.03) !important;
}
[data-testid="stTextArea"] textarea:focus {
    border-color: #6366f1 !important;
    box-shadow: 0 0 0 3px rgba(99,102,241,0.09) !important; outline: none !important;
}
[data-testid="stTextArea"] textarea::placeholder { color: #ccc !important; }

/* Buttons */
[data-testid="stButton"] > button {
    border-radius: 11px !important; font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important; font-size: 0.82rem !important;
    padding: 0.5rem 0.9rem !important; border: 2px solid #e0e0e0 !important;
    background: #fff !important; color: #444 !important; width: 100% !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important; transition: all 0.15s !important;
}
[data-testid="stButton"] > button:hover { border-color: #bbb !important; transform: translateY(-1px) !important; }

/* Speak button */
div.speak-btn [data-testid="stButton"] > button {
    background: #111 !important; color: #fff !important; border-color: #111 !important;
    font-size: 0.95rem !important; padding: 0.75rem !important;
    box-shadow: 0 4px 14px rgba(0,0,0,0.2) !important;
}
div.speak-btn [data-testid="stButton"] > button:hover { background: #333 !important; border-color: #333 !important; }

[data-testid="stSuccess"] {
    background: #f0fdf4 !important; border: 1px solid #bbf7d0 !important;
    border-radius: 10px !important; color: #166534 !important; font-size: 0.82rem !important;
}
[data-testid="stError"] { border-radius: 10px !important; font-size: 0.82rem !important; }
audio { width: 100%; border-radius: 10px; margin-top: 0.75rem; }
</style>
""", unsafe_allow_html=True)

# ── Voice data — each uses a DISTINCT edge-tts voice name ────────────────────
# All voices are real Microsoft Neural voices, genuinely different people/styles
MALE_COVER   = "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=600&h=400&fit=crop&crop=top"
FEMALE_COVER = "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=600&h=400&fit=crop&crop=top"

VOICE_PROFILES = {
    "Male": [
        {
            "name": "Guy",  "emoji": "🎤",
            "desc": "US English · Deep & authoritative",
            "voice": "en-US-GuyNeural",
            "img": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=300&h=300&fit=crop&crop=top"
        },
        {
            "name": "Eric", "emoji": "📻",
            "desc": "US English · Smooth broadcaster",
            "voice": "en-US-EricNeural",
            "img": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=300&h=300&fit=crop&crop=top"
        },
        {
            "name": "Ryan",  "emoji": "🇬🇧",
            "desc": "UK English · British accent",
            "voice": "en-GB-RyanNeural",
            "img": "https://images.unsplash.com/photo-1519345182560-3f2917c472ef?w=300&h=300&fit=crop&crop=top"
        },
        {
            "name": "William", "emoji": "🇦🇺",
            "desc": "Australian · Calm & warm",
            "voice": "en-AU-WilliamNeural",
            "img": "https://images.unsplash.com/photo-1560250097-0b93528c311a?w=300&h=300&fit=crop&crop=top"
        },
        {
            "name": "Prabhat", "emoji": "🇮🇳",
            "desc": "Indian English · Warm & clear",
            "voice": "en-IN-PrabhatNeural",
            "img": "https://images.unsplash.com/photo-1531891437562-4301cf35b7e4?w=300&h=300&fit=crop&crop=top"
        },
    ],
    "Female": [
        {
            "name": "Jenny", "emoji": "🌸",
            "desc": "US English · Friendly & warm",
            "voice": "en-US-JennyNeural",
            "img": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=300&h=300&fit=crop&crop=top"
        },
        {
            "name": "Aria",  "emoji": "📢",
            "desc": "US English · Confident & clear",
            "voice": "en-US-AriaNeural",
            "img": "https://images.unsplash.com/photo-1544005313-94ddf0286df2?w=300&h=300&fit=crop&crop=top"
        },
        {
            "name": "Libby", "emoji": "🇬🇧",
            "desc": "UK English · British & elegant",
            "voice": "en-GB-LibbyNeural",
            "img": "https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?w=300&h=300&fit=crop&crop=top"
        },
        {
            "name": "Natasha", "emoji": "🇦🇺",
            "desc": "Australian · Bright & upbeat",
            "voice": "en-AU-NatashaNeural",
            "img": "https://images.unsplash.com/photo-1502685104226-ee32379fefbe?w=300&h=300&fit=crop&crop=top"
        },
        {
            "name": "Neerja", "emoji": "🇮🇳",
            "desc": "Indian English · Warm & expressive",
            "voice": "en-IN-NeerjaNeural",
            "img": "https://images.unsplash.com/photo-1589571894960-20bbe2828d0a?w=300&h=300&fit=crop&crop=top"
        },
    ]
}

async def synthesize(text, voice, output_path):
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_path)

if "gender" not in st.session_state: st.session_state.gender = "Male"
if "vstyle" not in st.session_state: st.session_state.vstyle = "Guy"

# Reset stale vstyle if gender switched and old name doesn't exist
current_profiles = VOICE_PROFILES[st.session_state.get("gender","Male")]
valid_names = [p["name"] for p in current_profiles]
if st.session_state.get("vstyle") not in valid_names:
    st.session_state.vstyle = current_profiles[0]["name"]

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-title">🎙️ Voice Studio</div>
  <div class="hero-sub">10 distinct neural voices · Real male &amp; female</div>
</div>""", unsafe_allow_html=True)

# ── 01 Text ───────────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">01 &nbsp; Your Text</div>', unsafe_allow_html=True)
text_input = st.text_area("", placeholder="Type something to hear it spoken...", height=110)
st.markdown('<div class="div"></div>', unsafe_allow_html=True)

# ── 02 Gender ─────────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">02 &nbsp; Select Gender</div>', unsafe_allow_html=True)
g = st.session_state.gender
c1, c2 = st.columns(2)
with c1:
    mc   = "gcard male-active" if g == "Male" else "gcard"
    tick = " ✓" if g == "Male" else ""
    st.markdown(f"""
    <div class="{mc}">
      <img src="{MALE_COVER}" alt="Male"/>
      <div class="gcard-footer"><span class="gcard-name">♂ Male{tick}</span></div>
    </div>""", unsafe_allow_html=True)
    if st.button("Select Male", key="btn_male"):
        st.session_state.gender = "Male"
        st.session_state.vstyle = "Guy"
        st.rerun()

with c2:
    fc    = "gcard female-active" if g == "Female" else "gcard"
    tick2 = " ✓" if g == "Female" else ""
    st.markdown(f"""
    <div class="{fc}">
      <img src="{FEMALE_COVER}" alt="Female"/>
      <div class="gcard-footer"><span class="gcard-name">♀ Female{tick2}</span></div>
    </div>""", unsafe_allow_html=True)
    if st.button("Select Female", key="btn_female"):
        st.session_state.gender = "Female"
        st.session_state.vstyle = "Jenny"
        st.rerun()

gender   = st.session_state.gender
is_female = gender == "Female"
st.markdown('<div class="div"></div>', unsafe_allow_html=True)

# ── 03 Voice Style ─────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">03 &nbsp; Choose Voice</div>', unsafe_allow_html=True)
profiles = VOICE_PROFILES[gender]

# Photo cards
cards_html = '<div class="vstyle-grid">'
for p in profiles:
    is_active = st.session_state.vstyle == p["name"]
    cls = ("vcard fv-active" if is_female else "vcard v-active") if is_active else "vcard"
    cards_html += f"""
    <div class="{cls}">
      <img src="{p['img']}" alt="{p['name']}"/>
      <div class="vcard-label">{p['emoji']} {p['name']}</div>
    </div>"""
cards_html += '</div>'
st.markdown(cards_html, unsafe_allow_html=True)

btn_cols = st.columns(5)
for i, p in enumerate(profiles):
    with btn_cols[i]:
        if st.button(p["name"], key=f"vbtn_{i}"):
            st.session_state.vstyle = p["name"]
            st.rerun()

profile = next(p for p in profiles if p["name"] == st.session_state.vstyle)
dot_color = "#ec4899" if is_female else "#6366f1"
st.markdown(f"""
<div class="vdetail">
  <img src="{profile['img']}" alt="{profile['name']}"/>
  <div class="vdetail-text">
    <h4>{profile['emoji']} {profile['name']}</h4>
    <p>{profile['desc']}</p>
  </div>
  <div class="vdot" style="background:{dot_color};"></div>
</div>""", unsafe_allow_html=True)

st.markdown('<div class="div"></div>', unsafe_allow_html=True)

# ── Speak ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="speak-btn">', unsafe_allow_html=True)
speak = st.button("▶  Speak It", use_container_width=True, key="speak_btn")
st.markdown('</div>', unsafe_allow_html=True)

if speak:
    if not text_input.strip():
        st.error("Please enter some text first.")
    else:
        with st.spinner("Generating voice..."):
            try:
                with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
                    tmp_path = tmp.name

                asyncio.run(synthesize(text_input.strip(), profile["voice"], tmp_path))

                with open(tmp_path, "rb") as f:
                    audio_bytes = f.read()
                os.unlink(tmp_path)

                if len(audio_bytes) > 500:
                    st.success(f"✓  {profile['emoji']} {profile['name']} ({gender}) — ready!")
                    st.audio(audio_bytes, format="audio/mp3")
                    st.download_button("⬇  Download MP3", audio_bytes,
                        file_name=f"{profile['name'].lower()}_{gender.lower()}.mp3",
                        mime="audio/mp3", use_container_width=True)
                else:
                    st.error("Audio generation failed. Check your internet connection.")
            except Exception as e:
                st.error(f"Error: {e}\n\nMake sure edge-tts is installed: pip install edge-tts")


                #listening to the server but not responding accordingly