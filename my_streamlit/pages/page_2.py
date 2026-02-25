import streamlit as st

def page_2():
    st.title("Page 2")
    st.page_link("page_1.py", query_params={"utm_source": "page_2"})

pg = st.navigation([page_2, "page_1.py"])
pg.run()