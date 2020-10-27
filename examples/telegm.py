# Please install the package through the command below.
# pip install bwa
from bwa.telegm import deco_noti, send_noti
import os
import time

token = "<BOTS_TOKEN>"
chat_id = "<BOTS_CHAT_ID>"

# You can be notified when your function starts.
@deco_noti(token=token,
           chat_id=chat_id)
def decorator():
    print("Telegram Example: decorator")

# You can be notified when your function starts, 
# when it ends or dies.
@deco_noti(token=token,
           chat_id=chat_id,
           notify_end_too=True)
def decorator_end_too():
    print("Telegram Example: decorator_end_too")
    # raise Exception

# When your function starts, you can receive a notification
# consisting of your customized content.
@deco_noti(token=token,
           chat_id=chat_id,
           custom_content="Hello, Telegram")
def decorator_with_custom_content():
    print("Telegram Example: decorator_with_custom_content")

# [CAUTION] In order to receive notification from this decoder, 
# environment variables must be set.
# You can be notified when your function starts.
@deco_noti()
def simple_decorator():
    print("Telegram Example: simple_decorator")

# [CAUTION] In order to receive notification from this decoder, 
# environment variables must be set.
# consisting of your customized content.
@deco_noti(custom_content="Hello, Telegram")
def simple_decorator_with_custom_content():
    print("Telegram Example: simple_decorator_with_custom_content")


if __name__ == "__main__":
    decorator()
    decorator_end_too()
    decorator_with_custom_content()

    # $ export TELEGRAM_TOKEN="<Telegram Bot's token>"
    # $ export TELEGRAM_CHAT_ID="<Telegram Bot's chat id>"

    simple_decorator()
    simple_decorator_with_custom_content()
