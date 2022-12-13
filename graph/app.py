import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.write(
    '''
    # 탐색적 데이터 분석 (EDA) & Seaborn을 통한 데이터 시각화
    ## 데이터의 종류
    * 데이터의 특성에 따라서 시각화 방식도 달라짐
    * 정형 데이터 : 값으로 나타낼 수 있는 데이터 (숫자)
    * 비정형 데이터 : 정형 데이터가 아닌 것 (사진, 언어...)
    ## 정형 데이터
    |대분류|소분류|예시|
    |:-|:-|:-|
    |수치형 데이터(사칙 연산이 가능한 데이터)|연속형 데이터|키, 몸무게, 수입
    ||이산형 데이터|과일 개수, 책의 페이지 수
    |범주형 데이터(범주로 나누어지는 데이터)|순서형 데이터|학점, 순위(랭킹)|
    ||명목형 데이터|성별, 음식종류, 우편번호|
    # 수치형 데이터 numerical data
    > 사칙 연산이 가능한 데이터 (+, -, *, /)
    '''
)

# df
titanic = sns.load_dataset('titanic')
st.write(titanic) # 적당히 짤라줌
# st.table(titanic) # 전체를 보여줌

# seaborn를 통한 시각화
fig = plt.figure(figsize=(8, 4))
titanic['나이'] = titanic.age

import plotly.express as px

# 한글 사용 -> plotly
# requirements : plotly
# https://docs.streamlit.io/library/api-reference/charts/st.plotly_chart
# https://www.datacamp.com/cheat-sheet/plotly-express-cheat-sheet
fig = px.histogram(titanic, x="나이")
st.plotly_chart(fig)

fig = plt.figure(figsize=(8, 4))
sns.histplot(data=titanic, x='age', hue='alive', multiple='stack')
st.pyplot(fig)

# pie
x = [10, 60, 30] # 범주형 데이터별 파이 그래프의 비율
labels = ['A', 'B', 'C']
fig = plt.figure(figsize=(8, 4))
plt.pie(x=x, labels=labels, autopct='%.1f%%')
st.pyplot(fig)