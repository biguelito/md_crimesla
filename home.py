import streamlit as st
import os
from dotenv import load_dotenv
from sql.mysqlconnector import MysqlConnector
import datetime

def armas_por_tempo_area():
    connector = MysqlConnector()
    dataInicial = datetime.date(2020, 1, 1)
    dataFinal = datetime.date(2023, 10, 30)
    cidades= [15, 6]
    return connector.obter_armas_por_tempo_aera(dataInicial, dataFinal, cidades)


st.set_page_config(
    page_title = "M.D - CrimesLA - por Gabriel Reis e Washington Rocha",
    layout = "wide",
    menu_items = {
        'About': '''Projeto para a cadeira de modelagem de dados da professora 
        Ceça Maria feito pelos alunos: Gabriel Reis e Washington Rocha.
        '''
    }
)
st.markdown(f'''
    <h1>Projeto de M.D - CrimesLA</h1>
    <br>
    No âmbito da análise de dados, compreender e interpretar os padrões de criminalidade
            em uma região é crucial para o desenvolvimento de estratégias eficazes de 
            segurança pública. Este projeto de análise de dados tem como foco o banco de 
            dados de crimes de Los Angeles no ano de 2020, buscando lançar luz sobre o 
            cenário de estudo e proporcionar insights valiosos para formuladores de políticas, 
            pesquisadores e cidadãos interessados.
    <br>
    <h2>Alunos</h2>
    <ul>
            <li>Gabriel Reis</li>
            <li>Washington Rocha</li>
    </ul>

''', unsafe_allow_html=True)
st.write(armas_por_tempo_area())