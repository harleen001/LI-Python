import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Page Config
st.set_page_config(page_title="Employee Data Visualizer", layout="wide")

# 2. Load Data
df = pd.read_csv("employee.csv")

# 3. NORMALIZE COLUMNS (This is the most important part)
# This removes spaces and makes everything lowercase for easy coding
df.columns = df.columns.str.strip().str.lower()

# Map the expected columns to the lowercase versions for Plotly
# Based on your input: Empid, Ename, Job, Salary, Comm, Deptno
col_ename = 'ename'
col_salary = 'salary'
col_job = 'job'
col_dept = 'deptno'

# 4. SIDEBAR DROPDOWN
st.sidebar.header("Filter Data")

if col_job in df.columns:
    # Get unique jobs and sort them
    unique_jobs = sorted(df[col_job].unique().tolist())
    options = ["All Jobs"] + unique_jobs
    
    # This line creates the actual dropdown menu
    selected_job = st.sidebar.selectbox("Select a Job Title:", options)
else:
    st.error(f"Could not find a 'Job' column. Available columns are: {list(df.columns)}")
    st.stop()

# 5. FILTER LOGIC
if selected_job == "All Jobs":
    filtered_df = df
else:
    filtered_df = df[df[col_job] == selected_job]

# 6. DASHBOARD DISPLAY
st.title(f"Visualizing: {selected_job}")

# Metric summary
total_sal = filtered_df[col_salary].sum()
st.metric(label="Total Salary for Selection", value=f"${total_sal:,.2f}")

# Bar Chart
fig = px.bar(
    filtered_df,
    x=col_ename,
    y=col_salary,
    color=col_dept,
    hover_data=['empid', 'comm'],
    title=f"Salary Comparison for {selected_job}",
    template="plotly_white",
    color_continuous_scale="RdBu"
)

# Render the chart
st.plotly_chart(fig, use_container_width=True)

# 7. DATA PREVIEW
with st.expander("Show Data Table"):
    st.write(filtered_df)