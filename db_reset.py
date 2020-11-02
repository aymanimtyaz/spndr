import psycopg2 as pg2
import os
from config import user, password

""" CONNECTING TO POSTGRESQL DATABASE """
conn = pg2.connect(database='spndr', user=user, password=password)
cur = conn.cursor()


""" EXECUTING DATABASE RESET SCRIPT """
reset_script = open(os.getcwd()+'\\sql_scripts\\reset_db.sql').read()
cur.execute(reset_script)


""" COMMITTING CHANGES AND CLOSING THE CONNECTION """
conn.commit(); cur.close(); conn.close()

print("DONE")