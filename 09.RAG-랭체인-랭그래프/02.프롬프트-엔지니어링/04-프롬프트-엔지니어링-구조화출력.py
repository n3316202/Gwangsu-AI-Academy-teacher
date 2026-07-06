
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from openai import OpenAI

# 제로샷
# 예시 없음
# ↓
# 모델이 바로 답변
# Zero-shot (예시 없음)
# AI가 기준 없이 바로 답변 생성

prompt = """
다음 문장을 영어로 번역하세요.

나는 오늘 학교에 갔다.
"""

# Few-shot
# 예제 제공
# ↓
# 패턴 학습
# ↓
# 새 입력 예측
prompt = """
Q: 고양이
A: 동물

Q: 자동차
A: 탈것

Q: 사과
A:
"""

#Chain of Thought 적용
prompt = """
다음 문제를 단계별로 생각해서 풀어라.

문제:
철수는 사과 5개를 가지고 있다.
3개를 먹었다. 몇 개 남았는가?

풀이 과정:
1. 전체 개수 확인
2. 소비한 개수 확인
3. 계산 과정 설명
4. 최종 답변
"""

# Few-shot + CoT 혼합 (실전)
# 실무에서 가장 많이 쓰는 형태
prompt = """
[EXAMPLES]

예시 1:
문제: 2 + 2
풀이: 2 + 2 = 4
답: 4

예시 2:
문제: 5 + 3
풀이: 5 + 3 = 8
답: 8

[TASK]
문제: 7 + 6

[INSTRUCTION]
1. 단계별로 계산
2. 마지막에 답 출력
"""
# AI는 답을 주는 존재가 아니라, 생각 과정을 설계해야 제대로 작동

import sys
from pathlib import Path
import os

sys.path.append(str(Path(__file__).resolve().parent.parent))
from llm_loader import init_custom_llm

llm = init_custom_llm()
respose = llm.invoke(prompt)

print(respose.content)



