# Simple Notification Sender for Discord
# Author: SeungMin Lee,
# 		  Software Developer at ReturnZero Inc.,
#		  Undergraduate Student at DGIST.
# Reference: Hugging Face's knockknock
# 			 https://github.com/huggingface/knockknock

from datetime import datetime
import functools
import json
import os
import requests
import traceback

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class WebhookUrlEnteredError(Exception):
    def __init__(self):
        super().__init__("No webhook url entered; Please make sure that you entered `webhook_url` or the environment variable `DISCORD_WEBHOOK_URL` correctly.")


def deco_noti(webhook_url="", custom_content="", notify_end_too=False):
    def get_content_for_start(fname, start):
        return "🏃 **Your function <{fname}> has started.**\n \
		\t- function name: {fname}\n \
		\t- start time: {str_start}".format(fname=fname,
                                      str_start=start.strftime(DATE_FORMAT))

    def get_content_for_end(fname, start, end, run):
        return "🎉 **Your function <{fname}> is complete!**\n \
		\t- function name: {fname}\n \
		\t- start time: {str_start}\n \
		\t- end time: {str_end}\n \
		\t- run time: {run}".format(fname=fname, str_start=start.strftime(DATE_FORMAT),
                              str_end=end.strftime(DATE_FORMAT), run=run)

    def get_content_for_dead(fname, start, end, run, exp):
        return "😭 **Your function <{fname}> ended unexpectedly due to an exception or error.**\n \
		\t- function name: {fname}\n \
		\t- start time: {str_start}\n \
		\t- dead time: {str_end}\n \
		\t- run time: {run}\n \
		\t- Error Info: {exp}\n\n \
		\t- Traceback:\n \
		\t{trace}".format(fname=fname, str_start=start.strftime(DATE_FORMAT),
                    str_end=end.strftime(DATE_FORMAT), run=run,
                    exp=exp, trace=traceback.format_exc())

    def decorator(func):
        url = webhook_url or os.environ.get('DISCORD_WEBHOOK_URL')

        if not url:
            raise WebhookUrlEnteredError()

        def send(contents, error=False):
            content = contents if error else custom_content or contents
            _ = requests.post(url=url, data=json.dumps(
                {'content': content}), headers={'Content-Type': 'application/json'})

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = datetime.now()
            fname = func.__name__

            send(get_content_for_start(fname, start))

            try:
                res = func(*args, **kwargs)
                end = datetime.now()
                if notify_end_too and not custom_content:
                    send(get_content_for_end(fname, start, end, end - start))
                return res
            except Exception as exp:
                end = datetime.now()
                send(get_content_for_dead(
                    fname, start, end, end - start, exp), error=True)
                raise exp

        return wrapper
    return decorator


def send_noti(webhook_url="", custom_content=""):
    url = webhook_url or os.environ.get('DISCORD_WEBHOOK_URL')
    if not url:
        raise WebhookUrlEnteredError()

    default = "The notification has arrived from your program."

    _ = requests.post(url=url, data=json.dumps(
        {'content': custom_content or default}), headers={'Content-Type': 'application/json'})
