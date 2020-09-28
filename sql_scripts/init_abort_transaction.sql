UPDATE current_transaction
SET
previous_transaction_state = (%(previous_transaction_state)s),
transaction_state = 5
WHERE
u_id = (%(sender_id)s);
