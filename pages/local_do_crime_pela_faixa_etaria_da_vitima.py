import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sql.mysqlconnector import MysqlConnector
connector = MysqlConnector()


st.title("Quais são os locais mais propensos a crimes envolvendo a faixa etaria da vitima?")

faixas_etarias = ['Todos','Jovem','Adulto','Idoso']
faixa_selecionada = st.selectbox(label="Selecione a faixa etária",
                                 options=faixas_etarias,
                                 placeholder='Selecione')
if st.button("Processar Dados"):
    st.write("Exibindo resultados na faixa etária: "+faixa_selecionada)
    resultado = connector.obter_local_perigoso_por_faixa_etaria(faixa_selecionada)
    df = pd.DataFrame(resultado,columns=["Localidade","Quantidade"])
    top_10_df = df.head(10)
    st.header("Tabela de Dados")
    st.dataframe(df)
    # Criar gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(top_10_df["Localidade"], top_10_df["Quantidade"])

    # Adicionar rótulos e título
    ax.set_xlabel("Localidade")
    ax.set_ylabel("Quantidade de Crimes")
    ax.set_title("Quantidade de Crimes por Local")

    # Exibir gráfico no Streamlit
    st.pyplot(fig)
    
  