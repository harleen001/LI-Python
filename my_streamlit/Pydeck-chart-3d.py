import pandas as pd
import pydeck as pdk
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(
    rng(0).standard_normal((100, 2)) / [50, 50] + [31.3171033,75.5839436],
    columns=["lat", "lon"],
)

st.pydeck_chart(
    pdk.Deck(
        map_style=None,initial_view_state=pdk.ViewState(latitude=31.3171033,longitude=75.5839436,zoom=11,pitch=50,
        ),
        layers=[
            pdk.Layer(
                "HexagonLayer",data=df,get_position="[lon, lat]",
                radius=200,elevation_scale=24,
                elevation_range=[0, 10],pickable=True,extruded=True,
            ),
            pdk.Layer(
                "ScatterplotLayer",data=df,get_position="[lon, lat]",get_color="[200, 30, 0, 160]",get_radius=200,
            ),
        ],
    )
)