SELECT transaction_state FROM current_transaction
WHERE telegram_id = (%(sender_id)s);