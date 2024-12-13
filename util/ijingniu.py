import os

import requests


class IJingNiu(object):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def send(body):
        map = {
            'ChannelKey': os.getenv("SELF_TIMED_IJINGNIU_CHANNEL"),  # 设置服务器
            'TemId': '',
            'KeyWord1': '定时爬虫',
            'KeyWord2': '点击查看详情',
            'Head': '定时爬虫',
            'Body': body
        }
        print(map)
        headers = {
            "Content-Type": "application/json",
            "Accept-Encoding": "gzip, deflate, br"
        }
        post = requests.post(url="http://push.ijingniu.cn/push", json=map, headers=headers)
        print(post.text)
