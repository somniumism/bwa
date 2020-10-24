# This test may be executed as follows:
# $ python -m unittest discover -v bwa.test

from time import sleep
import unittest

from bwa.telegm import deco_noti, send_noti

token = "<BOT_TOKEN>"
chat_id = "<CHAT_ID>"

class TelegramTest(unittest.TestCase):
    def test_decorator(self):
        @deco_noti(token=token, chat_id=chat_id)
        def decorator():
            sleep(3)
        decorator()

    def test_decorator_with_end(self):
        @deco_noti(token=token, chat_id=chat_id, notify_end_too=True)
        def decorator_with_end():
            sleep(3)
        decorator_with_end()

    def test_decorator_with_exception(self):
        @deco_noti(token=token, chat_id=chat_id, notify_end_too=True)
        def decorator_with_exception():
            sleep(3)
            raise Exception
        decorator_with_exception()

    def test_decorator_with_custom_content(self):
        @deco_noti(token=token, chat_id=chat_id, custom_content="Hello, Discord")
        def decorator_with_custom_content():
            sleep(3)
        decorator_with_custom_content()

    def test_decorator_with_custom_content_true(self):
        @deco_noti(token=token, chat_id=chat_id, custom_content="Hello, Discord", notify_end_too=True)
        def decorator_with_custom_content_true():
            sleep(3)
        decorator_with_custom_content_true()

    def test_function(self):
        send_noti(token=token, chat_id=chat_id, custom_content="Hello, Discord")

    # Enter enviroment variable
    # os.environ['TELEGRAM_TOKEN'] = token
    # os.environ['TELEGRAM_CHAT_ID'] = chat_id
    # or `$ export TELEGRAM_TOKEN="<TELEGRAM_TOKEN>"`
    #    `$ export TELEGRAM_CHAT_ID="<TELEGRAM_CHAT_ID>"`
    def test_decorator_with_envar(self):
        @deco_noti()
        def decorator_with_envar():
            sleep(3)
        decorator_with_envar()

    def test_simple_decorator_with_custom_content(self):
        @deco_noti(custom_content="Hello, Discord")
        def simple_decorator_with_custom_content():
            sleep(3)
        simple_decorator_with_custom_content()

    def test_function_with_envar(self):
        send_noti()

    def test_simple_function_with_custom_content(self):
        send_noti(custom_content="Hello, Discord")


if __name__ == "__main__":
    unittest.main()
