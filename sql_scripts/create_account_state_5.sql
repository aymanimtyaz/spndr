UPDATE current_transaction
SET
transaction_state = 5,
email = (%(email)s)
WHERE
telegram_id = (%(sender_id)s);