import streamlit as st

def build_header():
    text ='''<h1>Header</h1>
    <p>Exemplo de paragrafo no cabeçalho.</p>
    '''
    st.write(text, unsafe_allow_html=True)

def build_body():
    text ='''
    <h2>Body</h2>
    <p>
    Exemplo de paragrafo no corpo da página.
    </P>
    '''
    st.write(text, unsafe_allow_html=True)

build_header()
build_body()