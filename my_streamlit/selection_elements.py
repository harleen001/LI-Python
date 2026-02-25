import streamlit as st

agree = st.checkbox("I agree")

if agree:
    st.write("Great!")

color = st.color_picker("Pick A Color", "#00f900")
st.write("The current color is", color)

#sentiment-mapping for color
sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"You selected {sentiment_mapping[selected]} star(s).")