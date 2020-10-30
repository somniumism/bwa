# Notification Sender for Gmail
# Author: SeungMin Lee,
# 		  Software Developer at ReturnZero Inc.,
#		  Undergraduate Student at DGIST.
# Reference: Hugging Face's knockknock
# 			 https://github.com/huggingface/knockknock

from datetime import datetime
import functools
import json
import os
import traceback
import yagmail
from smtplib import SMTPAuthenticationError

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class UserInfoEnteredError(Exception):
    def __init__(self):
        super().__init__("Your email info is invalid; Please make sure that you entered `sender_email` and 'sender_password' or the environment variable `SENDER_EMAIL` and `SENDER_PASSWORD` correctly.")


class AuthenticationError(Exception):
    def __init__(self):
        super().__init__("Your account authentication failed; Please check your email address and password correctly.")


def deco_noti(receiver_emails=[], sender_email="", sender_password="", custom_content="", notify_end_too=False):
    user = sender_email or os.environ.get('SENDER_EMAIL')
    password = sender_password or os.environ.get('SENDER_PASSWORD')
    if not user or not password:
        raise UserInfoEnteredError()
    sender = yagmail.SMTP(user=user, password=password)
    receivers = receiver_emails or [user]

    def get_content_for_start(fname, start):
        return "🏃 Your function <{fname}> has started.\n \
		\t- function name: {fname}\n \
		\t- start time: {str_start}".format(fname=fname,
                                      str_start=start.strftime(DATE_FORMAT))

    def get_content_for_end(fname, start, end, run):
        return "🎉 Your function <{fname}> is complete!\n \
		\t- function name: {fname}\n \
		\t- start time: {str_start}\n \
		\t- end time: {str_end}\n \
		\t- run time: {run}".format(fname=fname, str_start=start.strftime(DATE_FORMAT),
                              str_end=end.strftime(DATE_FORMAT), run=run)

    def get_content_for_dead(fname, start, end, run, exp):
        return "😭 Your function <{fname}> ended unexpectedly due to an exception or error.\n \
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
        def send(contents, receiver, error=False):
            try:
                content = contents if error else custom_content or contents
                title = content.split("\n")[0][:50] if len(
                    content.split("\n")[0]) > 50 else content.split("\n")[0]
                sender.send(receiver, title, content)
            except SMTPAuthenticationError:
                raise AuthenticationError()

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = datetime.now()
            fname = func.__name__

            for receiver in receivers:
                send(get_content_for_start(fname, start), receiver)

            try:
                res = func(*args, **kwargs)
                end = datetime.now()

                if notify_end_too and not custom_content:
                    for receiver in receivers:
                        send(get_content_for_end(
                            fname, start, end, end - start), receiver)
                return res
            except Exception as exp:
                end = datetime.now()
                for receiver in receivers:
                    send(get_content_for_dead(fname, start,
                                              end, end - start, exp), receiver, error=True)
                raise exp

        return wrapper
    return decorator


def send_noti(receiver_emails=[], sender_email="", sender_password="", custom_content=""):
    user = sender_email or os.environ.get('SENDER_EMAIL')
    password = sender_password or os.environ.get('SENDER_PASSWORD')
    if not user or not password:
        raise UserInfoEnteredError()
    sender = yagmail.SMTP(user=user, password=password)
    receivers = receiver_emails or [user]

    content = custom_content or "The notification has arrived from your program."
    title = content.split("\n")[0][:50] if len(
        content.split("\n")[0]) > 50 else content.split("\n")[0]
    try:
        for receiver in receivers:
            sender.send(receiver, title, content)
    except SMTPAuthenticationError:
        raise AuthenticationError()
