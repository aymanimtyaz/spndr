from psycopg2 import pool as pl
import os

from config import user, password, host

class DatabaseConnection:

    database = 'spndr'
    min_con = '1'
    max_con = '1'

    def __init__(self):
        self.connection_pool = pl.SimpleConnectionPool(
            self.min_con, self.max_con, database = self.database, 
            user = user, host = host, password = password, 
            application_name = f'spndr_telegram::{os.getpid()}')

    def __enter__(self):
        self.con = self.connection_pool.getconn()
        return self.con.cursor()

    def __exit__(self, exec_type, exec_val, exec_traceback):
        self.con.commit()
        self.connection_pool.putconn(self.con)

dbc = DatabaseConnection()
