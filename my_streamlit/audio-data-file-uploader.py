import streamlit as st
import pandas as pd

audio_value = st.audio_input("Record a voice message")
if audio_value:
    st.audio(audio_value)


# Higher sample rates can create higher-quality, larger audio files. 
audio_value = st.audio_input("Record high quality audio", sample_rate=48000)
if audio_value:
    st.audio(audio_value)


df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": False},
        {"command": "st.time_input", "rating": 3, "is_widget": True},
    ]
)
edited_df = st.data_editor(df)

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")



#uploading multiple files
uploaded_files = st.file_uploader(
    "Upload data", accept_multiple_files=True, type="csv"
)
for uploaded_file in uploaded_files:
    df = pd.read_csv(uploaded_file)
    st.write(df)

#camera widget
enable = st.checkbox("Enable camera")
picture = st.camera_input("Take a picture", disabled=not enable)

if picture:
    st.image(picture)