import streamlit as st

# | 구분    | Session     | Cache          |
# | ----- | ----------- | -------------- |
# | 목적    | 사용자 상태 유지   | 작업 결과 재사용      |
# | 기준    | 사용자별        | 앱/서버 기준        |
# | 저장 내용 | 로그인 정보, 입력값 | 데이터, 모델, 계산 결과 |
# | 공유    | 사용자마다 다름    | 여러 사용자가 공유 가능  |
# | 변경 주체 | 사용자 행동      | 프로그램 실행        |
# | 예     | 로그인 상태      | AI 모델          |

st.set_page_config(
    page_title="세션과캐쉬"
)

# =====================================================
# Session State 초기화
# =====================================================
# session_state = 유저별 저장공간
if "count" not in st.session_state: 
    st.session_state.count = 0

if st.button("증가"):
    st.session_state.count += 1 
    #st.session_state.count = st.session_state.count + 1

st.write("카운트=", st.session_state.count)

st.divider()

count = 0

if st.button("증가-1"):
    count += 1

st.write("count =", count)

st.divider()