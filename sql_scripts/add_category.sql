UPDATE current_transaction
SET
transaction_state = 4,
category = (%(category)s)
WHERE
u_id = (%(sender_id)s);