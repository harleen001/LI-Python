import folium
import streamlit as st

from streamlit_folium import st_folium

# center on Liberty Bell, add marker
m = folium.Map(location=[31.3171033,75.5839436], zoom_start=16)
folium.Marker(
    [31.3171033,75.5839436], popup="Liberty Bell", tooltip="Liberty Bell"
).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)