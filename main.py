import os
from dotenv import load_dotenv
from sql.mysqlconnector import MysqlConnector
import datetime

def main():
    dataInicial = datetime.date(2020, 1, 1)
    dataFinal = datetime.date(2023, 10, 30)
    cidades= [15, 6]

    connector = MysqlConnector()
    dados = connector.obter_local_perigoso_por_faixa_etaria('Jovem')
    for dado in dados:
        print(dado)
    return

if __name__ == '__main__':
    main()