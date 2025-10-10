st.image("shaftesbury_logo.png", width=150)
import streamlit as st
import pandas as pd

# Load the Excel file
df = pd.read_excel("Free rooms Oct25.xlsx", engine="openpyxl")

# Extract all period columns
period_columns = df.columns[1:]

# Streamlit UI
st.title("Shaftesbury School Free Room Checker")
selected_periods = st.multiselect("Select one or more periods:", period_columns)

if selected_periods:
    # Filter rooms that are 'Available' in all selected periods
    filtered_df = df[df[selected_periods].apply(lambda row: all(cell == "Available" for cell in row), axis=1)]
    st.subheader("Available Rooms")
    st.write(filtered_df[["Room"] + selected_periods])
else:
    st.info("Please select at least one period to see available rooms.")
