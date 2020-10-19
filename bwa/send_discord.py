# Notification Sender for Discord
# Author: SeungMin Lee,
# 		  Software Developer at ReturnZero Inc.,
#		  Undergraduate Student at DGIST.
# Reference: Hugging Face's knockknock
# 			 https://github.com/huggingface/knockknock

from datetime import datetime
import functools
import json
import requests
import traceback

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def notify_func(webhook_url, notify_end_too=False):
    def content_for_start(fname, start):
        return "🏃 **Your function <{fname}> has started.**\n \
		\t- function name: {fname}\n \
		\t- start time: {str_start}".format(fname=fname,
                                      str_start=start.strftime(DATE_FORMAT))

    def content_for_end(fname, start, end, run):
        return "🎉 **Your function <{fname}> is complete!**\n \
		\t- function name: {fname}\n \
		\t- start time: {str_start}\n \
		\t- end time: {str_end}\n \
		\t- run time: {run}".format(fname=fname, str_start=start.strftime(DATE_FORMAT),
                              str_end=end.strftime(DATE_FORMAT), run=run)

    def content_for_dead(fname, start, end, run, exp):
        return "😭 **Your function <{fname}> died in action...**\n \
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
        def send(content):
            _ = requests.post(url=webhook_url, data=json.dumps(
                {'content': content}), headers={'Content-Type': 'application/json'})

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = datetime.now()
            fname = func.__name__

            send(content_for_start(fname, start))

            if notify_end_too:
                try:
                    _ = func(*args, **kwargs)
                    end = datetime.now()

                    send(content_for_end(fname, start, end, end - start))
                except Exception as exp:
                    end = datetime.now()
                    send(content_for_dead(
                        fname, start, end, end - start, exp))

        return wrapper
    return decorator


def send_notification(webhook_url, content):
    _ = requests.post(url=webhook_url, data=json.dumps(
        {'content': content}), headers={'Content-Type': 'application/json'})
