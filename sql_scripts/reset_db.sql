/* This script initiallizes the following tables/relations:*/

--transactions: This table records all the individual spending that a user commits to the application.
--categories: This table holds all the different categories of transactions that the user has defined.


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
)