import streamlit as st
import requests

backend_url = "http://localhost:8000/ask"

st.set_page_config(page_title="AI mental health therapist", layout="wide")
st.title("AI Mental Health Therapist")

if"chat_history" not in st.session_state:
    st.session_state.chat_history = []
    
    
user_input=st.chat_input("what's on your mind today?")
if user_input:
    st.session_state.chat_history.append({"role":"User","content":user_input})  
    
fixed_reasponse_from_backend=requests.post(backend_url, json={"message":user_input})     

st.session_state.chat_history.append({"role":"AI","content":fixed_reasponse_from_backend.json()})

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
        
       