import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sql.mysqlconnector import MysqlConnector
connector = MysqlConnector()

def armas_por_tempo_area(sql, dataInicial, dataFinal, areas_nome):
    areas_id = None
    if len(areas_nome) > 0: 
        areas_id = [areas[i] for i in areas_nome]
    return sql.obter_armas_por_tempo_aera(dataInicial, dataFinal, areas_id)

def obter_listagem_areas(sql):
    return sql.obter_listagem_areas()

def processar_datas(data_inicio, data_fim):
    st.write(f"Processando dados entre {data_inicio} e {data_fim}")
    return


st.title("Qual é o histórico das armas mais prevalentes em diferentes regiões ao longo de um período específico?")

areas = obter_listagem_areas(connector)
data_inicio = st.date_input("Selecione a data de início", pd.to_datetime('2022-01-01'))
data_fim = st.date_input("Selecione a data de fim", pd.to_datetime('2022-12-31'))

areas_selecionadas = st.multiselect(label="Selecione as áreas", options=areas.keys())

#

if st.button("Processar Dados"):
    processar_datas(data_inicio, data_fim)
    armas_resultado = armas_por_tempo_area(connector, dataInicial=data_inicio,dataFinal=data_fim, areas_nome=areas_selecionadas)
    df = pd.DataFrame(armas_resultado, columns=["Tipo da arma","Quantidade"])
    
    # Ordenar o DataFrame pela coluna "Quantidade" em ordem decrescente
    df = df.sort_values(by="Quantidade", ascending=False)
    
    # Selecionar as 10 categorias mais expressivas
    top_10_df = df.head(10)

    # Gráfico de barras
    st.header("Top 10 armas mais utilizadas")
    
    # Personalizando aparência do gráfico
    cor_roxa = '#8a2be2'  
    plt.bar(top_10_df["Tipo da arma"],top_10_df["Quantidade"], color=cor_roxa, edgecolor='black', linewidth=1.2)

    # Adicionar rótulos e título com tamanhos de fonte maiores
    plt.xlabel('Armas', fontsize=8)
    plt.ylabel('Quantidade', fontsize=14)
    plt.title('Quantidade por Armas', fontsize=16)
    plt.xticks(rotation=45, ha="right")  
    
    # Adicionar grade
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    
    # Ajustar o layout para evitar cortar rótulos
    plt.tight_layout()
    st.pyplot(plt)

    # Dataframe de todos os resultados
    st.header("Armas ordenadas pela quantidade de crimes")
    st.dataframe(df)
  