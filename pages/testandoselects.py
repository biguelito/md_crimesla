import streamlit as st
import pandas as pd 
import mysql.connector
#conetando ao datawarehouse 
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="dw_crimesla"
)
# Executa a consulta SQL e armazena os dados em um DataFrame
df = pd.read_sql_query("SELECT * FROM dim_arma_crime", connection)

# Exibe os dados em uma tabela usando o Streamlit
st.dataframe(df)

