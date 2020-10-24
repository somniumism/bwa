# This test may be executed as follows:
# $ python -m unittest discover -v bwa.test.test_email

from time import sleep
import unittest

from bwa.gmail import deco_noti, send_noti

receiver_emails = ["<GMAIL_ADDRESS>"]
sender_email = "<TESTER's EMAIL>"
sender_password = "<TESTER's PASSWORD>"


class GmailTest(unittest.TestCase):
    def test_gmail(self):
        @deco_noti(receiver_emails=receiver_emails, sender_email=sender_email, sender_password=sender_password)
        def decorator():
            sleep(3)
        decorator()

    def test_decorator_with_end(self):
        @deco_noti(receiver_emails=receiver_emails, sender_email=sender_email, sender_password=sender_password, notify_end_too=True)
        def decorator_with_end():
            sleep(3)
        decorator_with_end()

    def test_decorator_with_exception(self):
        @deco_noti(receiver_emails=receiver_emails, sender_email=sender_email, sender_password=sender_password, notify_end_too=True)
        def decorator_with_exception():
            sleep(3)
            raise Exception
        decorator_with_exception()

    def test_decorator_with_custom_content(self):
        @deco_noti(receiver_emails=receiver_emails, sender_email=sender_email, sender_password=sender_password, custom_content="Hello, Gmail")
        def decorator_with_custom_content():
            sleep(3)
        decorator_with_custom_content()

    def test_decorator_with_custom_content_true(self):
        @deco_noti(receiver_emails=receiver_emails, sender_email=sender_email, sender_password=sender_password, custom_content="Hello, Gmail", notify_end_too=True)
        def decorator_with_custom_content_true():
            sleep(3)
        decorator_with_custom_content_true()

    def test_function(self):
        send_noti(receiver_emails=receiver_emails, sender_email=sender_email,
                  sender_password=sender_password, custom_content="Hello, Gmail")

    def test_decorator_with_no_receiver_emails(self):
        @deco_noti(sender_email=sender_email, sender_password=sender_password)
        def decorator_with_no_receiver_emails():
            sleep(3)
        decorator_with_no_receiver_emails()

    def test_function_with_no_receiver_emails(self):
        send_noti(sender_email=sender_email,
                  sender_password=sender_password, custom_content="Hello, Gmail")

    # Enter enviroment variable
    # os.environ['SENDER_EMAIL'] = sender_email
    # os.environ['SENDER_PASSWORD'] = sender_password
    # or `$ export SENDER_EMAIL="<SENDER_EMAIL>"`
    #    `$ export SENDER_PASSWORD="<SENDER_PASSWORD>"`
    def test_decorator_with_envar(self):
        @deco_noti(receiver_emails=receiver_emails)
        def decorator_with_envar(receiver_emails=receiver_emails):
            sleep(3)
        decorator_with_envar()

    def test_simple_decorator(self):
        @deco_noti()
        def simple_decorator():
            sleep(3)
        simple_decorator()

    def test_simple_decorator_with_custom_content(self):
        @deco_noti(receiver_emails=receiver_emails, custom_content="Hello, Gmail")
        def simple_decorator_with_custom_content():
            sleep(3)
        simple_decorator_with_custom_content()

    def test_function_with_envar(self):
        send_noti()

    def test_simple_function_with_custom_content(self):
        send_noti(custom_content="Hello, Gmail")


if __name__ == "__main__":
    unittest.main()
