/* This script initiallizes the following tables/relations:*/

--transactions: This table records all the individual spending that a user commits to the application.
--users: This table holds the telegram unique id of all the people who are subscribed to the application.
--current_transaction: This table stores the state of current ongoing transactions.

DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS current_transaction;
DROP TABLE IF EXISTS users;


CREATE TABLE IF NOT EXISTS users(   
	id BIGINT NOT NULL PRIMARY KEY UNIQUE                --primary key, unique, numeric id give by telegram to each user
);

CREATE TABLE IF NOT EXISTS transactions(
	id SERIAL NOT NULL PRIMARY KEY UNIQUE,                --primary key
	u_id BIGINT NOT NULL REFERENCES users (id),           --foreign key, id of the user who committed the transaction
	item TEXT NOT NULL,
	price DECIMAL NOT NULL CHECK(price > 0),
	vendor TEXT,
	category TEXT,                          
	date_of_purchase DATE DEFAULT CURRENT_DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS current_transaction(
	u_id BIGINT NOT NULL PRIMARY KEY UNIQUE,
	transaction_state INTEGER NOT NULL,
	previous_transaction_state INTEGER,
	item TEXT,
	price DECIMAL CHECK(price > 0),
	vendor TEXT,
	category TEXT
)

