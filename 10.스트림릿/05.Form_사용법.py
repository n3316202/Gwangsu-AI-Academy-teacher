import streamlit as st

st.title("Form 예제")

with st.form("폼태그"):
    name = st.text_input("이름")
    email = st.text_input("이메일")

    submit = st.form_submit_button("가입")

# 파일처럼 자원을 닫기 위한 목적이 아니라, 
# "현재 어떤 컨테이너(Container)에 위젯을 추가할 것인지"를 지정하는 역할


# with 문법
with open("test.txt","w",encoding="utf-8") as f:
    f.write("안녕하세요!!")

f = open("test.txt", "w", encoding="utf-8")

try:
    f.write("안녕하세요.")
finally:
    f.close()


# import requests

# if submit:
#     st.success("제출완료")
#     st.write(name,email)


#     response = requests.get(
#         "www.naver.com/login",
#         json = {
#             "name":name,
#             "email":email
#         }
#     )

#     if response.status_code == 200:
#         st.success("서버 전송 성공")
#     else:
#         st.error("전송실패")
    