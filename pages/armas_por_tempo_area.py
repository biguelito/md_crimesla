import datetime
import pandas as pd
import mysql.connector
import streamlit as st
import matplotlib.pyplot as plt
from sql.mysqlconnector import MysqlConnector

def armas_por_tempo_area(dataInicial, dataFinal):
    connector = MysqlConnector()
    cidades= [15, 6]
    return connector.obter_armas_por_tempo_aera(dataInicial, dataFinal, cidades)

def processar_datas(data_inicio, data_fim):
    st.write(f"Processando dados entre {data_inicio} e {data_fim}")


st.title("Armas por tempo e área")

data_inicio = st.date_input("Selecione a data de início", pd.to_datetime('2022-01-01'))
data_fim = st.date_input("Selecione a data de fim", pd.to_datetime('2022-12-31'))

categorias_selecionadas = st.multiselect("Selecione as áreas", ["area1","area2","area3","area4"])

#

if st.button("Processar Dados"):
    areas = " ".join(categorias_selecionadas)
    st.write(f"Areas selecionadas: "+areas)
    processar_datas(data_inicio, data_fim)
    df = pd.DataFrame(armas_por_tempo_area(dataInicial=data_inicio,dataFinal=data_fim),columns=["Tipo da arma","Quantidade"])
    # Ordenar o DataFrame pela coluna "Quantidade" em ordem decrescente
    df = df.sort_values(by="Quantidade", ascending=False)

    # Selecionar as 10 categorias mais expressivas
    top_10_df = df.head(10)

    # Layout em duas colunas
    col1, col2 = st.columns(2)

    # Exibir o DataFrame na coluna 1
    with col1:
        st.header("Tabela de Dados")
        st.dataframe(df)

    # Gráfico de barras na coluna 2
    with col2:
        st.header("Top 10 armas mais utilizadas")
        fig, ax = plt.subplots()
        ax.bar(top_10_df["Tipo da arma"], top_10_df["Quantidade"])
        plt.xticks(rotation=45, ha="right")  
        st.pyplot(fig)
    
  