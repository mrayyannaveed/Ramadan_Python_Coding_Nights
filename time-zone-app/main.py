import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

TIME_ZONES = [
    "UTC",
    "Asia/Karachi",
    "America/New_York",
    "Europe/London",
    "Asia/Tokyo",
    "Australia/Sydney",
    "America/Los_Angeles",
    "Europe/Berlin",
    "Asia/Dubai",
    "Asia/Kolkata"
]

st.set_page_config(page_title="Time Zone App", page_icon="🕰️")

st.title("TIME ZONE APP")
st.write("This app displays the current time in different time zones.")

selected_time_zones = st.multiselect("Select Time Zones", TIME_ZONES, default=["UTC", "Asia/Karachi"])

st.subheader("Current Time in Selected Time Zones")

for tz in selected_time_zones:
    current_time = datetime.now(ZoneInfo(tz)).strftime("%Y-%m-%d %I %H:%M:%S %p") 
    st.write(f"**{tz}**: {current_time}")  

st.subheader("Convert Time Between Timezones")

current_time = st.time_input("Current Time", value=datetime.now().time())

from_tz = st.selectbox("From Timezone", TIME_ZONES, index=0)

to_tz = st.selectbox("To Timezone", TIME_ZONES, index=1)

if st.button("Convert Time"):
    dt = datetime.combine(datetime.today(), current_time, tzinfo = ZoneInfo(from_tz))

    converted_time = dt.astimezone(ZoneInfo(to_tz)).strftime("%Y-%m-%d %I %H:%M:%S %p")

    st.success(f"Converted Time in {to_tz}: {converted_time}")
