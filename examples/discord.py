# Please install the package through the command below.
# pip install bwa
from bwa.discord import deco_noti, send_noti
import os
import time

webhook_url = "<DISCORD_WEBHOOK_URL>"

# You can be notified when your function starts.
@deco_noti(webhook_url=webhook_url)
def decorator():
    print("Discord Example: decorator")

# You can be notified when your function starts, 
# when it ends or dies.
@deco_noti(webhook_url=webhook_url,
           notify_end_too=True)
def decorator_end_too():
    print("Discord Example: decorator_end_too")
    # raise Exception

# When your function starts, you can receive a notification
# consisting of your customized content.
@deco_noti(webhook_url=webhook_url,
           custom_content="Hello, Discord")
def decorator_with_custom_content():
    print("Discord Example: decorator_with_custom_content")

# [CAUTION] In order to receive notification from this decoder, 
# environment variables must be set.
# You can be notified when your function starts.
@deco_noti()
def simple_decorator():
    print("Discord Example: simple_decorator")

# [CAUTION] In order to receive notification from this decoder, 
# environment variables must be set.
# consisting of your customized content.
@deco_noti(custom_content="Hello, Discord")
def simple_decorator_with_custom_content():
    print("Discord Example: simple_decorator_with_custom_content")


if __name__ == "__main__":
    decorator()
    decorator_end_too()
    decorator_with_custom_content()

    # $ export DISCORD_WEBHOOK_URL="<Your webhook url>"

    simple_decorator()
    simple_decorator_with_custom_content()
