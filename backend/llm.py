import os, json
from dotenv import load_dotenv
import httpx
from langchain_openai import AzureChatOpenAI

load_dotenv()
client = httpx.Client(verify=False)
llm = AzureChatOpenAI(
    model = "gpt-4",
    azure_endpoint = os.getenv("AZURE_OPENAI_GPT_4_ENDPOINT"),
    openai_api_version = os.getenv("AZURE_OPENAI_GPT_4_VERSION"),
    deployment_name = os.getenv("AZURE_OPENAI_GPT_4_DEPLOYMENT_NAME"),
    openai_api_key = os.getenv("AZURE_OPENAI_GPT_4_API_KEY"),
    openai_api_type = "azure",
    temperature = 0.1,
    max_tokens = 1000,
    http_client = client,
)