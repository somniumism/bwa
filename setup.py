import bwa
import setuptools

setuptools.setup(
    name="bwa",
    version=bwa.__version__,
    author=bwa.__author__,
    author_email='lsm.somniator@gmail.com',
    description="Bwa: Simple Notification Sender(Discord, Slack, Gmail and Telegram)",
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/somniumism/bwa',
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    keywords = [
        'notification-sender',
        'discord',
        'slack',
        'telegram',
        'gmail',
    ],
    install_requires=[
        'python-telegram-bot',
        'requests',
        'yagmail>=0.11.214',
    ],
    classifiers=(
        "Programming Language :: Python :: 3.6",
        'License :: OSI Approved :: MIT License',
    ),
)