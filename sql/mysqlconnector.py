import os
import mysql.connector

class MysqlConnector:
    _instance = None
    _criado = False
    
    def __init__(self) -> None:
        self.dw = mysql.connector.connect(
            user= 'root',#os.getenv('USER'), 
            password= 'Mysql@123',#os.getenv('PASSWORD'),
            host= 'localhost', #os.getenv('HOST'),
            database= 'dw_crimesla' #os.getenv('DATABASE_DW')
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
    
    def obter_listagem_areas(self):
        resultado_dict = {}
        file = open('sql/scripts/listagem_areas.sql', encoding='utf-8') 
        script = file.read() 
        file.close()

        cursor = self.dw.cursor()
        cursor.execute(script)    
        resultado = list(map(list, cursor.fetchall()))
        cursor.close()

        resultado_dict['id'] = [i[0] for i in resultado]
        resultado_dict['nome'] = [i[1] for i in resultado]

        return resultado_dict