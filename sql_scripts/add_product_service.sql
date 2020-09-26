UPDATE current_transaction
SET
transaction_state = 1,
item = (%(prod_serv)s)
WHERE
u_id = (%(sender_id)s);
