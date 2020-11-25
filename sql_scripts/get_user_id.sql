SELECT id FROM users
WHERE telegram_id = (%(sender_id)s);
