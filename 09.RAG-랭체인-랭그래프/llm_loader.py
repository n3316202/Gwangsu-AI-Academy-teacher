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

def init_custom_llm(temperature: float= 0.1, max_tokens:int = 1000):
    """지정된 환경변수 모델로 LLM을 초기화합니다."""
    model_name = os.getenv("LLM_AI_MODEL")
    print("모델이름",model_name)

    if not model_name:
        raise ValueError("환경변수 'LLM_AI_MODEL'이 설정되지 않았습니다.")

    return init_chat_model(
        model_name,
        temperature=temperature,
        max_tokens=max_tokens
    )
    