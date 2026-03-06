import streamlit as st
import pandas as pd
import plotly.express as px
import json

st.title("State And District Population Dashboard")

# Read CSV
df = pd.read_csv("State_district_combined.csv", encoding="latin1")

# Load GeoJSON files
with open("india_states.geojson", "r", encoding="utf-8") as f:
    india_states = json.load(f)

with open("dist.geojson", "r", encoding="utf-8") as f:
    india_dist = json.load(f)

# Sidebar
st.sidebar.header("Customization Options")
show_borders = st.sidebar.checkbox("Show District Borders in State Map", value=True)
border_color = st.sidebar.color_picker("Select District Border Color", "#FF0000")

# State and District selection
col1, col2 = st.columns(2)

with col1:
    state = st.selectbox('Select a State:', df['State'].unique())

with col2:
    # If no state is selected, show all districts
    if state:
        district_list = df[df['State'] == state]['District'].unique().tolist()
    else:
        district_list = df['District'].unique().tolist()
    district = st.multiselect("Select the District:", district_list)

# Show State Map
col3, col4 = st.columns(2)
with col3:
    state_df = df[df['State']==state].copy() if state else df.copy()
    state_df['value'] = state_df['total_population']

    fig = px.choropleth(
        state_df,
        geojson=india_states,
        featureidkey="properties.ST_NM",
        locations="State",
        color="value",
        color_continuous_scale="Plasma",
        title=f"Selected State - {state}",
        hover_data={
            "total_population": True,
            "population_male": True,
            "population_female": True
        }
    )

    # Add district borders if needed
    if show_borders and district:
        district_df = df[df['District'].isin(district)].copy()
        district_df['highlight'] = 1

        border_layer = px.choropleth(
            district_df,
            geojson=india_dist,
            featureidkey="properties.district",
            locations="District",
            color_discrete_sequence=["rgba(0,0,0,0)"],
            hover_data={
                "Population": True,
                "Male": True,
                "Female": True
            }
        )

        for trace in border_layer.data:
            trace.update(marker_line_width=2, marker_line_color=border_color)
            fig.add_trace(trace)

    fig.update_geos(fitbounds="locations", visible=False)
    st.plotly_chart(fig, use_container_width=True)

# District Map
with col4:
    if district:
        district_df = df[df['District'].isin(district)].copy()
        district_df['value'] = district_df["Population"]

        fig_district = px.choropleth(
            district_df,
            geojson=india_dist,
            featureidkey="properties.district",
            locations="District",
            color="Population",
            color_continuous_scale='Viridis',
            title=f"Selected Districts - {', '.join(district)}",
            hover_data={
                "Population": True,
                "Male": True,
                "Female": True
            }
        )
        fig_district.update_geos(fitbounds="locations", visible=False)
        st.plotly_chart(fig_district, use_container_width=True)

