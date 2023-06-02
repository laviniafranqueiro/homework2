import streamlit as st
import pandas as pd 
st.title('tarefa do Josir')
st.caption('Lavínia Franqueiro')

df = pd.read_csv('carprice.csv', sep =',')
st.dataframe(df)

chart_data = df[['make', 'wheel-base']]
st.bar_chart(chart_data, X = "make", Y = "wheel-base")
