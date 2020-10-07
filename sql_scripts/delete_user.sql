DELETE FROM transactions
WHERE u_id = (%(sender_id)s);

DELETE FROM users
WHERE id = (%(sender_id)s);

DELETE FROM current_transaction
WHERE u_id = (%(sender_id)s);