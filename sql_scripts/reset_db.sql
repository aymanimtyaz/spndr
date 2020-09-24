/* This script initiallizes the following tables/relations:*/

--transactions: This table records all the individual spending that a user commits to the application.
--categories: This table holds all the different categories of transactions that the user has defined.
--users: This table holds the telegram usernames of all the people who are subscribed to the application.

CREATE TABLE IF NOT EXISTS transactions(
	id SERIAL NOT NULL PRIMARY KEY UNIQUE,                --primary key
	item TEXT NOT NULL,
	price INTEGER CHECK(price > 0),
	vendor TEXT,
	category_id INTEGER NOT NULL,                         --foreign key, points to the id in the categories table
	date_of_purchase DATE DEFAULT CURRENT_DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS categories(
	id SERIAL NOT NULL PRIMARY KEY UNIQUE,                --primary key
	category TEXT NOT NULL UNIQUE,
	descr TEXT
);

CREATE TABLE IF NOT EXISTS users(   
	id BIGINT NOT NULL PRIMARY KEY UNIQUE,                --primary key, unique, numeric id give by telegram to each user
	username TEXT UNIQUE                                  --unique telegram username of the user
)
