
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from openai import OpenAI

# 1. JSON 출력 강제하기
# 일반출력
# 결과가 자유로운 텍스트로 나옴(파싱 불가능)
prompt = """
사용자 정보를 만들어줘.

이름: 김철수
나이: 25
직업: 개발자
"""

# JSON 구조화 출력
prompt = """
다음 정보를 JSON 형식으로 출력하세요.

조건:
- 반드시 JSON만 출력
- 설명 금지
- key는 영어로 작성

정보:
이름: 김철수
나이: 25
직업: 개
"""

# 실무형 JSON (강력 추천)
prompt = """
당신은 데이터 포맷터입니다.

다음 정보를 JSON으로 변환하세요.

[CONSTRAINT]
- 반드시 JSON만 출력
- 코드블록 사용 금지
- 추가 설명 금지
- null 금지

[DATA]
이름: 김철수
나이: 25
직업: 개발자
경력: 3년
"""
# Table 출력 (보고서용)
prompt = """
다음 데이터를 표 형식으로 정리하세요.

[DATA]
Python, 중급, 3년
Java, 초급, 1년
C++, 고급, 5년

[OUTPUT]
Markdown table 형식으로 출력
"""

# API용 Strict Output (실전 필수)
prompt = """
당신은 API 응답 생성기입니다.

[RULES]
- JSON만 출력
- 설명 금지
- key는 snake_case 사용
- 배열은 반드시 list로 출력

[OUTPUT FORMAT]
{
  "user_name": "",
  "user_age": 0,
  "user_skills": []
}

[INPUT]
이름: 김철수
나이: 25
기술: Python, AI, ML
"""

import sys
from pathlib import Path
import os

sys.path.append(str(Path(__file__).resolve().parent.parent))
from llm_loader import init_custom_llm

llm = init_custom_llm()
respose = llm.invoke(prompt)

print(respose.content)



