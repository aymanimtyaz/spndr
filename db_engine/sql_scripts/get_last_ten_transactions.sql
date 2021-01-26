SELECT item, price, vendor, date_of_purchase
FROM transactions
WHERE id = (%(user_id)s)
ORDER BY t_id DESC LIMIT 10;