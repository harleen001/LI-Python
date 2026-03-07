import pandas as pd
import json
import streamlit as st

st.title("State Wise Population")

df =pd.read_csv('state_wise_population_2019.csv')
with open("india_states.geojson", "r", encoding="utf-8") as f:
    india_states = json.load(f)

with open("dist.geojson", "r", encoding="utf-8") as f:
    india_dist = json.load(f)