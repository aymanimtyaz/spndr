INSERT INTO transactions(id, item, price, vendor, category)
VALUES
(
    (SELECT id FROM chatbot_users
     WHERE client = 'telegram' AND client_id = (%(sender_id)s)),
    
    (%(item)s),

    (%(price)s),

    (%(vendor)s),

    (%(category)s)
);