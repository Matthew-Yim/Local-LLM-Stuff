# Keep in mind that {python app.py} has to be executed first to establish the langserver which
    # the client.py (User interface) calls, basically langserver is the API and client.py is the UI and can make calls to the API
import requests
import streamlit as st

def get_openai_response(input_text):
    response = requests.post("http://localhost:8000/essay/invoke", 
                             json = {'input':{'topic':input_text}})

    return response.json()['output']['content']

def get_ollama_response(input_text):
    response = requests.post("http://localhost:8000/poem/invoke", 
                             json = {'input':{'topic':input_text}})

    return response.json()['output']

# StreamLit Framework

st.title('LangChain Demo with LLAMA2 API')
input_text = st.text_input("Write an essay on")
input_text1 = st.text_input("Write a poem on")

if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))