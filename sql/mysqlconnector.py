import os
import mysql.connector

class MysqlConnector:
    _instance = None
    _criado = False
    
    def __init__(self) -> None:
        self.dw = mysql.connector.connect(
            user=os.getenv('USER'), 
            password=os.getenv('PASSWORD'),
            host=os.getenv('HOST'),
            database=os.getenv('DATABASE_DW')
        )

    def obter_armas_por_tempo_aera(self, dataInicial, dataFinal, cidades):
        resultado = []
        format_strings = ','.join(['%s'] * len(cidades))
        params = [dataInicial, dataFinal] + cidades
        
        file = open('sql/scripts/armas_por_tempo_area.sql', encoding='utf-8') 
        script = file.read() 
        file.close()
        script = script.replace('#areas#', format_strings)
        
        cursor = self.dw.cursor()
        cursor.execute(script, params)    
        resultado = list(map(list, cursor.fetchall()))
        cursor.close()
        
        return resultado
    

