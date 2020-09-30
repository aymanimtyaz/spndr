'''import psycopg2 as pg2 

con = pg2.connect(database='spndr', user='postgres', password='password')
cur = con.cursor()

cur.execute(''' '''SELECT item, price, vendor, category
               FROM transactions
               WHERE u_id = (%(sender_id)s)
               ORDER BY id DESC LIMIT 10
''' ''', {"sender_id":1152426782})

dicto = cur.fetchmany(10)
print(dicto)'''

sentence = "Elanor is crazy"
article = 'An' if sentence.lower().startswith('a') or if sentence.lower().startswith('e') or if sentence.lower().startswith('i') or if sentence.lower().startswith('o') or if sentence.lower().startswith('u') else 'A'
print(article)





