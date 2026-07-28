import streamlit as st

from dotenv import load_dotenv

from langchain.chat_models import init_chat_model
import sys
from pathlib import Path
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages

sys.path.append(
    str(Path(__file__).resolve().parent)
)
from llm_loader import init_custom_llm

llm = init_custom_llm()

st.title("챗봇 실습")


#출력 위치를 먼저 확보
chat_area = st.container()

# 입력창을 위에 배치
question = st.text_input("질문하세요")

# ┌──────────────────────────────┐
# │                              │
# │  chat_area                   │
# │  (아직 내용 없음)             │
# │                              │
# ├──────────────────────────────┤
# │ 질문하세요                    │
# │ ┌──────────────────────────┐ │
# │ │파이썬이 뭐야               │ │
# │ └──────────────────────────┘ │
# └──────────────────────────────┘

#  👤  파이썬이 뭐야?  
# ┌──────────────────────────────┐
# │                              │
# │  👤                     │
# │  ┌────────────────────────┐  │
# │  │ 파이썬이 뭐야?           │  │
# │  └────────────────────────┘  │
# │                              │
# ├──────────────────────────────┤
# │ 질문하세요                    │
# │ ┌──────────────────────────┐ │
# │ │ 파이썬이 뭐야?            │ │
# │ └──────────────────────────┘ │
# └──────────────────────────────┘

if question:
    with chat_area:
        with st.chat_message("user", avatar="🙂"):
            st.write(question)

        respose = llm.invoke(question)

        with st.chat_message("assistant"):
            st.write(respose.content)

# ┌──────────────────────────────┐
# │                              │
# │ 👤 user                      │
# │ ┌──────────────────────────┐ │
# │ │ 파이썬이 뭐야?             │ │
# │ └──────────────────────────┘ │
# │                              │
# │ 🤖 assistant                 │
# │ ┌──────────────────────────┐ │
# │ │ 파이썬은 프로그래밍       │ │
# │ │ 언어입니다.               │ │
# │ └──────────────────────────┘ │
# │                              │
# ├──────────────────────────────┤
# │ 질문하세요                    │
# │ ┌──────────────────────────┐ │
# │ │                          │ │
# │ └──────────────────────────┘ │


# 핵심정리
# st.chat_input()	채팅 입력창 생성
# st.chat_message()	채팅 말풍선 생성
# st.write()
# 화면에 출력