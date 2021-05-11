SELECT EXISTS (SELECT * FROM chatbot_users WHERE client = 'telegram' AND client_id = (%(sender_id)s));
