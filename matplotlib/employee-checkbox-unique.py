import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("employee.csv")
df.columns = df.columns.str.strip()
col_job = 'Job'
st.title("Dynamic Job Distribution")
col_left, col_right = st.columns([3, 1]) 

with col_right:
    st.write("### Filter Jobs")
    jobs = sorted(df[col_job].unique())
    selected_jobs = []
    
    for job in jobs:
        if st.checkbox(job, value=False): 
            selected_jobs.append(job)
with col_left:
    filtered_df = df[df[col_job].isin(selected_jobs)]
    
    if not filtered_df.empty:
        fig = px.pie(
            filtered_df, 
            names=col_job, 
            title=f"Employee Count for {', '.join(selected_jobs)}",
            hole=0.4 
        )
        fig.update_traces(
            textinfo='label+value',
            textfont_size=16
        )
        
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Check a job on the right to see the pie chart count.")