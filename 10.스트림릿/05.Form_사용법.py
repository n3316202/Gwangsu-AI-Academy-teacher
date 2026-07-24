import streamlit as st

st.title("Form 예제")

with st.form("폼태그"):
    name = st.text_input("이름")
    email = st.text_input("이메일")

    submit = st.form_submit_button("가입")


# with 문법
with open("test.txt","w",encoding="utf-8") as f:
    f.write("안녕하세요!!")



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
    