import streamlit as st

st.set_page_config(layout="wide")

st.title("Project Dashboard")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Streamlit Documentation")
    st.info("Access the latest guides and API references.")
    st.link_button("Open Documentation", "https://docs.streamlit.io/en/latest", use_container_width=True)

with col2:
    st.subheader("Random Services")
    st.info("Probability and Statistical resources.")
    st.link_button("Open Resource", "https://www.randomservices.org/", use_container_width=True)