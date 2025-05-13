import os
import streamlit as st
import streamlit_chat
from streamlit_chat import message
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

ai_model=Groq(api_key=os.getenv("groq_api"))


global prompt
st.title("Mechanical Workshop")

def get_initial_message():
    messages=[
        {"role":"system","content":"You are my Mechanical Workshop Assistant"},
        {"role":"user","content":"Hello"}

    ]
    return messages
def get_chatbot_response(messages):
    response=ai_model.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages
          )
     
    return response.choices[0].message.content
def update_chat(messages,role,content):
    messages.append({"role":role,"content":content})
    return messages
if 'generated' not in st.session_state:
    st.session_state['generated']=[]

if 'past' not in st.session_state:
    st.session_state['past']=[]

if 'messages' not in st.session_state:
    st.session_state['messages']= get_initial_message()

prompt=st.text_input("How may I help You?", key="input")

if prompt:
    with st.spinner('generating.....'):
        messages= st.session_state['messages']
        messages=update_chat(messages,"user",prompt)
        response=get_chatbot_response(messages)
        messages=update_chat(messages,"assistant",response)
        st.session_state.past.append(prompt)
        st.session_state.generated.append(response)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1,-1,-1):
        message(st.session_state['past'][i], is_user=True, key=str(i)+  '_user' )
        message(st.session_state["generated"][i], key=str(i))