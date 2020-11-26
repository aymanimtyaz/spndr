INSERT INTO transactions(id, item, price, vendor, category)
VALUES
((%(user_id)s), 

 (SELECT item
  FROM current_transaction
  WHERE telegram_id = (%(sender_id)s)
  LIMIT 1), 
  
 (SELECT price
  FROM current_transaction
  WHERE telegram_id = (%(sender_id)s)
  LIMIT 1), 

 (SELECT vendor
  FROM current_transaction
  WHERE telegram_id = (%(sender_id)s)
  LIMIT 1), 

 (SELECT category
  FROM current_transaction
  WHERE telegram_id = (%(sender_id)s)
  LIMIT 1)
);

DELETE FROM current_transaction
WHERE telegram_id = (%(sender_id)s);