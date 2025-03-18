import streamlit as st
import random
import time
import requests

st.set_page_config(
    page_title="Money Making Machine",
    page_icon="💰",
    layout="wide"
)
st.title("Money Making Machine")

def generate_money():
    return random.randint(1, 1000)

st.subheader("Money Generating Machine!")
if st.button("Generate Money"):
    st.write("Generating your money...")
    time.sleep(1)
    amount = generate_money()
    st.success(f"You generated ${amount}!")


def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustle?apiKey=123456")
        if response.status_code == 200:
            hustles = response.json()
            return hustles["side_hustle"]
        else:
            return ("Freelancing")
    except:
        return ("Something went wrong!")

st.subheader("📓Side Hustle Ideas")
if st.button("Generate Hustle"):
    idea = fetch_side_hustle()
    st.success(idea)


def fetch_money_qoute():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes?apiKey=123456")
        if response.status_code == 200:
            qoutes = response.json()
            return qoutes["money_qoutes"]
        else:
            return ("The best way to predict the future is to invent it")
    except:
        return ("Something went wrong!")
    
st.subheader("💲Money Making Qoutes")
if st.button("Generate Wonderful Inspiring Qoute"):
    qoute = fetch_money_qoute()
    st.info(qoute)