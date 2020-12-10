UPDATE users
SET
telegram_id = (%(sender_id)s)
WHERE
email = (%(email)s)