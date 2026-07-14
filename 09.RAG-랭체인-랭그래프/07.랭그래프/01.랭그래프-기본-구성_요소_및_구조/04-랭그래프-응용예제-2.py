from typing import TypedDict
from langgraph.graph import StateGraph, START, END

# 1.state 정의
class State(TypedDict):
    price:int

# {
#     "price":0
# }

# 2. node 함수

def discount(state:State):
    state["price"] = int(state["price"] * 0.9)
    return state

def delivery(state:State):
    #state["price"] = state["price"] + 5000
    return {
        "price" : state["price"] + 5000
    }

# 3. 그래프 생성
builder = StateGraph(State)

builder.add_node("discount",discount)
builder.add_node("delivery",delivery)



# START
#   ↓
# discount
#   ↓
# delivery
#   ↓
# END
# 
# 초기값
# 100000
# 결과
# 95000

# 계산 과정

# 100000
# ↓

# 10% 할인

# 90000
# ↓

# 배송비 +5000

# 95000

