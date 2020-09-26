INSERT INTO transactions(u_id, item, price, vendor, category)
SELECT u_id, item, price, vendor, category 
FROM current_transaction
WHERE u_id = (%(sender_id)s);

