from matplotlib import cm
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
    if areas_selecionadas == []:
        st.write("Selecione uma ou mais áreas!")
    elif areas_selecionadas != []:
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
        
        st.header("Os dez tipos de crime mais recorrentes")
        # Gráfico em pizza
        # Criar um gráfico de pizza com cores automáticas
        cores = cm.tab10.colors[:len(top_10_df["Tipo do Crime"])]  # Use a paleta de cores 'tab10'
        # Configurar as propriedades do texto (aumentar o tamanho da fonte)
        textprops = {'fontsize': 18, 'color':'white'}
        plt.figure(figsize=(20, 20), facecolor='none', edgecolor='none')
        plt.pie(top_10_df["Quantidade"], labels=top_10_df["Tipo do Crime"], colors=cores,
        autopct='%1.1f%%', startangle=140,textprops=textprops)
        # Ajustar o layout para evitar cortar rótulos
        plt.tight_layout()
        st.pyplot(plt)
        st.header("Tipos de crimes ordenados pela quantidade")
        st.dataframe(df)