# llm_loader.py
import langchain
import langchain_openai
from langchain.chat_models import init_chat_model

import os
from pathlib import Path
from dotenv import load_dotenv

print(langchain.__version__)
print(langchain_openai.__version__)

env_path = Path(__file__).resolve().parent / ".env"
print("llm_loader 위치:", Path(__file__).resolve())
print(".env 위치:", env_path)

load_dotenv(env_path)
