UPDATE current_transaction
SET
transaction_state = previous_transaction_state,
previous_transaction_state = NULL
WHERE
telegram_id = (%(sender_id)s);