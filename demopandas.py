import streamlit as st
import pandas as pd

students={
    "Name":["Kiran","Rohit","Mohit","Pawan","Suri"],
    "Rollno":[1,2,3,4,5],
    "Age":[21,23,22,19,21]
}

df=pd.DataFrame(students)

st.dataframe(df)