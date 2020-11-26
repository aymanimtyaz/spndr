SELECT EXISTS (SELECT * FROM users WHERE telegram_id = (%(sender_id)s));
