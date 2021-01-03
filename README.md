# spndr - I.M. based spending tracker
A simple spending tracker that can be used from an instant messenger.
Built using Python (Flask), PostgreSQL and Redis. Currently supports Telegram.


## Table of Contents
* [Requirements and Setup](#requirements-and-setup)
* [Working](#working)
* [Modules and Functionality](#modules-and-functionality)



## Requirements and Setup 
### Software Requirements
1. OS - Ubuntu Linux
2. Python 3.8.5
3. PostgreSQL 12.5
4. Redis 6.0.9
5. Ngrok 2.3.35
### Python Dependencies
1. flask
2. flask-bcrypt
3. email-validator
4. psycopg2
5. redis
6. requests
### Setup
1. Make sure you have PostgreSQL and Redis installed and running in the background.
2. Start an ngrok tunnel to your localhost on your preferred port, for example, a public url to port 5000 on your local host can be created as such:

```
./ngrok http 5000
```
	
3. Copy the https forwarding link that is generated:
```
ngrok by @inconshreveable                                                                                                     (Ctrl+C to quit)
                                                                                                                                              
Session Status                online                                                                                                          
Account                       ##################### (Plan: Free)                                                                              
Version                       2.3.35                                                                                                          
Region                        United States (us)                                                                                              
Web Interface                 http://127.0.0.1:4040                                                                                           
Forwarding                    http://############.ngrok.io -> http://localhost:5000                                                           
Forwarding                    https://############.ngrok.io -> http://localhost:5000                                                          
                                                                                                                                              
Connections                   ttl     opn     rt1     rt5     p50     p90                                                                     
                              0       0       0.00    0.00    0.00    0.00                                                                    
                                                                                                                      
```
                              
5. create a file; **config.py** in the repo and add the following variables to it:
- **_bot_token_**: A string containing the Telegram API key for the bot. Click this link to see how you can get an API key: [https://core.telegram.org/#bot-api](https://core.telegram.org/#bot-api)
- **_user_**: A string containing the username of your PostgreSQL server.
- **_password_**: A string containing the password of your PostgreSQL server.
- _**host**_: the hostname (string) for telegram to push updates to via a webhook, should be _**localhost**_ for now.
- _**webhook_url**_: the url (string) obtained in step 4 from ngrok
- _**webhook_port**_: the same port (integer) used in step 4
```
'''
config.py
CONFIGURATION FILE FOR SPNDR
'''
bot_token = 'bot API token here'
user = 'PostgreSQL server username here'
password = 'PostgreSQL password here'
host = 'localhost'
webhook_url = 'ngrok https link here'
webhook_port = 1234 #Replace 1234 with your port number
```
6. Run db_reset.py to initiallize the Postgres database.
7. Run initiallize_webhook.py to send telegram the webhook url which is the ngrok url generated in step 4
8. Run webhook_endpoint_starter.py in the background
9. Run main_webhook.py
10. The app is up and running! Try sending your bot a message. 
## Working
The operation of the bot is fairly simple. Whenever someone sends a message to the bot. Telegram forwards the message to us via the ngrok webhook url.
On our localhost, the message is pushed into a Redis queue via the flask app defined in ***webhook_endpoint_starter.py*** . The message is popped out of the Redis queue and processes by ***main_webhook.py***. Any necessary backend work is done and a reply is sent back to the sender on telegram. 
The above process continues in a loop.
## Modules and Functionality
The app has 4 main modules that are called when main_webhook.py is run:
- ***api_engine***: This module contains the files that are required to set up the webhook, send replies to telegram and parse received updates from telegram.
- ***app_engine***: This module is the working brain of the app, the business logic of the app is defined here.
- ***db_engine***: This module contains the files necessary for interfacing with PostgreSQL databases and Redis.
- ***replies_engine***: This module contains the necessary templates for generating replies to send back to the telegram users.

#### If you have any questions about this project, message me on aymanimtyaz@gmail.com :)