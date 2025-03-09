import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters # uppercase and lowercase letters

    if use_digits:
        characters += string.digits # add digits

    if use_special:
        characters += string.punctuation # add special characters

    return ''.join(random.choice(characters) for _ in range(length))

st.title("Password Generator")

length = st.slider("Select Your Password Length", min_value=8, max_value=24, value=12)

use_digits = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"Generated Password: `{password}`")

st.write("---------------------------------------")
st.write("Build with ❤️ by [Muhammad Rayyan Naveed]")

