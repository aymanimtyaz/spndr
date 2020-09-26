SELECT transaction_state FROM current_transaction
WHERE u_id = (%(sender_id)s);