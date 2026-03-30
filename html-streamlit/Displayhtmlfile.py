import streamlit as st
import streamlit.components.v1 as components
path_to_html = "./home.html" 

with open(path_to_html,'r') as f: 
    html_data = f.read()

# Show in webpage
st.header("Show an external HTML")
st.components.v1.html(html_data)