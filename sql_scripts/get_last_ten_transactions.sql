SELECT item, price, vendor, date_of_purchase
FROM transactions
WHERE u_id = (%(sender_id)s)
ORDER BY id DESC LIMIT 10;