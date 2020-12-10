INSERT INTO transactions(id, item, price, vendor, category)
VALUES
(
    (SELECT id FROM users
     WHERE telegram_id = (%(sender_id)s)),
    
    (%(item)s),

    (%(price)s),

    (%(vendor)s),

    (%(category)s)
);