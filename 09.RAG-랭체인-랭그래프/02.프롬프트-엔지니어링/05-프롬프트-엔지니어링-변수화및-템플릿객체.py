from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from openai import OpenAI

# Prompt 변수화 (Template 구조)
topic = "딥러닝"

# 💡 문제점
# 코드와 Prompt가 섞임
# 재사용 어려움
prompt = f"""
당신은 AI 강사입니다.

다음 주제를 설명하세요:
{topic}

조건:
- 초보자 대상
- 예제 포함
- 5줄 이내
"""

import sys
from pathlib import Path
import os

sys.path.append(str(Path(__file__).resolve().parent.parent))
from llm_loader import init_custom_llm
from langchain_core.prompts import PromptTemplate

topic = "타이타닉 생존률"

prompt = PromptTemplate.from_template("""
당신은 데이터 분석 전문가입니다.

주제: {topic}

다음 조건으로 설명하세요:
- 초보자도 이해 가능
- 핵심만 설명
- 예제 포함
                                                                            
""")

result = prompt.invoke({"topic":"머신러닝"})
#result = prompt.format(topic="반복문")

print(type(result))
print(result)

messages = ChatPromptTemplate.from_messages([
  ("system", "당신은 Python 강사입니다."),
  ("human", "{topic}을 설명하세요")  
])

print(messages)
result = messages.invoke({"topic","딕셔너리"})

llm = init_custom_llm()
respose = llm.invoke(result)

print(respose.content)



