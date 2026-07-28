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

question = st.text_input("질문하세요")

if question:

    respose = llm.invoke(question)

    st.write(respose.content)