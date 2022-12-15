# streamlit 라이브러리 호출
import streamlit as st
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/bigdata-young/ai_26th/main/data/insurance.csv')
st.write(df)

import joblib
model = joblib.load('./ml_model/app.py')
st.write(model.coef_)