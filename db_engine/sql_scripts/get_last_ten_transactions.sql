SELECT item, price, vendor, date_of_purchase
FROM transactions
WHERE id = (%(user_id)s)
ORDER BY id DESC LIMIT 10;