
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
import sys
from pathlib import Path
import os

sys.path.append(str(Path(__file__).resolve().parent.parent))
from llm_loader import init_custom_llm

# 템플릿 사용

llm = init_custom_llm()

# 첫번째 질문
response = llm.invoke("안녕하세요, 제이름은 홍길동 입니다.")
print("응답1", response.content)

# 두번째 질문
response = llm.invoke("제 이름은 뭐였죠")
print("응답2", response.content)