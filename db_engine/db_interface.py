import psycopg2 as pg2
from psycopg2 import pool as pl
import os

try:    
    from spndr_tg.config import user, password, host
except:
    from config import user, password, host

# REDACTED
# class pool_init:
    
#     data = 'spndr'
#     min_con = '1'
#     max_con = '1'

#     def __init__(self, function):
#         self.connection_pool = pl.SimpleConnectionPool(self.min_con, self.max_con, database = self.data, 
#                                                              user = user, host = host, password = password)
#         self.function = function

#     def __call__(self, *args, **kwargs):
#         return self.function(self.connection_pool, args, kwargs)

# @pool_init
# def cnnct(*args):
#     con_obj = args[0].getconn()
#     cur_obj = con_obj.cursor()
#     return args[0], con_obj, cur_obj

# def dscnnct(pool, con, curs):
#     con.commit()
#     curs.close()
#     pool.putconn(con)

class db_connection:

    database = 'spndr'
    min_con = '1'
    max_con = '1'

    def __init__(self):
        self.connection_pool = pl.SimpleConnectionPool(self.min_con, self.max_con, database = self.database, 
                                                       user = user, host = host, password = password, application_name = f'spndr_telegram::{os.getpid()}')
    
    def cnnct(self):
        db_connection = self.connection_pool.getconn()
        db_cursor = db_connection.cursor()
        return db_connection, db_cursor

    def dscnnct(self, db_connection, db_cursor):
        db_connection.commit()
        db_cursor.close()
        self.connection_pool.putconn(db_connection)

dbc = db_connection()
