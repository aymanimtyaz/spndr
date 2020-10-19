# Welcome to spndr!

## What is spndr?

**spndr** is a spending tracker built in **Python**, using a **PostgreSQL** database in the backend and using **Telegram** as the frontend, via the **Telegram bot API**. spndr is a telegram bot that can help you record your spending details in a simple, step-by-step process.

## How it works

The program logic of the bot is fairly simple. 
1. The bot receives an update via the Telegram API of any messages sent to it. 

2. Once it has received a message, it processes the message which consists of :
    a. Doing any necessary back-end work, mostly database transactions.
    b. Selecting the reply to send to the end user from a folder of reply templates.

3. Sends the reply selected in step 2b. above to the user.

 And the process repeats.
 
 ## File functionality
 This is a brief description of each file in its current state:
 
 ### 1. tester.py
 This is the starter file for the program. **The app gets initialized and starts executing when this file is run**. The steps laid out above are 
 executed in this file.

### 2. message_processor.py
This is the file that **handle's the processing of the end users' messages to the bot**. It is the working brain of the application.
End users' messages are processed followed by carrying out any necessary database operations, and then the message to be sent back to the end users is generated.

### 3. database_operations.py
This file calls the **psycopg2 wrapper module, _db_interface.py_** and carries out various specific database operations such as adding and deleting users, retrieving previous transaction info, etc. 
It opens the required **.sql file stored in the _sql_scripts_ directory** to carry out a database operation as and when called upon by message_processor.py to do so.

### 4. db_interface.py
This file is a module that acts as wrapper for the **psycopg2 library; A PostgreSQL database adapter module for Python**. It consists of class **pool_init()** and two standalone functions; **cnnct()** and **dscnnct()**. 
The  pool_init class is a **_decorator class_** for the cnnct() function. 

When cnnct() is called for the first time, **pool_init() creates a psycopg2 connection pool object** and passes it to cnnct() from which it can get connection objects and cursors and pass them on to  database_operations.py when called upon. The cursor is then used to perform the required database query. After the query is complete. The dscnnct() function is called that commits any changes, closes the cursor object, and puts the connection object back into the connection pool.

### 5. api_caller.py
This file calls the functions in **telegrambot.py**, which is a wrapper module that implements the Telegram bot API. It **parses the json object returned from telegrambot.py** for necessary info and passes the info onwards.

### 6. telegrambot.py
This is a wrapper module that implements the Telegram bot API functions **getUpdates** and **sendMessage**

### 7. replies.py
This file open's the bot's reply templates stored in the _replies_ directory and return's them to message_processor.py when called upon.

## Running Instructions
1. Make sure you have Python 3.7 installed with the psycopg2 package
2. Make sure you have PostgreSQL installed 
3. download this repo
4. create a file named bot_token.txt in the repo and paste your telegram API key in it.
Click this link to see how you can get an API key: https://core.telegram.org/#bot-api
5. Open db_interface.py and change the class variables username and password in the pool_init class to the username and password of your PostgreSQL server.
6. run tester.py and send the bot a message. 
7. That's it! You're all done!


#### If you have any questions about this project, you can email me at aymanimtyaz@gmail.com :)
