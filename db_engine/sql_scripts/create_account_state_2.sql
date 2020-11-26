UPDATE current_transaction
SET
transaction_state = 2
WHERE
telegram_id = (%(sender_id)s);