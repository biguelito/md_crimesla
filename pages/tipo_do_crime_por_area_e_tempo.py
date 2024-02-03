import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sql.mysqlconnector import MysqlConnector
connector = MysqlConnector()

def obter_tipo_crime_por_tempo_aera(sql, dataInicial, dataFinal, areas_nome):
    areas_id = [areas[i] for i in areas_nome]
    return sql.obter_tipo_crime_por_tempo_aera(dataInicial, dataFinal, areas_id)

def obter_listagem_areas(sql):
    return sql.obter_listagem_areas()

def processar_datas(data_inicio, data_fim):
    st.write(f"Processando dados entre {data_inicio} e {data_fim}")
    return


st.title("Quais são os tipos de crimes mais comuns em uma determinada área durante um período específico?")

areas = obter_listagem_areas(connector)
data_inicio = st.date_input("Selecione a data de início", pd.to_datetime('2022-01-01'))
data_fim = st.date_input("Selecione a data de fim", pd.to_datetime('2022-12-31'))

areas_selecionadas = st.multiselect(label="Selecione as áreas", options=areas.keys())

#

if st.button("Processar Dados"):
    # areas = " ".join(categorias_selecionadas)
    # st.write(f"Areas selecionadas: "+areas)
    processar_datas(data_inicio, data_fim)
    tipo_resultado = obter_tipo_crime_por_tempo_aera(connector, dataInicial=data_inicio,dataFinal=data_fim, areas_nome=areas_selecionadas)
    df = pd.DataFrame(tipo_resultado, columns=["Tipo do Crime","Quantidade"])
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
        st.header("Top 10 tipos de crime mais recorrentes")
        fig, ax = plt.subplots()
        ax.bar(top_10_df["Tipo do Crime"], top_10_df["Quantidade"])
        plt.xticks(rotation=45, ha="right")  
        st.pyplot(fig)
    
  