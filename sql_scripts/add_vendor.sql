UPDATE current_transaction
SET
transaction_state = 3,
vendor = (%(vendor)s)
WHERE
u_id = (%(sender_id)s);