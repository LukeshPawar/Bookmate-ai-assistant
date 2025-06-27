# Bookmate-ai-assistant
BookMate is a conversational AI assistant that helps users check calendar availability and schedule events using Google Calendar. It integrates a LangGraph-style message processor, FastAPI backend, Streamlit frontend, and the Google Calendar API.

## 🚀 Features

- 🤖 Conversational assistant to check and book time slots
- 📅 Real-time Google Calendar integration
- 🧠 Smart intent handling using LangGraph-style logic
- ⚙️ FastAPI backend with clean REST endpoint
- 🌐 Streamlit frontend with chat UI
- 🔒 OAuth2 secure authentication with Google


## 🛠️ Tech Stack

- **Backend:** Python, FastAPI  
- **Frontend:** Streamlit  
- **Calendar:** Google Calendar API (OAuth2)  
- **AI Flow:** LangGraph (rule-based for this version)  
- **Others:** Uvicorn, OpenAI (optional), Requests

## 📁 Project Structure

bookmate/
├── main.py # FastAPI backend entry
├── agent.py # Message parsing and routing logic
├── calendar_api.py # Google Calendar authentication & booking
├── streamlit_app.py # Streamlit UI interface
├── requirements.txt # Dependencies list
├── .gitignore # Ignored files (credentials, cache)
├── README.md # You're reading it!
