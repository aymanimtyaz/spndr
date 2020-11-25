SELECT item, price, vendor, date_of_purchase
FROM transactions
WHERE id = (%(id)s)
ORDER BY id DESC LIMIT 10;