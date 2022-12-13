# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    """
    # 제 첫 웹페이지 입니다
    ## 부족하지만 많이 사랑해주세요!
    * 1$ = 1,400원
    * ^_^
    """
)

# https://pixabay.com/ko
st.image(
    "https://cdn.pixabay.com/photo/2014/11/30/14/11/cat-551554_960_720.jpg"
)