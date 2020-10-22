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
This is the starter file for the program. **The app gets initialized and starts executing when this file is run**. The steps laid out above are executed in this file.

### 2. message_processor.py
This is the file that **handles the processing of the end users' messages to the bot**. It is the working brain of the application.
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
This file opens the bot's reply templates stored in the _replies_ directory and returns them to message_processor.py when called upon.

### 8. reset_db.py
This file resets the PostgreSQL database 


## Control Flow Diagram
![CONTROL FLOW DIAGRAM](https://i.ibb.co/30MxhN0/DATA-FLOW-DIAGRAM.png)
## PostgreSQL Database Schema
![DATABASE SCHEMA](https://i.ibb.co/dr5389N/DATABASE-SCHEMA.png)

# Running Instructions
1. Make sure you have Python installed with the **_psycopg2_** and **_requests_** package.
2. Make sure you have PostgreSQL installed.
3. Clone this repo.  
4. Create a config.py file in the repo and add the following variables to it:
    a. __*bot_token*__: A string containing the Telegram API key for the bot. Click this link to see how you can get an API key: https://core.telegram.org/#bot-api
    b. __*user*__: A string containing the username of your PostgreSQL server.
    c. __*password*__: A string containing the password of your PostgreSQL server.
5. Create a PostgreSQL database and name it 'spndr'.
6. Run reset_db.py to initialize the database.
7. Run tester.py and send the bot a message. 
8. That's it! You're all done!


#### If you have any questions about this project, you can email me at aymanimtyaz@gmail.com :)