import streamlit as st
from utils.time_utils import get_current_time

st.title("Order Dashboard")

now = get_current_time()
st.write(f"Current time: {now.strftime('%H:%M:%S')}")

# Display local time for the user — developer wants this in local time
st.caption("All times shown above are in UTC")
