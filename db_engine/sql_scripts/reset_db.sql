DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users(   
	id SERIAL NOT NULL PRIMARY KEY UNIQUE,                
    email VARCHAR(64) NOT NULL UNIQUE,
    telegram_id BIGINT UNIQUE,
    hashed_password VARCHAR(150) NOT NULL
);

CREATE INDEX users_id_idx ON users(id);
CREATE INDEX users_email_idx ON users(email);
CREATE INDEX users_telegram_id_idx ON users(telegram_id);

CREATE TABLE IF NOT EXISTS transactions(
	t_id SERIAL NOT NULL PRIMARY KEY UNIQUE,                
	id BIGINT NOT NULL REFERENCES users (id),           
	item TEXT NOT NULL,
	price DECIMAL NOT NULL CHECK(price > 0),
	vendor TEXT,
	category TEXT,                          
	date_of_purchase DATE DEFAULT CURRENT_DATE NOT NULL
);

CREATE INDEX transactions_id_idx on transactions(id);

--REDACTED
-- CREATE TABLE IF NOT EXISTS current_transaction(
-- 	telegram_id BIGINT NOT NULL PRIMARY KEY UNIQUE,
-- 	email VARCHAR(64),
-- 	hashed_password VARCHAR(150),
-- 	transaction_state INTEGER NOT NULL,
-- 	previous_transaction_state INTEGER,
-- 	item TEXT,
-- 	price DECIMAL CHECK(price > 0),
-- 	vendor TEXT,
-- 	category TEXT
-- )

