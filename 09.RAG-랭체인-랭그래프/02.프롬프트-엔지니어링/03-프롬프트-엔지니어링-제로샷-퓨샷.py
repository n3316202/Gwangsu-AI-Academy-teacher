
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from openai import OpenAI


# 제로샷
# 예시 없음
# ↓
# 모델이 바로 답변
# Zero-shot (예시 없음)
# AI가 기준 없이 바로 답변 생성

prompt = """
다음 문장을 영어로 번역하세요.

나는 오늘 학교에 갔다.
"""



import sys
from pathlib import Path
import os

sys.path.append(str(Path(__file__).resolve().parent.parent))
from llm_loader import init_custom_llm

print(init_custom_llm)

llm = init_custom_llm()
respose = llm.invoke(prompt)

print(respose.content)



