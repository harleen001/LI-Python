import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

df = pd.read_csv("superstore.csv")

col1, col2 = st.columns([2, 1]) 

with col2:
    category = st.selectbox("Select Category", options=df['Category'].unique())
    
    sub_df = df[df['Category'] == category]
    unique_subs = sub_df['Sub-Category'].unique()
    
    selected_subs = []
    st.write("Select Sub-Categories:")
    for sub in unique_subs:
        if st.checkbox(sub, key=sub, value=False):
            selected_subs.append(sub)

filtered_df = df[(df['Category'] == category) & (df['Sub-Category'].isin(selected_subs))]

with col1:
    col1A, col1B = st.columns(2)
    
    with col1A:
        st.subheader("Sales")
        st.bar_chart(filtered_df['Sales'])
        
        st.subheader("Profit")
        st.bar_chart(filtered_df['Profit'])
    
    with col1B:
        st.subheader("Discount")
        st.bar_chart(filtered_df['Discount'])

st.markdown("""
    <style>
    .block-container {
        padding-top: 5rem;
        padding-bottom: 0rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)