# app.py
import streamlit as st
from datetime import datetime

# Function to determine the zodiac sign based on the date
def get_zodiac_sign(day, month):
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    else:
        return "Invalid Date"

# Streamlit app
st.title("Zodiac Sign Finder")

# Date picker for user input
date_of_birth = st.date_input("Enter your Date of Birth", value=datetime(2000, 1, 1))

# Extract day and month
day = date_of_birth.day
month = date_of_birth.month

# Get the zodiac sign
zodiac_sign = get_zodiac_sign(day, month)

# Display the result
st.write(f"Your Zodiac Sign is: **{zodiac_sign}**")
