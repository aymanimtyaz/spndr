UPDATE current_transaction
SET
transaction_state = 4,
category = (%(category)s)
WHERE
telegram_id = (%(sender_id)s);