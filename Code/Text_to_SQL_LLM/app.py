# Agenda -> Text to SQL LLM Application
# Prompt --> LLM --> llama2 --> Query --> SQL DB --> Response

# Implementation
#   1. SQLlite --> Insert some records --> python code
#   2. LLM App --> llama2 --> SQL DB

from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3

## Configure our API key Sample for google
# import google.generativeai as genai
# genai.configure(api_key=os.getenv("Google_API_KEY"))

    # Function to Load Google Gemini Model and provide sql query as response
    # def get_gemini_response(question, prompt):
    #   model = genai.GenerativeModel('gemini-pro')
    #   response = model.generate_content([prompt, question])
    #   return response.text

# Function to retrieve query from the sql database
def read_sql_query(sql, db):
  connection = sqlite3.connect(db)
  cursor = connection.cursor()
  cursor.execute(sql)
  rows = cursor.fetchall()
  connection.commit()
  connection.close()
  for row in rows:
      print(row)
  return rows

# Define your prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION, and GRADES \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """
]

## Streamlit App
st.set_page_config(page_title="Retrieve SQL query")
st.header("Llama2 App to Retrieve SQL Data")
question = st.text_input("Input: ", key="input")
submit=st.button("ASk the question") 

# if submit is clicked
if submit:
    response = get_llama_response(question, prompt)
    print(response)
    data = read_sql_query(response, "student.db")
    st.subheader("The response is")
    for row in response:
       print(row)
       st.header(row)