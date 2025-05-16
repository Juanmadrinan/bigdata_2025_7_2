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
        except Exception as err:
            print("Fallo, capturamos error en la creacion de la base de datos")

    def close_database(self):
        self.conn.close()