from typing import Annotated
from typing_extensions import TypedDict

from langgraph.graph import (
    StateGraph,
    START,
    END
)

from langgraph.graph.message import add_messages

from langchain_core.messages import (
    HumanMessage,
    AIMessage
)

import sys
from pathlib import Path


sys.path.append(str(Path(__file__).resolve().parent.parent.parent.parent)
)

from llm_loader import init_custom_llm

llm = init_custom_llm()

# state 
class State(TypedDict):
    #대화 내역
    messages:Annotated[list,add_messages]

    # Planner가 결정
    need_debug: bool

    #각 Agnet 완료 여부
    debug_done: bool
    fix_done: bool
    review_done : bool

    # 슈퍼바이져가 선택할 다음 노드
    next: str

# 노드 함수 

def planner(state):

    print("\n===================== Planner =================")
    user_question = state["messages"][0].content   

    prompt = f"""
    당신은 Software Project Planner입니다.

    사용자의 요청을 읽고

    디버깅 작업인지 판단하세요.

    오류를 분석하지 않고
    코드를 수정하지 않고
    리뷰도 하지 않습니다.

    반드시 아래 형식만 출력하세요.

    debug=True

    또는

    debug=False


    ----------------------

    사용자 요청

    {user_question}
    """

#     content=f"""
# 아래 Python 코드의 오류를 수정해주세요.

# ```python
# def average(nums):
#     return sum(nums) / len(nums)

# print(average([]))
# ```

    result = llm.invoke(prompt)
    text = result.content.lower()
    need_debug = "debug=True" in text()

    return {
        "need_debug":need_debug
    }

# ----------------------------------------------------
# Router
# ----------------------------------------------------
