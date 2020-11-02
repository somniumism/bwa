# Bwa: Simple Notification Sender

[![PyPI Latest Release](https://img.shields.io/pypi/v/bwa.svg)](https://pypi.org/project/bwa/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-red.svg)]()
[![License](https://img.shields.io/badge/Licence-MIT-blue.svg)](https://github.com/somniumism/bwa/blob/main/LICENSE)
[![Downloads](https://pepy.tech/badge/bwa)](https://pepy.tech/project/bwa)

Document: [English](https://github.com/somniumism/bwa) | [한국어](https://github.com/somniumism/bwa/blob/main/docs/README.kr.md)

Notion page: [English](https://www.notion.so/somniumis/Bwa-Simple-Notification-Sender-a9919a46f2d64d11baab60deb4e8de55) | [한국어](https://www.notion.so/somniumis/Bwa-Simple-Notification-Sender-0146f53d2f3f4807b029bdf6f7bfd7a9)

More specific details can be accessed from the Notion page below: [Bwa: Simple Notification Sender](https://www.notion.so/somniumis/Bwa-Simple-Notification-Sender-a9919a46f2d64d11baab60deb4e8de55)

<p align="center">
    <img src="../docs/example.gif" width="450" height="300"/>  
</p>

**bwa** is a tool, simple notifcation sender, that can send notifications related to the execution of functions by using a decorator. If you set up a decorator `@deco_noti()` above the function you made and a few client settings , you can receive a notification from the client when the function starts, completes, or ends due to an unexpected error. Currently, **bwa** supports these features for four clients; `Discord`, `Slack`, `Telegram` and `Gamil`. You will thus get messages from these clients.

If you set your webhook url as an environment variable, you will be notified quite simply as follows:

```python
from bwa.discord import deco_noti

@deco_noti()
def run():
    print("Hi, bwa!")
```
To be notified, you need to set up certain client settings or prepare information from the client, such as the web-hook url. Please refer to the following Notion page for detailed setup methods of each client.

- Detailed setup methods and usage: [Bwa: Simple Notification Sender](https://www.notion.so/somniumis/Bwa-Simple-Notification-Sender-a9919a46f2d64d11baab60deb4e8de55)

- Platforms supported:  
    - [Discord](https://www.notion.so/somniumis/Discord-231544b268b64a42b3d084d1aa3c3d96) : `bwa.discord`
    - [Slack](https://www.notion.so/somniumis/Slack-5633bf0e13ab4e499e2b2c677852dbbf) : `bwa.slack`
    - [Telegram](https://www.notion.so/somniumis/Telegram-888407c4770a4b5a806a9c7c65e45250) : `bwa.telegm`
    - [Gmail](https://www.notion.so/somniumis/Gmail-197fc3dcf2f74c9dba651afb19267747) : `bwa.gmail`

Note that the `telegram` module is `bwa.telegm`, not `bwa.telegram`

## Installation

By using `pip` , you can install **bwa**. Simply install it using the command below.

```bash
pip install bwa==1.1.1
```

## Usage

**bwa** provides the decorator `@deco_noti()` and the method `send_noti()`. `@deco_noti()` lets you receive notifications about the start, complete, unexpected shutdown of your function. In addition, if you add `send_noti()` anywhere in your code, you will be notified when that code is executed.

As I explained earlier, **bwa** has the feature that send and receive notifications through Discord(`bwa.discord`), Slack(`bwa.slack`), Telegram(`bwa.telegm`) and Gmail(`bwa.gmail`). Depending on the kind of client, the required parameters differ. The difference is as follows:

- [bwa.discord](https://www.notion.so/somniumis/Discord-231544b268b64a42b3d084d1aa3c3d96#f3fe6caaaaf8441a829e1bfbd577ba0c)  
    `webhook_url` or environment variable `DISCORD_WEBHOOK_URL` : webhook url of your Discord server 
    
- [bwa.slack](https://www.notion.so/somniumis/Slack-5633bf0e13ab4e499e2b2c677852dbbf#6d2f20e33fc74b728813b0ddcb63ba69)  
    `webhook_url` or environment variable `SLACK_WEBHOOK_URL`: webhook url of your Slack server 

- [bwa.telegm](https://www.notion.so/somniumis/Telegram-888407c4770a4b5a806a9c7c65e45250#2b2295b99afb4489b24a6775dc23e0e4)  
    `token` or environment variable `TELEGRAM_TOKEN` : token of your telegram bot  
    `chat_id` or environment variable `TELEGRAM_CHAT_ID` : chat id of your telegram bot  

- [bwa.gmail](https://www.notion.so/somniumis/Gmail-197fc3dcf2f74c9dba651afb19267747#58e9db16a1544a9484a88d2d5857c5ba)  
    `receiver_emails` : email address of receivers  
    `sender_email` or environment variable `SENDER_EMAIL` : sender's Gmail address  
    `sender_password` or environment variable `SENDER_PASSWORD` : sender's Gmail password

Please refer to our [Notion page](https://www.notion.so/somniumis/Bwa-Simple-Notification-Sender-a9919a46f2d64d11baab60deb4e8de55) , if you want to know what each parameter means and how you can get it.

Also, please refer to [/examples](https://github.com/somniumism/bwa/tree/main/examples) in Github for the example code of each client.

## Output format(Default)

**bwa** provides `custom_content` parameters to help you send your own messages. If you do not enter `custom_content`, however, you will be notified in the default format set by **bwa**; it is as follows. Because it is an example, there may be a difference from the actual results.

### When the function starts:

```
🏃 Your function <function_name> has started.
    - function name: function_name
    - start time: 2020-10-27 20:47:32
```

### When the function is complete:

```
🎉 Your function <function_name> is complete!
    - function name: function_name
    - start time: 2020-10-27 20:47:24
    - end time: 2020-10-27 20:47:27
    - run time: 0:00:02.970100
```

### When the function is ended due to an unexpected error:

```
😭 Your function <function_name> ended unexpectedly due to an exception or error.
    - function name: function_name
    - start time: 2020-10-25 01:25:06
    - dead time: 2020-10-25 01:25:12
    - run time: 0:00:05.774958
    - Error Info:

    - Traceback:
    Traceback (most recent call last):
    File "/Users/test-user/test/gmail_test_case.py", line 83, in wrapper
```

## FAQ

Q. What does **bwa** mean?

A: **bwa** means 'look at' in Korean.
Importing such as `bwa.discord` can be translated into `look at discord` in Korean.


Q. What is the difference between Huggingface's **knockknock** and **bwa**?

A: I used `knockknock` a lot, and there were many inconveniences while using `knockknock`.

1. `knockknock` cannot send the custom message that the user wants. You have to send the message only in the format made by them.

2. Because `knockknock` does not support environment variables, you must write all parameters when using the decorator. In other words, it's not pretty and it's not simple.

3. `knockknock` only supports the decorator. You may want to be notified about the execution of the line rather than the execution of the function. However, it is not possible in `knockknock`, which only supports the decorator.

So I designed **bwa** to support all of the above functions and create a simply, pretty and user-friendly library.

- **bwa** provides a parameter `custom_content` so that you can send the message you want.

- **bwa** supports you to use environment variables. So you can use it very simply and pretty, like `@deco_noti()`.

- **bwa** provides a method `send_noti()` so that you can be notified on any line without being restricted to the function.

Most importantly, `knockknock` is 10 letters, but `bwa` is 3 letters. Short, simple and easy is best.

## Reference & Copyright

Referred to huggingface's [knockknock](https://github.com/huggingface/knockknock)

If you have any questions or any problems, please leave a Github issue or contact me by email.

Any advice, pull request, and collaboration that can be used on more diverse platforms or make it easier to send a notification is always welcome. : )

If you find something that you don't understand or have a wrong grammar in the English document, please contact or contribute at any time.

Copyright (c) 2020 SeungMin Lee | MIT License  
Author: SeungMin Lee(@somniumism)  
Contact: lsm.somniator@gmail.com
