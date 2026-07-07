#  메모리 관리에서 가장 중요한 부분
# **"왜 RunnableWithMessageHistory를 사용하는가?"**를 이해하는 것이 목표
# 흐름은 반드시 아래처럼 진행하는 것을 추천
# 직접 저장 → 불편함 → RunnableWithMessageHistory → 자동 저장

# 예제 1. 직접 저장하는 방식 (복습)
# history.add_user_message(question)
# response = llm.invoke(history.messages)
# history.add_ai_message(response.content)
# 질문
# "매번 이 세 줄을 써야 할까요?"
# 답
# 너무 불편하다.

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
import sys
from pathlib import Path
import os
from langchain_core.prompts import MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

sys.path.append(str(Path(__file__).resolve().parent.parent))
from llm_loader import init_custom_llm


llm = init_custom_llm()
