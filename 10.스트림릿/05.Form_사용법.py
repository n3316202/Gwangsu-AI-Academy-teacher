import streamlit as st

st.title("Form 예제")

with st.form("폼태그"):
    name = st.text_input("이름")
    email = st.text_input("이메일")

    submit = st.form_submit_button("가입")

if submit:
    st.success("제출완료")
    #st.write(name,email)

    st.write(st.session_state)