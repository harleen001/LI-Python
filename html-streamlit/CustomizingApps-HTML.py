import streamlit as st

def local_css(file_name):
    try:
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Could not find {file_name}. Make sure it is in the same folder as your script!")

# Call the function instead of using the <link> tag
local_css("styles.css")

st.text_input(
    "Enter your name:", 
    max_chars=10, 
    placeholder="Your name",
    help="This is a standard Streamlit input"
)

# Keep your branding hide script
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)