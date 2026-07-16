from dotenv import load_dotenv
from typing import TypedDict

from langgraph.graph import (
    StateGraph,
    START,
    END
)

import os

# ==========================
# 환경변수
# ==========================

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))

from llm_loader import init_custom_llm

llm = init_custom_llm()

from langchain_core.tools import tool
from  datetime import datetime

@tool
def age(birth_year):
    """
    출생연도를 입력받아 현재 나이를 계산합니다.
    """    
    current_year = datetime.now().year
    
    return current_year - birth_year

# result = age.invoke(
#     {
#         "birth_year":2000
#     }
# )
# print(result)
# print(age.name)
# print(age.description)

from langchain.agents import create_agent

agent = create_agent(
    model=llm,
    tools=[age],
    system_prompt="""
    당신은 친절한 AI 비서입니다.

    필요하면 Tool을 사용하여 답변하세요.
    """
)
from langchain_core.messages import  HumanMessage, SystemMessage

result = agent.invoke(
    {
        "messages":[HumanMessage(content="2000년생 나이는?")]
    }
)

print(result["messages"][-1].content)
print("="*50)
print(result)

