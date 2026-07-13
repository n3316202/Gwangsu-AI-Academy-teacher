from typing import TypedDict
from langgraph.graph import StateGraph, START, END

# 랭그래프 아저씨가 이해하는 딕셔너리를 만들기 위해.
#
# 랭그래프 아저씨가 이해하는 딕셔너리를 만들기 위해.
class State(TypedDict):
    name:str
    age:int

dic:State = {
    "name":"홍길동",
    "age": 30
}
# print(type(dic)) # <class 'dict'>
# print(dic)

# 주의 
# dic_persion = State()
# print(dic_persion)

# 노드 = 함수 = 랭그래프가 사용 하는 함수
# 노드(랭그래프가 사용하는 함수)를 만들때
# 규칙(제약)이 존재함
# 이 규칙대로 함수를 만들어 야 됨

# 첫번째 규칙 : 해당 함수 파라미터를 가지는데
# 반드시 state 를 파라미터로 받음

# 두번째 규칙 
# 리턴값도 반드시 있어야함
# State 를 변경(업데이트)하여 반환하거가 또는 그대로 반환

# 1. Node의 입력은 항상 State이다.
# 2. State는 Dictionary이다.
# 3. Node는 State를 읽어서 필요한 작업을 한다.
# 4. Node는 입력받은 State를 변경하여 반환한다.

# 노드 가장 기본
# 그대로 반환
def info(state:State):

    state["name"]= "홍길순"
    state["age"]= 39
    
    return state

# 변경(업데이트) 하여 업데이트 
# def info(state:State):
# #     {
# #     "name":"홍길순",
# #     "age": 30
# # }
#     # state["name"] = "홍길순"
#     # return state
#     return {
#         "name":"홍길순"
#     }


#그래프 생성
builder = StateGraph(State)

builder.add_node("info",info) # 함수 등록 

builder.add_edge(START, "info")
builder.add_edge("info",END)

# 그래프 컴파일
graph = builder.compile()

result = graph.invoke({
    "name":"홍길동",
    "age": 30
})
 
print(result)


# from IPython.display import Image, display


# display(
#     Image(
#         graph.get_graph()
#         .draw_mermaid_png()
#     )
# )