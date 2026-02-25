import streamlit as st

st.title("Registration Form",text_alignment="center")

with st.form("registration_form"):
    
    c1, c2 = st.columns([1, 3])
    name = c2.text_input("Username", label_visibility="collapsed")
    c1.text("Username")


    c3, c4 = st.columns([1, 3])
    password = c4.text_input("Password", type="password", label_visibility="collapsed")
    c3.text("Password")

    c5, c6 = st.columns([1, 3])
    password2 = c6.text_input("Retype Password", type="password", label_visibility="collapsed")
    c5.text("Confirm Password")
    
    c7, c8 = st.columns([1, 3])
    gender = c8.radio("Gender", ["Male", "Female"], label_visibility="collapsed", horizontal=True)
    c7.text("Gender")

    c9, c10 = st.columns([1, 3])
    correspondance = c10.text_area("Correspondance", label_visibility="collapsed")
    c9.text("Correspondance")

    c11, c12 = st.columns([1, 3])
    mobile = c12.number_input("Mobile Number", label_visibility="collapsed")
    c11.text("Mobile")

    c13, c14 = st.columns([1, 3])
    pin = c14.number_input("Pin Code", label_visibility="collapsed")
    c13.text("Pin Code")

    c15, c16 = st.columns([1, 3])
    c15.text("Interests")
    selection = c16.multiselect("Interests", ("Painting", "Reading", "Singing", "Dancing"), label_visibility="collapsed")

    c17, c18 = st.columns([1, 3])
    dob = c18.date_input("Date of Birth", label_visibility="collapsed")
    c17.text("  DOB")

    submit_button = st.form_submit_button("Submit")

if submit_button:
       st.write("Username = ",name," \nPassword = ",password," \nGender = ",gender," \nCorrespondance = ",correspondance,
             " \nMobile No = ",mobile, " \nPincode = ",pin," \nInterest = ", ", ".join(selection)," \nDate of Birth = ",dob)