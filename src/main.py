from datapi import DatApi
from database import Database
import pandas as pd

def main():

    df = pd.DataFrame()
    datapi = DatApi()
    database = Database()
    df = datapi.getData()
    df.to_csv('src/static/csv/tasas_de_cambio.csv', index=False, encoding='utf-8')
    
    nombre_tabla = "Tazas de Cambio del Dolar"
    database.insert_database(df)

    print("******** Datos insertados en la base datos tabla: {}*********".format(nombre_tabla))
    print("******** Impresion de los datos ********")
    print(df.shape)
    print(df.head())

    database.close_database()

if __name__ == "__main__":
    main()