INSERT INTO users(email, telegram_id, hashed_password)
VALUES
((%(email)s), (%(sender_id)s), (%(hashed_password)s));
