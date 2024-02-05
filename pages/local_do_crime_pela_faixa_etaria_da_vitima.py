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
    
    
    # Limitar o número de caracteres no eixo X
    max_chars = 25
    top_10_df.loc[:,"Localidade"] = top_10_df["Localidade"].apply(lambda x: x[:max_chars] + "..." if len(x) > max_chars else x)
    # Criar gráfico de barras
    cor_roxa = '#8a2be2'  
    plt.bar(top_10_df["Localidade"], top_10_df["Quantidade"], color=cor_roxa, edgecolor='black', linewidth=1.2)
    
    # Adicionar rótulos e título com tamanhos de fonte maiores
    plt.xlabel('Localidade', fontsize=8)
    plt.ylabel('Quantidade', fontsize=14)
    plt.title('Quantidade por locais', fontsize=16)
    # Adicionar grade
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    
    # Ajustar o layout para evitar cortar rótulos
    plt.tight_layout()
    # Exibir gráfico no Streamlit
    st.header("Os dez locais de crime mais recorrentes")
    plt.xticks(rotation=45, ha="right") 
    st.pyplot(plt)
    
    # Dados resultantes ordenados
    st.header("Locais de crime ordenados pela quantidade de crimes")
    st.dataframe(df)
  