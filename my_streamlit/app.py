import streamlit as st

st.title("# Welcome",text_alignment="center")
st.header("My First Page")
st.subheader("My title")
st.markdown("## Weldone")
st.badge("New")
st.badge("Success", icon="🥺", color="green")

name=st.text_input("Enter your name")
password=st.text_input("enter your password",type="password")
rollno=st.text_input("Enter your rollno")
address=st.text_area("Address")
if st.button("submit"):
    st.write("username=",name, " \nRollno=",rollno," \nPassword",password," \nAddress",address)


options = st.multiselect(
    "What are your favorite colors?",
    ["Green", "Yellow", "Red", "Blue"],
    default=["Yellow", "Red"],
)

st.write("You selected:", options)


st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")

with st.container(horizontal=True, horizontal_alignment="distribute"):
    "`A`" if st.button("A", shortcut="A") else "` `"
    "`S`" if st.button("S", shortcut="Ctrl+S") else "` `"
    "`D`" if st.button("D", shortcut="Cmd+Shift+D") else "` `"
    "`F`" if st.button("F", shortcut="Mod+Alt+Shift+F") else "` `"