import os
import streamlit as st
import streamlit_chat
from streamlit_chat import message
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
query=input("Enter Your Desired Question:")
ai_model=Groq(api_key=os.getenv("groq_api"))
response=ai_model.chat.completions.create(
    messages=[
        {"role":"system","content":"You are my Mechanical Workshop Assistant"},
        {"role":"user","content":query}

    ], model="llama-3.3-70b-versatile"
)
print(response.choices[0].message.content)