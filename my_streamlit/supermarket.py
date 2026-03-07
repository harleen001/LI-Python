import streamlit as st
import pandas as pd
import plotly.express as px


#in plotly you can simply use dataframe in text =

st.set_page_config(layout="wide")

df = pd.read_csv("superstore.csv")
st.title("Supermarket Dashboard")

col1, col2 = st.columns([3, 1]) 

with col2:
    category = st.selectbox("Select Category", options=df['Category'].unique())
    sub_df = df[df['Category'] == category]
    
    selected_subs = []
    st.write("Select Sub-Categories:")
    for sub in sub_df['Sub-Category'].unique():
        if st.checkbox(sub, key=sub, value=True):
            selected_subs.append(sub)

filtered_df = df[(df['Category'] == category) & (df['Sub-Category'].isin(selected_subs))].head(10).copy()


with col1:
    col1A, col1B = st.columns(2)
    
    with col1A:
        st.subheader("Sales")
        fig_sales = px.area(filtered_df, x="Product Name", y="Sales", text=filtered_df['Sales'],color_discrete_sequence=['#0000FF'])
        fig_sales.update_traces(texttemplate='%{text:.2s}', textposition='top center')
        st.plotly_chart(fig_sales, use_container_width=True)
        
        
        st.subheader("Profit")
        fig_profit = px.line(filtered_df, x="Product Name", y="Profit", text=filtered_df['Profit'],color_discrete_sequence=['#008000'])
        fig_profit.update_traces(texttemplate='%{text:.2s}', textposition='top center')
        st.plotly_chart(fig_profit, use_container_width=True)
    
    with col1B:
        st.subheader("Discount")
        fig_disc = px.bar(filtered_df, x="Product Name", y="Discount", text=filtered_df['Discount'],color_discrete_sequence=['#FFFF00'])
        fig_disc.update_traces(texttemplate='%{text:.2f}', textposition='outside')
        st.plotly_chart(fig_disc, use_container_width=True)

st.markdown("""
    <style>
    .block-container { padding-top: 2rem; }
    </style>
    """, unsafe_allow_html=True)