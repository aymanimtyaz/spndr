import psycopg2 as pg2
import os
try:
    from spndr_tg.config import user, password, host
except ModuleNotFoundError:
    from config import user, password, host


def reset():
    """ CONNECTING TO POSTGRESQL DATABASE """
    conn = pg2.connect(database='spndr', user=user, host=host, password=password)
    cur = conn.cursor()


    """ EXECUTING DATABASE RESET SCRIPT """
    reset_script = open(os.path.dirname(__file__)+'/db_engine/sql_scripts/reset_db.sql').read()
    cur.execute(reset_script)


    """ COMMITTING CHANGES AND CLOSING THE CONNECTION """
    conn.commit(); cur.close(); conn.close()

    print("DONE")

if __name__ == '__main__':
    reset()

