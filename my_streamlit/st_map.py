import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(
    rng(0).standard_normal((10, 2)) / [50, 50] + [31.3171033,75.5839436],
    columns=["lat", "lon"],
)

st.map(df)