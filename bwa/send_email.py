# Notification Sender for Email
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
import yagmail

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def notify_func(receiver_emails, sender_email, sender_password):
    sender = yagmail.SMTP(user=sender_email, password=sender_password)

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
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = datetime.now()
            fname = func.__name__

            for receiver in receiver_emails:
                    content = content_for_start(fname, start)
                    sender.send(receiver, content.split("\n")[0], content)
            try:
                _ = func(*args, **kwargs)
                end = datetime.now()
                duration = end - start

                for i in range(len(recipient_emails)):
                    current_recipient = recipient_emails[i]
                    yag_sender.send(current_recipient, 'Training has sucessfully finished 🎉', contents)
            except Exception as ex:

        return wrapper
    return decorator


def send_notification(receiver_emails, sender_email):
    _ = requests.post(url=webhook_url, data=json.dumps(
        {'content': content}), headers={'Content-Type': 'application/json'})
