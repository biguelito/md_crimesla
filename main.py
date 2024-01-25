from dotenv import load_dotenv
from sql.mysqlconnector import MysqlConnector
import datetime

def armas_por_tempo_area(dataInicial, dataFinal, cidades):
    connector = MysqlConnector()
    armas = connector.obter_armas_por_tempo_aera(dataInicial, dataFinal, cidades)
    for arma in armas:
        print(arma)
    return

def main():
    load_dotenv('.env')
    dataInicial = datetime.date(2020, 1, 1)
    dataFinal = datetime.date(2023, 10, 30)
    cidades= [15, 6]
    armas_por_tempo_area(dataInicial, dataFinal, cidades)
    return

if __name__ == '__main__':
    main()