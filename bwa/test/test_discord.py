# This test may be executed as follows:
# $ python -m unittest discover -v bwa.test

from time import sleep
import unittest

from bwa.discord import deco_noti, send_noti

webhook_url = "<YOUR_WEBHOOK_URL>"


class DiscordTest(unittest.TestCase):
    def test_decorator(self):
        @deco_noti(webhook_url=webhook_url)
        def decorator():
            sleep(3)
        decorator()

    def test_decorator_with_end(self):
        @deco_noti(webhook_url=webhook_url, notify_end_too=True)
        def decorator_with_end():
            sleep(3)
        decorator_with_end()

    def test_decorator_with_exception(self):
        @deco_noti(webhook_url=webhook_url, notify_end_too=True)
        def decorator_with_exception():
            sleep(3)
            raise Exception
        decorator_with_exception()

    def test_decorator_with_custom_content(self):
        @deco_noti(webhook_url=webhook_url, custom_content="Hello, Discord")
        def decorator_with_custom_content():
            sleep(3)
        decorator_with_custom_content()

    def test_decorator_with_custom_content_true(self):
        @deco_noti(webhook_url=webhook_url, custom_content="Hello, Discord", notify_end_too=True)
        def decorator_with_custom_content_true():
            sleep(3)
        decorator_with_custom_content_true()

    def test_function(self):
        send_noti(webhook_url=webhook_url, custom_content="Hello, Discord")

    # Enter enviroment variable
    # os.environ['DISCORD_WEBHOOK_URL'] = webhook_url
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
