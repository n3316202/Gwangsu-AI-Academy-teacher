import streamlit as st

st.title("다운로드 업로드 버튼")

if st.button("클릭"):
    st.success("버튼 클릭!")

text = "스트림릿 다운로드 테스트"

st.download_button(
    label="파일다운로드",
    data=text,
    file_name="test.txt"
)

file = st.file_uploader("파일 업로드")

if file:
    st.write("파일명", file.name)

st.title("CSV 이미지 업로드")

file = st.file_uploader(
    "CSV 파일선택",
    type=["csv"]
)

import pandas as pd

if file:
   df = pd.read_csv(file)
   st.dataframe(df)

   st.write("텍스트")
   st.write(df.describe())
   st.write(df.head())

############################
st.title("이미지 업로드")

file = st.file_uploader(
    "이미지 선택",
    type=["png","jpg","jpeg"]
)

if file:
    st.image(file,caption="이미지 업로드")

