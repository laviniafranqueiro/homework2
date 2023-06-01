import streamlit as st
import pandas as pd 
st.title('tarefa 1 do Josir')
st.caption('Lavínia Franqueiro')

df = pd.read_csv('carprice.csv', sep =',')
st.dataframe(df)

#arquivo = open('carprice.csv')
#for linha in arquivo:
#    st.write(linha)
