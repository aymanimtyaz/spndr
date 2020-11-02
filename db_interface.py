import psycopg2 as pg2
from psycopg2 import pool as pl
from config import user, password

class pool_init:
    
    data = 'spndr'
    usr = user
    pw = password
    min_con = '1'
    max_con = '1'

    def __init__(self, function):
        self.connection_pool = pl.SimpleConnectionPool(self.min_con, self.max_con, database = self.data, 
                                                             user = self.usr, password = self.pw)
        self.function = function

    def __call__(self, *args, **kwargs):
        return self.function(self.connection_pool, args, kwargs)

@pool_init
def cnnct(*args):
    con_obj = args[0].getconn()
    cur_obj = con_obj.cursor()
    return args[0], con_obj, cur_obj

def dscnnct(pool, con, curs):
    con.commit()
    curs.close()
    pool.putconn(con)