from datapi import DatApi
from database import Database
def main():

    datapi = DatApi()
    database = Database()
    df = datapi.getData()
    df.to_csv('bigdata_2025_7_2/src/static/csv/tasas_de_cambio.csv', index=False, encoding='utf-8')
    database.close_database()

if __name__ == "__main__":
    main()