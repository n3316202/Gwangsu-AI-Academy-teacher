import streamlit as st
import pandas as pd

# 사용자 입력 받기v
# Widget 값 저장
# 입력 결과 출력

#st.title("스트림릿 입력 위젯")

st.markdown(
    "<h1>스트림릿 <span style='color:#FFD700;'>입력</span> 위젯</h1>",
    unsafe_allow_html=True
)

# 텍스트 입력
name = st.text_input("이름입력")

st.write("이름:", name)

# 숫자 입력
age = st.number_input(
    "나이",
    min_value=0,
    max_value=100,
    value=20
    )

st.write("나이:", age)

# 선택 박스
job = st.selectbox(
    "직업선택",
    [
        "학생",
        "개발자",
        "디자이너",
        "회사원"
    ]
)

st.write("직업:", job)

st.markdown("---")

# 멀티 실렉트
hobby = st.multiselect(
    "취미선택",
    [
        "운동",
        "독서",
        "게임",
        "여행"
    ]
)

st.write("직업:", hobby)
print("실행")

st.markdown("---")

gender = st.radio(
    "성별",
    [
        "남자",
        "여자",
        "동물"
    ]
)
st.write("성별:", gender)

st.markdown("---")

agress = st.checkbox("개인정보 수집 동의")
st.write("동의:", agress)

# 슬라이더
score = st.slider(
    "점수",
    0,
    100,
    50
)
st.write("점수:", score)

# 날짜와 시간
st.divider()
date = st.date_input("생년월일")
st.write("날짜 :", date)
st.divider()

time = st.time_input("출근 시간")

st.write("시간 :", time)