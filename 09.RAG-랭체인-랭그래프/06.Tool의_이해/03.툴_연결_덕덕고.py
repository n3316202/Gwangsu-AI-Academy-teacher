# pip install -U ddgs

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))
from llm_loader import init_custom_llm

llm = init_custom_llm()

#LLM 은 현재 시각을 학습 하지 않았기 때문에, 시간을 알려줄수 없음

from langchain.tools import tool
from datetime import datetime
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_community.tools import DuckDuckGoSearchRun

# | 검색 엔진                | 최신 정보 | API Key | 추천도   |
# | -------------------- | ----- | ------- | ----- |
# | DuckDuckGo           | O     | ❌       | ⭐⭐⭐⭐⭐ |
# | Tavily               | O     | ✅       | ⭐⭐⭐⭐⭐ |
# | SerpAPI (Google)     | O     | ✅       | ⭐⭐⭐⭐  |
# | Google Custom Search | O     | ✅       | ⭐⭐⭐⭐  |
# | Bing Search          | O     | ✅       | ⭐⭐⭐   |
# | Brave Search         | O     | ✅       | ⭐⭐⭐⭐  |
# | Exa Search           | O     | ✅       | ⭐⭐⭐⭐⭐ |

########################################################################
# 1. DuckDuckGo Tool 생성
########################################################################

duck = DuckDuckGoSearchRun()

@tool
def web_search(query):
    """
    인터넷에서 최신 정보를 검색하는 도구입니다.

    사용 조건:
    - 오늘
    - 현재
    - 최신
    - 뉴스
    - 주가
    - 환율
    - 날씨
    - 최근 발표
    - 최근 출시
    - 실시간 정보

    일반 지식 질문에는 사용하지 않습니다.
    """
    print("덕덕고 호출")
    return duck.run(query)

# result = web_search.invoke({
#     "query":"오늘 삼성전자 주가"
# })
# print(result)

agent = create_agent(
    model = llm,
    tools=[web_search]
)

system = SystemMessage(
    content="""

당신은 AI Assistant입니다.

규칙:

1. 일반적인 지식 질문은 Tool을 사용하지 않습니다.
2. 최신 정보가 필요한 경우 반드시 web_search Tool을 사용합니다.

최신 정보 예:

- 오늘
- 현재
- 최신
- 뉴스
- 환율
- 주가
- 날씨
- 최근 발표
- 최근 출시
- 실시간 정보


검색 결과를 그대로 출력하지 말고
사용자가 이해하기 쉽게 요약합니다.
"""
)

messages = [
    system,
    HumanMessage(content=input("질문하세요? :"))
]

response = agent.invoke({
    "messages":messages
})

print("="*50)
print(response["messages"][-1].content)

# | Tool 종류    | 사용 예         | 추천 라이브러리/API                                      |
# | ---------- | ------------ | ------------------------------------------------- |
# | 🌐 웹 검색    | 일반 최신 정보, 뉴스 | DuckDuckGo, Tavily, SerpAPI, Google Search        |
# | 🌦️ 날씨     | 현재 날씨, 예보    | OpenWeatherMap, WeatherAPI, 기상청 API               |
# | 💰 환율      | USD→KRW      | ExchangeRate API, Frankfurter API                 |
# | 📈 주가      | 삼성전자 주가      | Yahoo Finance, Alpha Vantage, Finnhub, LS OpenAPI |
# | 📰 뉴스      | 오늘 AI 뉴스     | NewsAPI, GNews                                    |
# | 📍 지도      | 맛집, 거리       | Google Maps API, Kakao Map API, Naver Map API     |
# | 📧 이메일     | 메일 보내기       | Gmail API, Microsoft Graph                        |
# | 📅 일정      | 일정 등록        | Google Calendar API                               |
# | 📂 파일      | PDF, Excel   | LangChain Document Loader                         |
# | 🧮 계산      | 수학 계산        | Python Tool                                       |
# | 🐍 코드 실행   | 데이터 분석       | Python REPL                                       |
# | 🗄️ 데이터베이스 | SQL 조회       | SQLDatabase Tool                                  |
# | 📚 RAG     | 문서 검색        | Chroma, FAISS, Pinecone                           |
# | 🖼️ 이미지 생성 | 그림 생성        | OpenAI Images                                     |
# | 🎤 음성      | STT/TTS      | Whisper                                           |
# | 🧠 LLM     | 질의응답         | OpenAI, Anthropic, Gemini                         |
