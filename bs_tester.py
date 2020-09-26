import psycopg2 as pg2 

con = pg2.connect(database='spndr', user='postgres', password='password')
cur = con.cursor()

cur.execute('''UPDATE current_transaction
               SET
               transaction_state = 1,
               item = (%(prod_serv)s)
               WHERE u_id = (%(sender_id)s);
''', {"sender_id":1152426782, "prod_serv":"Skamteboard"})

