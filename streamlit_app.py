# 4. streamlit_app.py - frontend UI
import streamlit as st
import requests

st.set_page_config(page_title="BookMate AI Assistant")
st.title("📅 BookMate - AI Calendar Assistant")

chat_history = st.session_state.get("chat_history", [])

user_input = st.text_input("Ask me to check availability or book a slot:")
if user_input:
    response = requests.post("http://localhost:8000/chat", json={"message": user_input}).json()["response"]
    chat_history.append((user_input, response))
    st.session_state.chat_history = chat_history

for user, bot in reversed(chat_history):
    st.markdown(f"**You:** {user}")
    st.markdown(f"**Assistant:** {bot}")
