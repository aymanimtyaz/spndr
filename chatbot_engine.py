
from stateengine import IntegratedStateEngine
from api_engine import telegrambot_caller as ac
from db_interface import dbc
from extensions import red
from utils import generate_show_reply

chatbot = IntegratedStateEngine()

@chatbot.state_handler("default", default=True)
def default(input):
    message, chat_id, sender_id = input[0].lower(), input[1], input[2]
    user = red.hgetall(f"on_tra{sender_id}")
    if not user:
        sql = (
            """
            SELECT EXISTS(
                SELECT * FROM chatbot_users 
                WHERE client='telegram' 
                AND client_id=(%(sender_id)s)
                LIMIT 1
            );
            """)
        with dbc as curs:
            curs.execute(sql, {"sender_id":str(sender_id)})
            is_chatbot_user = curs.fetchone()[0]
        if not is_chatbot_user:
            reply_text = (
                """
                Hi! Please authenticate yourself with 
                telegram on spndr.co to use spndr's 
                telegram client.
                """)
            ac.sendMsg(chat_id, reply_text)
            return None
    if message in ["/help", "/new", "/show", '/delete']:
        if message == "/help":
            reply_text = (
                """
                LIST OF AVAILABLE COMMANDS:

                /new - Starts a new transaction.
                /show - See your last 10 purchases.
                /delete - Delete your account.
                /help - Brings up this dialogue.      
                """)
            ac.sendMsg(chat_id, reply_text)
            return None
        elif message == "/new":
            reply_text = (
                """
                Enter the name of the product
                or service that you bought.
                /abort
                """)
            ac.sendMsg(chat_id, reply_text)
            return "get_item"
        elif message == "/show":
            reply_text = generate_show_reply(sender_id)
            ac.sendMsg(chat_id, reply_text)
            return None
        elif message == "/delete":
            reply_text = (
                """
                Are you sure you want to unlink
                this telegram account from your 
                spndr account (y/n)?
                """)
            ac.sendMsg(chat_id, reply_text)
            return "get_account_deletion_confirmation"
        else:
            reply_text = (
                """
                Type /help to get a list of commands.
                """)
            ac.sendMsg(chat_id, reply_text)
            return None

@chatbot.state_handler("get_account_deletion_confirmation")
def get_account_deletion_confirmation(input):
    message, chat_id, sender_id = input[0].lower(), input[1], input[2]
    if message in ["y", "n"]:
        if message == "y":
            sql = (
                """
                DELETE FROM chatbot_users
                WHERE client = 'telegram' AND 
                client_id = (%(sender_id)s);
                """)
            values = {
                "sender_id":str(sender_id),
            }
            with dbc as curs:
                curs.execute(sql, values)
            reply_text = (
                """
                This telegram account was successfully 
                unlinked from your spndr account.

                Have a great day!
                """)
            ac.sendMsg(chat_id, reply_text)
            return None
        reply_text = (
            """
            Your telegram account was not
            unliked from your spndr account.
                    /new /show
            """)
        ac.sendMsg(chat_id, reply_text)
        return None
    else:
        reply_text = (
            """
            Would you like to unlink this
            telegram account from your 
            spndr account (y/n) ?

            Send y for yes.
            Send n for no.
            """)
        ac.sendMsg(chat_id, reply_text)
        return "get_account_deletion_confirmation"



@chatbot.state_handler("get_item")
def get_item(input):
    message, chat_id, sender_id = input[0], input[1], input[2]
    if message.lower()[0] == "/":
        if message.lower() == "/abort":
            reply_text = (
                """
                Are you sure you want to abort
                this transaction? (y/n)
                """)
            ac.sendMsg(chat_id, reply_text)
            return "get_item_abort"
        elif message.lower() == "/help":
            reply_text = (
                """
                LIST OF AVAILABLE COMMANDS:

                /abort - aborts the current transaction.
                /help - brings up this dialogue.
                """)
            ac.sendMsg(chat_id, reply_text)
            return "get_item"
        else:
            reply_text = (
                """
                Type /help to get a list of 
                available commands.

                Enter the name of the product
                or service that you bought.
                /abort
                """)
            ac.sendMsg(chat_id, reply_text)
            return "get_item"
    else:
        item = message
        red.hset(name=f"on_tra{sender_id}", mapping={"item":item})
        reply_text = (
            """
            How much did you spend?
            """)
        ac.sendMsg(chat_id, reply_text)
        return "get_price"

@chatbot.state_handler("get_price")
def get_price(input):
    message, chat_id, sender_id = input[0], input[1], input[2]
    if message.lower()[0] == "/":
        if message.lower() == "/abort":
            reply_text = (
                """
                Are you sure you want to abort
                this transaction? (y/n)
                """)
            ac.sendMsg(chat_id, reply_text)
            return "get_price_abort"
        elif message.lower() == "/help":
            reply_text = (
                """
                LIST OF AVAILABLE COMMANDS:

                /abort - aborts the current transaction.
                /help - brings up this dialogue.
                """)
            ac.sendMsg(chat_id, reply_text)
            return "get_price"
        else:
            reply_text = (
                """
                Type /help to get a list of 
                available commands.

                How much did you spend?
                /abort
                """)
            ac.sendMsg(chat_id, reply_text)
            return "get_price"
    try:
        float(message)
    except ValueError:
        reply_text = (
            """
            Please enter a numeric value 
            for the price.
            """)
        ac.sendMsg(chat_id, reply_text)
        return "get_price"
    if float(message) <= 0:
        reply_text = (
            """
            Please enter a value that is 
            greater than zero for the
            price.
            """)
        ac.sendMsg(chat_id, reply_text)
        return "get_price"
    price = float(message)
    red.hset(f"on_tra{sender_id}", mapping={"price":price})
    reply_text = (
        """
        Where did you buy this product 
        from?
        """)
    ac.sendMsg(chat_id, reply_text)
    return "get_vendor"

@chatbot.state_handler("get_vendor")
def get_vendor(input):
    message, chat_id, sender_id = input[0], input[1], input[2]
    if message.lower()[0] == "/":
        if message.lower() == "/abort":
            reply_text = (
                """
                Are you sure you want to abort
                this transaction? (y/n)
                """)
            ac.sendMsg(chat_id, reply_text)
            return "get_vendor_abort"
        elif message.lower() == "/help":
            reply_text = (
                """
                LIST OF AVAILABLE COMMANDS:

                /abort - aborts the current transaction.
                /help - brings up this dialogue.
                """)
            ac.sendMsg(chat_id, reply_text)
            return "get_vendor"
        else:
            reply_text = (
                """
                Type /help to get a list of 
                available commands.

                Where did you buy this product
                from?
                /abort
                """)
            ac.sendMsg(chat_id, reply_text)
            return "get_vendor"
    vendor = message
    red.hset(f"on_tra{sender_id}", mapping={"vendor":vendor})
    reply_text = (
        """
        What category would you put
        this purchase in?
        """)
    ac.sendMsg(chat_id, reply_text)
    return "get_category"

@chatbot.state_handler("get_category")
def get_category(input):
    message, chat_id, sender_id = input[0], input[1], input[2]
    if message.lower()[0] == "/":
        if message.lower() == "/abort":
            reply_text = (
                """
                Are you sure you want to abort
                this transaction? (y/n)
                """)
            ac.sendMsg(chat_id, reply_text)
            return "get_category_abort"
        elif message.lower() == "/help":
            reply_text = (
                """
                LIST OF AVAILABLE COMMANDS:

                /abort - aborts the current transaction.
                /help - brings up this dialogue.
                """)
            ac.sendMsg(chat_id, reply_text)
            return "get_category"
        else:
            reply_text = (
                """
                Type /help to get a list of 
                available commands.

                What category would you put
                this purchase in?
                /abort
                """)
            ac.sendMsg(chat_id, reply_text)
            return "get_category"
    category = message
    transaction_info = red.hgetall(f"on_tra{sender_id}")
    red.delete(f"on_tra{sender_id}")
    transaction_info["category"] = category
    # add transaction info to transactions
    sql = (
        """
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
        """)
    values = {
        "sender_id":str(sender_id),
        "item":transaction_info["item"],
        "price":transaction_info["price"],
        "vendor":transaction_info["vendor"],
        "category":transaction_info["category"]
    }
    with dbc as curs:
        curs.execute(sql, values)
    reply_text = (
        """
        The transaction was successfully
        recorded!
                /show /new /help
        """)
    ac.sendMsg(chat_id, reply_text)
    return None



@chatbot.state_handler("get_item_abort")
def get_item_abort(input):
    message, chat_id, sender_id = input[0].lower(), input[1], input[2]
    if message in ["y", "n"]:
        if message == "y":
            red.delete(f"on_tra{sender_id}")
            reply_text = (
                """
                The transaction was successfully
                aborted. /new /show /help
                """)
            ac.sendMsg(chat_id, reply_text)
            return None
        reply_text = (
            """
            The transaction was not aborted.

            Enter the name of the product
            or service that you bought.
            /abort
            """)
        ac.sendMsg(chat_id, reply_text)
        return "get_item"
    else:
        reply_text = (
            """
            Please confirm if you would like 
            to abort the ongoing transaction.

            Reply y for yes.
            Reply n for no.
            """)
        ac.sendMsg(chat_id, reply_text)
        return "get_item_abort"

@chatbot.state_handler("get_price_abort")
def get_price_abort(input):
    message, chat_id, sender_id = input[0].lower(), input[1], input[2]
    if message in ["y", "n"]:
        if message == "y":
            red.delete(f"on_tra{sender_id}")
            reply_text = (
                """
                The transaction was successfully
                aborted. /new /show /help
                """)
            ac.sendMsg(chat_id, reply_text)
            return None
        reply_text = (
            """
            The transaction was not aborted.

            How much did you spend?
            /abort
            """)
        ac.sendMsg(chat_id, reply_text)
        return "get_price"
    else:
        reply_text = (
            """
            Please confirm if you would like 
            to abort the ongoing transaction.

            Reply y for yes.
            Reply n for no.
            """)
        ac.sendMsg(chat_id, reply_text)
        return "get_price_abort"

@chatbot.state_handler("get_vendor_abort")
def get_vendor_abort(input):
    message, chat_id, sender_id = input[0].lower(), input[1], input[2]
    if message in ["y", "n"]:
        if message == "y":
            red.delete(f"on_tra{sender_id}")
            reply_text = (
                """
                The transaction was successfully
                aborted. /new /show /help
                """)
            ac.sendMsg(chat_id, reply_text)
            return None
        reply_text = (
            """
            The transaction was not aborted.

            Where did you buy this product 
            from?
            /abort
            """)
        ac.sendMsg(chat_id, reply_text)
        return "get_vendor"
    else:
        reply_text = (
            """
            Please confirm if you would like 
            to abort the ongoing transaction.

            Reply y for yes.
            Reply n for no.
            """)
        ac.sendMsg(chat_id, reply_text)
        return "get_vendor_abort"

@chatbot.state_handler("get_category_abort")
def get_category_abort(input):
    message, chat_id, sender_id = input[0].lower(), input[1], input[2]
    if message in ["y", "n"]:
        if message == "y":
            red.delete(f"on_tra{sender_id}")
            reply_text = (
                """
                The transaction was successfully
                aborted. /new /show /help
                """)
            ac.sendMsg(chat_id, reply_text)
            return None
        reply_text = (
            """
            The transaction was not aborted.

            What category would you put
            this purchase in?
            /abort
            """)
        ac.sendMsg(chat_id, reply_text)
        return "get_category"
    else:
        reply_text = (
            """
            Please confirm if you would like 
            to abort the ongoing transaction.

            Reply y for yes.
            Reply n for no.
            """)
        ac.sendMsg(chat_id, reply_text)
        return "get_category_abort"