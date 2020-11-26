UPDATE users
SET
telegram_id = (%(sender_id)s)
WHERE
email = (
    SELECT email FROM current_transaction
    WHERE telegram_id = (%(sender_id)s)
    LIMIT 1
);

DELETE FROM current_transaction
WHERE telegram_id = (%(sender_id)s);
