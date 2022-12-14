import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('전국 지역보건의료기관 현황')

# 파일 가져오기

df = pd.read_csv('./medical_institution/medical_instituntion.csv', encoding='CP949')
df.set_index = df['보건기관명']

# 데이터를 어디에서 가져왔는지
if st.button('data copyright link'):
    st.write('https://www.data.go.kr/tcs/dss/selectFileDataDetailView.do?publicDataPk=3072692')

# 데이터를 보여줌
if st.checkbox('원본 데이터 보기'):
    st.subheader('Raw data')
    st.write(df)

tab1, tab2, tab3 = st.tabs(["시에 따른 분류", "시군구에 따른 분류", "보건기관 검색하기"])

with tab1:
   # 일단 그래프 그려보기
    st.subheader('지역보건의료기관 시에 따른 분류')
    fig = plt.figure(figsize=(8, 4))
    sns.histplot(data=df, x='시도')
    st.pyplot(fig)

    # 데이터를 분석하기 # 리스트 출력
    st.subheader('시에 따른 분류')
    option = st.selectbox(
        '시를 선택하세요', 
        (df['시도'].drop_duplicates()))

    station_data = df.loc[(df['시도'] == option)]
    st.write(station_data)

with tab2:
    # 일단 그래프 그려보기 - 선택에 따라서 시안에 구만 보이게? 
    # 선택한 구와 비슷한 다른구와 비교하는 것도 좋을 것 같음.
    st.subheader('지역보건의료기관 시에 따른 분류 top 10')
    fig = plt.figure(figsize=(8, 4))
    # sns.histplot(data=df, x='시군구', bins=10)
    sns.countplot(data=df, x='시군구', order=df.시군구.value_counts()[:10].index)
    st.pyplot(fig)

    # 데이터를 분석하기 # 리스트 출력
    # 시를 선택하고 그에 맞는 구가 나오도록 개선 필요
    st.subheader('시군구에 따른 분류')
    option = st.selectbox(
        '시군구를 선택하세요', 
        (df['시군구'].drop_duplicates()))
    station_data = df.loc[(df['시군구'] == option)]
    st.write(station_data)

with tab3:
    st.subheader('원하는 의료기관 정보 보기!') # 일부만 입력해도 출력되도록 고쳐야됨
    title = st.text_input('원하는 의료기관의 이름을 입력하세요!(보건소까지 정확하게 입력해주세요!)', 'Life of Brian')
    if title:
        station_data = df.loc[(df['보건기관명'] == title)]
        st.write(station_data)