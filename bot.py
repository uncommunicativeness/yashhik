import logging

from pytube import YouTube
from telegram.ext import Updater, MessageHandler, Filters

import config
from yandex import send_to_screen

logging.basicConfig(level=logging.DEBUG)
last_url = ""
authorised_users = config.authorised_users


def get_video_url(url):
    global last_url

    if url == last_url:
        yt = YouTube(url).streams.first()
        last_url = url
        return yt.url

    last_url = url

    if "https://www.youtube" in url:
        url = url.split("&")[0]

    if "https://youtu.be" in url:
        url = "https://www.youtube.com/watch?v=" + url.split("/")[-1]

    return url


def extract_url(message):
    return message.text  # TODO: getting url by entities info


def message_received(update, callback):
    user_id = update.message.chat_id

    if user_id not in authorised_users:
        callback.bot.send_message(chat_id=update.message.chat_id, text="Unauthorised request blocked!")
        return

    url = extract_url(update.message)
    video_url = get_video_url(url)
    result = send_to_screen(video_url)

    callback.bot.send_message(chat_id=update.message.chat_id, text=result + video_url)


updater = Updater(token=config.telegram_bot_token, request_kwargs=config.proxy)

message_handler = MessageHandler(Filters.all, message_received)
updater.dispatcher.add_handler(message_handler)

updater.start_polling()
