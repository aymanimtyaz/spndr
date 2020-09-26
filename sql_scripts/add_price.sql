UPDATE current_transaction
SET
transaction_state = 2,
price = (%(price)s)
WHERE
u_id = (%(sender_id)s);