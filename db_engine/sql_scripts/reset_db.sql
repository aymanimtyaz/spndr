DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS oauth_users;
DROP TABLE IF EXISTS chatbot_users;
DROP TABLE IF EXISTS users;


CREATE TABLE IF NOT EXISTS users(   
	id SERIAL NOT NULL PRIMARY KEY UNIQUE,                
    email VARCHAR(64) UNIQUE,
    hashed_password VARCHAR(150)
);

CREATE INDEX users_id_idx ON users(id);
CREATE INDEX users_email_idx ON users(email);

CREATE TABLE IF NOT EXISTS oauth_users(
	oauth_provider VARCHAR(35) NOT NULL,
	oauth_provider_id VARCHAR(100) NOT NULL PRIMARY KEY UNIQUE,
	id BIGINT NOT NULL REFERENCES users (id),
	oauth_token VARCHAR(500),
	oauth_token_refresh VARCHAR(500)
);

CREATE INDEX oauth_users_id_idx ON oauth_users(id);

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

CREATE TABLE IF NOT EXISTS chatbot_users(
	client VARCHAR(100) NOT NULL,
	client_id VARCHAR(200) NOT NULL,
	id BIGINT NOT NULL UNIQUE PRIMARY KEY REFERENCES users(id),
	UNIQUE(client, client_id)
);

CREATE INDEX chatbot_users_id_idx on chatbot_users(id);
