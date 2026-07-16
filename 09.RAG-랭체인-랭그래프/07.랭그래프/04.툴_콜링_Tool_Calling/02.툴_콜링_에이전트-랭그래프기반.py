        #             ┌──────────────┐
        #             │    START     │
        #             └──────┬───────┘
        #                    │
        #                    │
        #                    ▼
        #             ┌──────────────┐
        #             │   chatbot    │
        #             └──────────────┘
        #                    ┆
        #                    ┆  tool_calls ?
        #                    ┆
        #           ┌────────┴────────┐
        #           ┆                 │
        #           ┆                 │
        #           ▼                 ▼
        #    ┌──────────────┐      ┌──────────────┐
        #    │  tool_node   │      │     END      │
        #    └──────┬───────┘      └──────────────┘
        #           │
        #           │
        #           ▼
        #    ┌──────────────┐
        #    │   chatbot    │
        #    └──────────────┘


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

@tool
def today():
    """
    오늘 날짜를 반환합니다.
    """   
    
    return  datetime.now().strftime("%Y-%m-%d")

@tool
def current_time():
    """
    현재 시간을 반환합니다.
    """   
    
    return  datetime.now().strftime("%H:%M:%S")

# 웹 검색
from langchain_community.tools import DuckDuckGoSearchResults

search = DuckDuckGoSearchResults(
    output_format="list", #"string", "list", "json" 
    max_results=5, # 검색 결과 갯수 
    backend="news", # 검색 종류 "text", "news", "images"
    region="kr-kr", # 검색 지역 "kr-kr", "us-en", "jp-jp", "wt-wt"
    timelimit="d" # 하루 # "d", "w", "m", "y"
)

@tool
def web_search(query):
    """
    인터넷 검색
    최신 정보 검색
    뉴스 검색
    주가 검색
    """
    try:
        result = search.invoke(query)
        
        if result:
            return result
        
    except Exception as e:
        return f"검색 실패 : {e}"

tools = [
    age,
    today,
    current_time,
    web_search
]

llm = llm.bind_tools(tools)

# =====================================================
# Tool Node
# =====================================================

from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode


class AgentState(TypedDict):
    messages: Annotated[list, add_messages]

# 챗봇 노드
def chatbot(state:AgentState):

    response = llm.invoke(state["messages"])

    # print(response)

    return {
        "messages":[response]
    }

# =====================================================
# Tool Node
# =====================================================

tool_node = ToolNode(tools)

# =====================================================
# Conditional Edge
# =====================================================
def should_continue(state:AgentState):
    last_message = state["messages"][-1]

    #print("라스트 메세지", last_message)

    # Tool 호출 여부 확인
    if getattr(last_message, "tool_calls", None):
        return "tool_node"
    
    return END


# =====================================================
# Graph Builder
# =====================================================

builder = StateGraph(AgentState)

builder.add_node("chatbot",chatbot)
builder.add_node("tool_node",tool_node)

builder.add_edge(START,"chatbot")
builder.add_conditional_edges(
    "chatbot",
    should_continue,
)

builder.add_edge(
    "tool_node",
    "chatbot"
)

graph = builder.compile()

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from util import show_graph
# show_graph(graph)

question = input("\n질문 : ")

# if question.lower() == "exit":
#     break

result = graph.invoke({
    "messages":question
})

answer = result["messages"][-1].content
print("AI 답변:",answer)

