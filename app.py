
import streamlit as st
import pandas as pd

st.image("Shaftesbury logo.png", width=150)

# Load the Excel file
df = pd.read_excel("Free rooms Oct25.xlsx", engine="openpyxl")

# Extract all period columns
period_columns = df.columns[1:]

# Streamlit UI
st.title("Free Room Checker")
selected_periods = st.multiselect("Select one or more periods:", period_columns)

if selected_periods:
    # Filter rooms that are 'Available' in all selected periods
    filtered_df = df[df[selected_periods].apply(lambda row: all(cell == "Available" for cell in row), axis=1)]
    st.subheader("Available Rooms")
    st.write(filtered_df[["Room"] + selected_periods])
else:
    st.info("Please select at least one period to see available rooms.")


import streamlit as st

warning_message = """
- **Instructions for students:**
    - Staff may be using a room for lesson preparation
    - If the teacher requests the room or it is used for a cover class, please respect this and find somewhere else to work  
    - Strictly no eating  
    - Quiet study only  
    - Rooms left as you found them (tidy!)  
    - Behaviour must be impeccable at all times  
    - If students misuse a school space, they are liable to be sanctioned in accordance with the school behaviour policy  
    - Where ongoing concerns occur, the room will be removed from the free rooms list  
"""

st.markdown(warning_message)

st.markdown("*Room data accurate as of 13/10/2025*")
