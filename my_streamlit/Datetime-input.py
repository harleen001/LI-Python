import datetime
import streamlit as st

d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
st.write("Your birthday is:", d)    #simple date input

#date range input from - to

today = datetime.datetime.now()
next_year = today.year + 1
jan_1 = datetime.date(next_year, 1, 1)
dec_31 = datetime.date(next_year, 12, 31)

d = st.date_input(
    "Select your vacation for next year",
    (jan_1, datetime.date(next_year, 1, 7)),
    jan_1,
    dec_31,
    format="MM.DD.YYYY",
)
d


#empty to input

d = st.date_input("When's your birthday", value=None)
st.write("Your birthday is:", d)


#date with time
event_time = st.datetime_input(
    "Schedule your event",
    datetime.datetime(2025, 11, 19, 16, 45),
)
st.write("Event scheduled for", event_time)


#only time input
t = st.time_input("Set an alarm for", datetime.time(8, 45))
st.write("Alarm is set for", t)