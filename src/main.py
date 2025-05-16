from datapi import DatApi

def main():
    datapi = DatApi()

    df = datapi.getData()
    df.to_csv('bigdata_2025_7_2/src/static/csv/tasas_de_cambio.csv', index=False, encoding='utf-8')

if __name__ == "__main__":
    main()