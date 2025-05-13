import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("groq_api")
ai_model = Groq(api_key=api_key)

# Set page layout
st.set_page_config(page_title="Mechanical Workshop Assistant", layout="centered")
st.title("🔧 Mechonics Workshop Assistant")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are my Mechanical Workshop Assistant. \
         You should know each and every thing about the workshop so that when the user ask anything you can answer it easily.\
         The workshop provides services such as Engine tuning,Oil change, Brake service, Wheel alignment, AC repair,Denting-painting,Diagnostic scan.\
         The wokshop  is located in lahore.\
         The workshop timing is from 9 am to 5 pm.\
         The workshop provides services for all sort of hybrid, electric and combustion engine cars.\
         For the pricing information call the workshop for the latest rates.\
         if anything other than the workshop is asked you must reply with I only assist you regarding the workshop. \
         The workshop owner is Muhammad Hamza. He is a brilliant Mechanical Engineer. \
         You can contact him on his business Email.\
         The Email is mechonics123@gmail.com.\
         The workshop name is Mechonics \
         Check the different service types for the type of engine before suggesting any. As oil change cannot be done in electric cars."},
         {"role":"user","content":"Hi!"},
        {"role": "assistant", "content": "Hello! How can I assist you in the workshop today?"}
    ]

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    elif msg["role"] == "assistant":
        with st.chat_message("assistant"):
            st.markdown(msg["content"])

# Chat input (only shows when Streamlit finishes displaying history)
user_prompt = st.chat_input("Type your question here...")

# Define response generation
def get_chatbot_response(message_list):
    response = ai_model.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=message_list
    )
    return response.choices[0].message.content

# Process user message
if user_prompt:
    # Show user's message
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    # Call chatbot and show typing spinner
    with st.chat_message("assistant"):
        with st.spinner("Assistant is typing..."):
            assistant_reply = get_chatbot_response(st.session_state.messages)
            st.markdown(assistant_reply)

    # Add assistant's reply to history
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
