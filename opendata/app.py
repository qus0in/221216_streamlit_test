import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.write(
   "https://www.data.go.kr/data/15070282/fileData.do"
)

# UTF-8 / CP-949
# https://seong6496.tistory.com/269
df = pd.read_csv('./opendata/data.csv', encoding='cp949')
st.write(df)