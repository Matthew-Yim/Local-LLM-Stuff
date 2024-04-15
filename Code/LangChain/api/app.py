# To Run application shell>: python app.py
    # localhost:8000 --> results in error
    # localhost:8000/docs --> results in informational page

from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes # Route to different LLMs to use
import uvicorn
import os
from langchain_community.llms import Ollama 
from dotenv import load_dotenv

load_dotenv()

# os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title = "Langchain Server",
    version = "1.0",
    description = "A simple API Server"
)

# add_routes(
#     app,
#     ChatOpenAI(),
#     path = "/openai"
# )

# model = ChatOpenAI()
## Ollama llama2
llm = Ollama(model="llama2:70b")

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 1000 words")
prompt2 = ChatPromptTemplate.from_template("Write me an poem about {topic} with 1000 words")

# add_routes(
#     app,
#     prompt1|model,
#     path = "/essay" # This path is responsible for interfacing with OpenAI the endpoint basically
# )

add_routes(
    app,
    prompt2|llm,
    path = "/poem" # This path is responsible for interfacing with OpenAI the endpoint basically
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)