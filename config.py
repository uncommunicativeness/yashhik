import os

login = os.environ.get('login')
password = os.environ.get('password')
telegram_bot_token = os.environ.get('token')

if proxy := os.environ.get('proxy'):
    proxy = {
        'proxy_url': proxy
    }
else:
    proxy = None
