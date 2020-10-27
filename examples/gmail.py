# Please install the package through the command below.
# pip install bwa
from bwa.gmail import deco_noti, send_noti
import os
import time

receiver_emails = ["<RECEIVER_EMAIL_ADDRESS>"]
sender_email = "<SENDER_EMAIL_ADDRESS>"
sender_password = "<SENDER_EMAIL_PASSWORD>"

# You can be notified when your function starts.
@deco_noti(receiver_emails=receiver_emails,
           sender_email=sender_email,
           sender_password=sender_password)
def decorator():
    print("Gamil Example: decorator")

# You can be notified when your function starts, 
# when it ends or dies.
@deco_noti(receiver_emails=receiver_emails,
           sender_email=sender_email,
           sender_password=sender_password,
           notify_end_too=True)
def decorator_end_too():
    print("Gamil Example: decorator_end_too")
    # raise Exception

# When your function starts, you can receive a notification
# consisting of your customized content.
@deco_noti(receiver_emails=receiver_emails,
           sender_email=sender_email,
           sender_password=sender_password,
           custom_content="Hello, Gmail")
def decorator_with_custom_content():
    print("Gamil Example: decorator_with_custom_content")

# [CAUTION] In order to receive notification from this decoder, 
# environment variables must be set.
# You can be notified when your function starts.
@deco_noti()
def simple_decorator():
    print("Gamil Example: simple_decorator")

# [CAUTION] In order to receive notification from this decoder, 
# environment variables must be set.
# consisting of your customized content.
@deco_noti(custom_content="Hello, Gmail")
def simple_decorator_with_custom_content():
    print("Gamil Example: simple_decorator_with_custom_content")


if __name__ == "__main__":
    decorator()
    decorator_end_too()
    decorator_with_custom_content()

    # $ export SENDER_EMAIL="<Sender's email>"
    # $ export SENDER_PASSWORD="<Sender's password>"

    simple_decorator()
    simple_decorator_with_custom_content()
