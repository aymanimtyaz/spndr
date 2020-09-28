SELECT EXISTS (SELECT * FROM users WHERE id = (%(sender_id)s));
