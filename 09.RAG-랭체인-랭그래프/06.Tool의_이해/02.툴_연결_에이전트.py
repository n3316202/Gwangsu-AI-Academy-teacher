import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from llm_loader import init_custom_llm

llm = init_custom_llm()

#LLM 은 현재 시각을 학습 하지 않았기 때문에, 시간을 알려줄수 없음

from langchain.tools import tool
from datetime import datetime
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage


@tool
def bmi(height:float, weight:float):
    """
    BMI = 몸무게(kg) ÷ (키(m) × 키(m))
    키(cm)와 몸무게(kg)를 이용하여 BMI를 계산한다.
    """

    result = weight /  ((height / 100) ** 2)

    if result < 18.5:
        state = "저체중 입니다"
    elif result < 24.9:
        state = "정상 입니다"
    else:
        state = "과체중 입니다"
    
    return f"BMI:{result},{state}"

@tool
def add(a,b):
    """
    두 수를 더한다
    """
    print("add 함수 호출")
    return a + b

@tool
def get_time(city):
    '''
    도시 이름을 받아 현재 시간을 알려준다.
    '''
    now = datetime.now()
    return f"{city} 현재시간 {now.strftime('%Y-%m-%d %H:%M:%S')}"

print(get_time)
print(type(get_time))

result = get_time.invoke({"city":"seoul"})
print(result)

agent = create_agent(
    model = llm,
    tools=[get_time,add, bmi]
) 

response = agent.invoke(
    {
        "messages":[
            HumanMessage(content=input("질문하세요? :"))
        ]
    }
)

#print(response)
print("="*50)
print(response["messages"][-1].content)

