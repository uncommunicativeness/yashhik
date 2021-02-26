import json

import requests
from fake_useragent import UserAgent

import config


def send_to_screen(video_url):
    headers = {
        'method': 'GET',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
        'cache-control': 'max-age=0',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': UserAgent().random,
    }

    auth_data = {
        'login': config.login,
        'passwd': config.password
    }

    s = requests.Session()
    s.get("https://passport.yandex.ru/", headers=headers)
    s.post(
        "https://passport.yandex.ru/passport?mode=auth&retpath=https://yandex.ru",
        data=auth_data,
        headers=headers
    )

    Session_id = s.cookies["Session_id"]

    token = s.get('https://frontend.vh.yandex.ru/csrf_token').text

    devices_online_stats = s.get("https://quasar.yandex.ru/devices_online_stats").text
    devices = json.loads(devices_online_stats)["items"]

    headers = {
        "x-csrf-token": token,
    }

    data = {
        "msg": {
            "provider_item_id": video_url
        },
        "device": devices[0]["id"]
    }

    if "https://www.youtube" in video_url:
        data["msg"]["player_id"] = "youtube"

    res = s.post("https://yandex.ru/video/station", data=json.dumps(data), headers=headers)

    return res.text
