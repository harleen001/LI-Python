import streamlit as st

#vertical alignment, middle space three parts divided
left, middle, right = st.columns(3)

left.space("medium")
left.button("Left button", width="stretch")

middle.space("small")
middle.text_input("Middle input")

right.audio_input("Right uploader")


#left and right button divided
with st.container(horizontal=True):
    st.button("Left")
    st.space("stretch")
    st.button("Right")