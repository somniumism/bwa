# Simple Notification Sender for Telegram
# Author: SeungMin Lee,
# 		  Software Developer at ReturnZero Inc.,
#		  Undergraduate Student at DGIST.
# Reference: Hugging Face's knockknock
# 			 https://github.com/huggingface/knockknock

from datetime import datetime
import functools
import os
import telegram
import traceback

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class TelegramBotEnteredError(Exception):
    def __init__(self):
        super().__init__("Your email info is invalid; Please make sure that you entered `token` and 'chat_id' or the environment variable `TELEGRAM_TOKEN` and `TELEGRAM_CHAT_ID` correctly.")


def deco_noti(token="", chat_id="", custom_content="", notify_end_too=False):
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
        t_token = token or os.environ.get('TELEGRAM_TOKEN')
        t_chat_id = chat_id or os.environ.get('TELEGRAM_CHAT_ID')

        if not t_token or not t_chat_id:
            raise TelegramBotEnteredError()

        bot = telegram.Bot(token=t_token)

        def send(contents, error=False):
            text = contents if error else custom_content or contents
            bot.send_message(chat_id=int(t_chat_id), text=text)

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


def send_noti(token="", chat_id="", custom_content=""):
    t_token = token or os.environ.get('TELEGRAM_TOKEN')
    t_chat_id = chat_id or os.environ.get('TELEGRAM_CHAT_ID')
    if not t_token or not t_chat_id:
        raise TelegramBotEnteredError()

    bot = telegram.Bot(token=t_token)
    default = "The notification has arrived from your program."

    bot.send_message(chat_id=int(t_chat_id), text=custom_content or default)
