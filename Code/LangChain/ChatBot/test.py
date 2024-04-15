from langsmith import Client
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACKING_V2"] ="true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
print(os.getenv("LANGCHAIN_API_KEY"))
# client = Client()

# url = next(client.list_runs(project_name="Default")).url
# print(url)