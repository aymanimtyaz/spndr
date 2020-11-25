SELECT hashed_password FROM users 
WHERE email = (
SELECT email FROM current_transaction
WHERE telegram_id = (%(sender_id)s)
LIMIT 1) LIMIT 1;