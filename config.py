import os

login = os.environ.get('login')
password = os.environ.get('password')
telegram_bot_token = os.environ.get('token')
authorised_users = [int(user_id) for user_id in os.environ.get('authorised_users_str').split(",")]

if proxy := os.environ.get('proxy'):
    proxy = {
        'proxy_url': proxy
    }
else:
    proxy = None
