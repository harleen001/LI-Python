import streamlit as st

# AUDIO:     st.audio("abc.mp3", format="audio/mpeg", loop=True)

#AUDIO INPUT
st.audio_input("Please speak")

st.badge("Hello", color="red")
st.balloons()

# st.camera_input("Click me !")
st.caption("this is camera")


st.code("""
        def hello():
            print("Hello")
        """,language="python")
st.color_picker("pick color")
st.divider()

st.download_button("Download me",data="Hello kartik")