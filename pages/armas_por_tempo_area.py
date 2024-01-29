import pandas as pd
import mysql.connector
import streamlit as st
from sqlalchemy import create_engine

# Cria uma conexão com o banco de dados MySQL
# engine = create_engine('mysql+mysqlconnector://root:password@localhost/dw_crimesla')

# Carrega a query do arquivo SQL e executa a consulta SQL
# query = pd.read_sql_query("sql/scripts/teste_armas_por_tempo_area.sql", engine)

# Exibe os dados em uma tabela usando o Streamlit
# st.dataframe(query)