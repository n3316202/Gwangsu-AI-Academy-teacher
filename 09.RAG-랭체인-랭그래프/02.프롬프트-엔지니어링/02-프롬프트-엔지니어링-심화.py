
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from openai import OpenAI

load_dotenv()
from openai import OpenAI
client = OpenAI()

# 페르소나 => (인물설정)
# AI의 성격 + 경력 + 말투를 지정
prompt = """
당신은 다음 특징을 가진 AI입니다.

[Persona]
- 20년차 AI 연구원
- 매우 엄격한 대학 교수
- 틀린 질문은 바로 지적함
- 칭찬보다 비판을 먼저 하는 스타일
- 핵심만 짧고 냉정하게 설명

[Task]
머신러닝이 무엇인지 설명하세요.

[Constraint]
- 5줄 이내
- 비유 1개 포함
- 초보자 대상
"""
# 여러 케릭터 지정
prompt = """
다음 질문에 대해 서로 다른 Role로 답변하세요.

질문: AI란 무엇인가?

Role 1: AI 연구원
Role 2: 초등학교 선생님
Role 3: 비유를 많이 쓰는 유튜버

각 Role별로 답변을 구분해서 작성하세요.
"""

# 역할하고 Tone 조합
prompt = """
당신은 친절한 스타트업 CTO입니다.

스타트업에서 AI를 도입해야 하는 이유를 설명하세요.

조건:
- 말투: 친근하고 현실적
- 예시 포함
- 투자자 설득용 느낌
"""

import sys
from pathlib import Path
import os

sys.path.append(str(Path(__file__).resolve().parent.parent))
from llm_loader import init_custom_llm

print(init_custom_llm)

llm = init_custom_llm()
respose = llm.invoke(prompt)

print(respose.content)



# response = client.responses.create(
#     model="gpt-4o-mini",
#     input=prompt
# )

# print(response.output_text)