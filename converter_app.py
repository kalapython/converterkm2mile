import streamlit as st

# Title of the app
st.title("Kilometer to Mile Converter")

# Input field for the user
km = st.number_input("Enter distance in kilometers:", min_value=0.0, step=0.1)

# Conversion function
def km_to_miles(km):
    return km * 0.621371

# Button to convert
if st.button("Convert"):
    miles = km_to_miles(km)
    st.success(f"{km} km is equal to {miles:.2f} miles.")
