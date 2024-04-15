from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

# os.environ["OPEN_API_KEY"] = os.getenv("OPENAI_API_KEY")
## Langsmith tracking --> Does not work for conda environments
# os.environ["LANGCHAIN_TRACKING_V2"] ="true"
# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
## Conda Environments --> conda env config vars set LANGCHAIN_TRACKING_V2=true LANGCHAIN_API_KEY=your_api_key in shell first
# conda env config vars list -n my_env

# export LANGCHAIN_TRACKING_V2=true
# export LANGCHAIN_API_KEY=your_api_key
# to list environmental variables: printenv


## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries"),
        ("user", "Question: {question}")
    ]
)

## streamlit framework
st.title('Langchain Demo With LLAMA2 API')
input_text = st.text_input("Search the topic u want")

# ollama Llama2 LLM
llm = Ollama(model = "llama2:70b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))