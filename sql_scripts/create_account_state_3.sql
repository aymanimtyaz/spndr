UPDATE current_transaction
SET
transaction_state = 3
WHERE
telegram_id = (%(sender_id)s);