UPDATE current_transaction
SET
hashed_password = (%(hashed_password)s)
WHERE
telegram_id = (%(sender_id)s);

INSERT INTO users(email, telegram_id, hashed_password)
SELECT email, telegram_id, hashed_password FROM current_transaction
WHERE
telegram_id = (%(sender_id)s)
LIMIT 1;

DELETE FROM current_transaction
WHERE telegram_id = (%(sender_id)s);




