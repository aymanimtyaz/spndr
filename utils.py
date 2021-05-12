from db_interface import dbc

def generate_show_reply(sender_id):
    sql = (
        """
        SELECT item, price, vendor, date_of_purchase
        FROM transactions
        WHERE id = (
            SELECT id FROM chatbot_users
            WHERE client='telegram'
            AND client_id=(%(sender_id)s)
        )
        ORDER BY t_id DESC LIMIT 10;
        """)
    with dbc as curs:
        curs.execute(sql, {"sender_id":str(sender_id)})
        spending_data = curs.fetchall()
    if len(spending_data) == 0:
        return (
            """
            You haven't shared any of your
            spending data with us yet. 
            Send /new to share your spending
            data.
            """)
    ret_str = ''; i=1
    for row in spending_data:
        article = 'An' if row[0].lower()[0] in ['a', 'e', 'i', 'o', 'u'] else 'A'
        if row[0].lower().endswith('s'):
            article = '' 
        ret_str+=str(i)+str(". {} {} for {} dollars from {} on {}.".format(article, row[0], row[1], row[2], row[3])+'\n\n')
        i+=1
    return "Your last 10 transaction:\n"+ret_str