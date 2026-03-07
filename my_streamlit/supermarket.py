import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# --- CUSTOM CSS FOR RESPONSIVE SWAP ---
st.markdown("""
    <style>
    /* Desktop: Keep standard row layout */
    [data-testid="stHorizontalBlock"] {
        display: flex;
        flex-direction: row;
    }

    /* Mobile: Swap the vertical stack order */
    @media (max-width: 768px) {
        [data-testid="stHorizontalBlock"] {
            flex-direction: column-reverse !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)


df = pd.read_csv("superstore.csv")
st.title("Supermarket Dashboard")


col1, col2 = st.columns([3, 1])

with st.sidebar: 
    category_list = df['Category'].unique()

with col1:
    chart_container = st.container()
with col2:
    st.subheader("Filters")
    selected_cat = st.selectbox("Select Category", options=category_list)
    sub_df = df[df['Category'] == selected_cat]
    
    selected_subs = []
    st.write("Select Sub-Categories:")
    for sub in sub_df['Sub-Category'].unique():
        if st.checkbox(sub, key=sub, value=True):
            selected_subs.append(sub)

filtered_df = df[(df['Category'] == selected_cat) & (df['Sub-Category'].isin(selected_subs))].head(10).copy()

with chart_container:
    col1A, col1B = st.columns(2)
    with col1A:
        st.subheader("Sales")
        fig_sales = px.area(filtered_df, y="Sales", text="Sales", color_discrete_sequence=['blue'])
        fig_sales.update_traces(texttemplate='%{text:.2s}', textposition='top center', mode="lines+markers+text")
        st.plotly_chart(fig_sales, use_container_width=True)

        st.subheader("Profit")
        fig_profit = px.line(filtered_df, y="Profit", text="Profit", color_discrete_sequence=['green'])
        fig_profit.update_traces(texttemplate='%{text:.2s}', textposition='top center', mode="lines+markers+text")
        st.plotly_chart(fig_profit, use_container_width=True)

    with col1B:
        st.subheader("Discount")
        fig_disc = px.bar(filtered_df, y="Discount", text="Discount", color_discrete_sequence=['yellow'])
        fig_disc.update_traces(texttemplate='%{text:.2f}', textposition='outside')
        st.plotly_chart(fig_disc, use_container_width=True)