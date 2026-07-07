
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate


import sys
from pathlib import Path
import os

sys.path.append(str(Path(__file__).resolve().parent.parent))
from llm_loader import init_custom_llm
# 템플릿 사용
from langchain_core.prompts import PromptTemplate

llm = init_custom_llm()

topics=[
    "Python",
    "Django",
    "React"
]

prompt = PromptTemplate.from_template("""
당신은 파이썬 강사입니다.
주제: {topic}    
초보자도 이해할 수 있게 설명하세요.                                  
""")


# for t in topics:
#     formatted = prompt.format(topic=t)
    
#     respose = llm.invoke(formatted)
#     print("===========")
#     print(respose.content)

# 
# 체인 연결

# 1. Chain
# 여러 작업을 순서대로 연결
chain =  prompt | llm 

result = chain.invoke({
    "topic":"반복문"
})
print(result.content)

