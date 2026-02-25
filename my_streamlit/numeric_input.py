import streamlit as st


#box input
number = st.number_input("Insert a number")
st.write("The current number is ", number)


#slider input
age = st.slider("How old are you?", 0, 130, 25)
st.write("I'm ", age, "years old")