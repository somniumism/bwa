from time import sleep
import unittest

from bwa.send_discord import notify_func, send_notification

webhook_url = "<WEBHOOK_URL>"

class Test(unittest.TestCase):    
    def test_decorator(self):
        @notify_func(webhook_url=webhook_url)
        def test_decorator():
            sleep(3)
        test_decorator()
    
    def test_decorator_with_end(self):
        @notify_func(webhook_url=webhook_url, notify_end_too=True)
        def test_decorator_with_end():
            sleep(3)
        test_decorator_with_end()

    def test_decorator_with_exception(self):
        @notify_func(webhook_url=webhook_url, notify_end_too=True)
        def test_decorator_with_exception():
            sleep(3)
            raise Exception
        test_decorator_with_exception()

    def test_function(self):
        send_notification(webhook_url=webhook_url, content="Hello, Discord")

if __name__ == "__main__":
    unittest.main()