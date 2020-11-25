DELETE FROM current_transaction
WHERE
telegram_id = (%(sender_id)s);