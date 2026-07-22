import streamlit as st
import pandas as pd

####################################################
# 제목
####################################################
st.title("스트림릿 따라하기 : 허쌤")
st.header("Header 예제")
st.subheader("SubHeader 예제")


st.text("안녕하세요")
st.write("Streamlit을 배워봅시다!")

# ####################################################
# # Markdown
# ####################################################

st.markdown("---")
st.markdown("### Markdown")
st.markdown("## Markdown")
st.markdown("# Markdown")
st.markdown("""
- Python
- Streamlit
- LangChain
- RAG
""")
# ####################################################
# # 코드 출력
# ####################################################

st.markdown("---")
st.subheader("코드 출력")

code = """
for i in range(5):
    print(i)
"""

st.code(code,language="python")

# ####################################################
# # 캡션
# ####################################################

st.caption("이 화면은 스트림릿 실습입니다.")

# ####################################################
# # 이미지
# ####################################################

st.markdown("---")
st.subheader("이미지 출력")

st.image("cat.png",width=300)


# ####################################################
# # DataFrame
# ####################################################

st.markdown("---")
st.subheader("데이타 프레임 출력")

df = pd.DataFrame(
    {
        "이름": ["홍길동", "김철수", "이영희"],
        "나이": [20, 22, 25],
        "점수": [90, 85, 100]
    }
)

st.dataframe(df)

# ####################################################
# # Table
# ####################################################

st.subheader("테이블(Table)")
st.table(df)

# ####################################################
# # Metric
# ####################################################

st.markdown("---")
st.subheader("Metric")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("매출","100만원","+10%")

with col2:
    st.metric("매출","100만원","+10%")

with col3:
    st.metric("매출","100만원","+10%")

st.markdown("---")
st.subheader("Columns(컬럼 함수)")

left, right = st.columns(2)

with left:
    st.write("왼쪽 화면")
    st.success("성공")

with right:
    st.write("오른 화면")
    st.info("정보")