UPDATE current_transaction
SET
transaction_state = 2,
price = (%(price)s)
WHERE
telegram_id = (%(sender_id)s);