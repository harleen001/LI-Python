import streamlit as st
import numpy as np

with st.container():
    st.write("This is inside the container")
    st.bar_chart(np.random.randn(50, 3))
st.write("This is outside the container")


container = st.container(border=True)
container.write("This is inside the container")
st.write("This is outside the container")

container.write("This is inside too")



#grid layout with column
row1 = st.columns(3)
row2 = st.columns(3)

for col in row1 + row2:
    tile = col.container(height=120)
    tile.title(":balloon:")

#scrolling container
long_text = "Lorem ipsum. " * 1000

with st.container(height=300):
    st.markdown(long_text)

#right aligned cards container
flex = st.container(horizontal=True, horizontal_alignment="right")

for card in range(3):
    flex.button(f"Button {card + 1}")