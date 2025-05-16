import os
import datetime
import sqlite3
import pandas as pd

class Database:
    def __init__(self):
        self.db_name = "bigdata_2025_7_2/src/static/db/exchangerate.db"
        self.create_database()

    def create_database(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
        except Exception as err:
            print("Fallo, capturamos error en la creacion de la base de datos")

    def close_database(self):
        if self.conn:
            self.conn.close()
        else:
            print("No hay conexión para cerrar.") # O manejar de otra forma
