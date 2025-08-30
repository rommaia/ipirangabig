import streamlit as st
import pandas as pd

st.title('FATEC IPIRANGA')
st.header('Disciplina de BIG DATA')
st.subheader('Prof. : Rômulo Maia')
st.write(' Ola alunos Fatec Ipiranga')

if st.button('Exibir tabela da População'):
        dados = pd.read_csv('world_population.csv')
        st.write(dados)

nome = st.text_input('Qual o seu nome : ')
st.write(nome)
