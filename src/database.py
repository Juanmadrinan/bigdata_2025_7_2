import os
import datetime
import sqlite3
import pandas as pd

class Database:
    def __init__(self):
        self.db_name = "src/static/db/exchangerate.db"
        self.create_database()

    def create_database(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasas_cambio (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha_captura DATETIME DEFAULT CURRENT_TIMESTAMP,
                pais TEXT UNIQUE,
                valor REAL
            )
        ''')
        except Exception as err:
            print("Fallo, capturamos error en la creacion de la base de datos")

    def insert_database(self, df: pd.DataFrame):
        """
        Inserta los datos del DataFrame en la tabla tasas_cambio.
        Asume que el DataFrame tiene una única fila donde las columnas son los países
        y los valores son las tasas de cambio.
        """
        try:
            if not df.empty:
                # Iterar a través de las columnas del DataFrame (que son los países)
                for pais, valor in df.iloc[0].items():
                    self.cursor.execute(
                        "INSERT OR REPLACE INTO tasas_cambio (pais, valor) VALUES (?, ?)",
                        (pais, valor)
                    )
                self.conn.commit()
                print("Datos insertados en la base de datos.")
            else:
                print("El DataFrame está vacío, no se insertaron datos.")

        except sqlite3.Error as e:
            print(f"Error al insertar datos en la base de datos: {e}")
            self.conn.rollback()  # Revertir cualquier cambio en caso de error

    def close_database(self):
        if self.conn:
            self.conn.close()
        else:
            print("No hay conexión para cerrar.") # O manejar de otra forma
