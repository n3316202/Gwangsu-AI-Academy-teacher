from langgraph.graph import StateGraph
from langgraph.graph import START, END

from langchain.chat_models import init_chat_model
from state import AnalysisState
from tools import *


# ----------------------
# LLM
# ----------------------
import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent.parent.parent)
)

from llm_loader import init_custom_llm

llm = init_custom_llm()

# ----------------------
# CSV
# ----------------------
BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "sales.csv"

df = load_csv(str(DATA_PATH))
print(df)

# ----------------------
# Question
# ----------------------
def question_node(state):

    state["dataframe"] = df

    return state

# ----------------------
# Planner
# ----------------------
def planner_node(state):
    
    prompt = f"""
당신은 데이터 분석 작업을 분류하는 Planner Agent입니다.

사용자의 질문을 보고 가장 적합한 분석 작업 유형 하나만 선택하세요.

반드시 아래 단어 중 하나만 출력하세요.

EDA
GROUP
FILTER
PLOT
STATISTICS
ML


분석 유형 판단 기준:

1. EDA
- 데이터 전체 구조를 파악하는 질문
- 데이터 개수, 컬럼, 결측치, 기본 통계 확인
예)
"데이터를 분석해줘"
"컬럼 정보를 알려줘"
"결측치를 확인해줘"


2. GROUP
- 특정 기준으로 데이터를 묶어서 집계하는 질문
- "별", "마다", "단위로", "그룹별", "월별", "년도별", "지역별", "상품별"
- sum, count, average 같은 집계가 필요한 경우

예)
"월별 매출은?"
"지역별 판매량은?"
"상품별 매출 합계를 알려줘"
"년도별 평균 매출"


3. FILTER
- 특정 조건에 맞는 데이터 조회
- 조건 검색
- 특정 값 또는 범위 선택

예)
"서울 데이터만 보여줘"
"매출 100만원 이상만 보여줘"
"2025년 데이터만 조회"


4. PLOT
- 그래프 생성 요청

예)
"매출 그래프 보여줘"
"월별 추이를 차트로 만들어줘"


5. STATISTICS
- 통계 분석 요청
- 상관관계, 평균, 분산, 가설검정 등

예)
"매출 평균은?"
"상관관계를 분석해줘"
"두 그룹 차이가 유의미한가?"


6. ML
- 머신러닝 관련 요청

예)
"매출을 예측해줘"
"지역을 군집화해줘"


판단 규칙:

- "~별", "~마다", "~단위", "~별 합계"가 있으면 GROUP
- 날짜 기준(월, 년, 분기, 일)으로 집계하면 GROUP
- 그래프 요청이 있으면 PLOT
- 조건으로 데이터를 선택하면 FILTER
- 예측/분류/군집이면 ML


질문:
{state["question"]}


출력:
분석 유형 이름 하나만 출력하세요.
"""
    state["analysis_type"] = llm.invoke(prompt).content.strip().upper()
    
    return state
