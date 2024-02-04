import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sql.mysqlconnector import MysqlConnector
connector = MysqlConnector()

st.title("Quais são os locais mais propensos a crimes envolvendo a faixa etaria da vitima?")

faixas_etarias = ['Jovem','Adulto','Idoso']
faixa_selecionada = st.selectbox(label="Selecione a faixa etária",
                                 options=faixas_etarias,
                                 placeholder='Selecione')
if faixa_selecionada != "Selecione":
    st.write("Exibindo resultados na faixa etária: "+faixa_selecionada)



    
  