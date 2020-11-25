UPDATE users
set
telegram_id = NULL
WHERE
telegram_id = (%(sender_id)s);

DELETE FROM current_transaction
WHERE telegram_id = (%(sender_id)s);