import streamlit as st
import graphviz

st.graphviz_chart('''
    digraph {
        grandfather -> father
        grandfather -> uncle
        uncle -> brother
        father -> me
    }
''')