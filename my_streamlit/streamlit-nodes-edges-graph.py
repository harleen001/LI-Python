import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config

st.title("Network Graph Example")
nodes = []
nodes.append(Node(id="Alice", label="Alice", size=25, color="#FF4B4B")) 
nodes.append(Node(id="Bob", label="Bob", size=25, color="#1C83E1"))
nodes.append(Node(id="Charlie", label="Charlie", size=25, color="#00C092"))

edges = []
edges.append(Edge(source="Alice", target="Bob", label="friends"))
edges.append(Edge(source="Bob", target="Charlie", label="works with"))
edges.append(Edge(source="Charlie", target="Alice", label="follows"))

config = Config(
    width=800,
    height=500,
    directed=True, 
    physics=True, 
    hierarchical=False,
    # **kwargs for more Vis.js options
)

# 4. Render the Graph
return_value = agraph(nodes=nodes, edges=edges, config=config)

if return_value:
    st.write(f"You clicked on: **{return_value}**")