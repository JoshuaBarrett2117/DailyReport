# -*- coding: utf-8 -*-
# !/usr/bin/env python3
# cron:0 0/1 * * *
# new Env("影巢签到")

import json
import os

import requests


class HdhiveCheckIn(object):
    def __init__(self, auth):
        self.auth = auth

    def main(self):
        session = requests.session()
        session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/63.0.3239.108",
                "Referer": "https://hdhive.online/",
                "Connection": "keep-alive",
                "Authorization": self.auth
            }
        )
        # 添加代理
        session.proxies = {
            "http": "http://192.168.31.12:7890",
            "https": "http://192.168.31.12:7890"
        }

        post = session.post(
            "https://hdhive.online/api/customer/user/checkin")
        # load = json.loads(post.text)

        msg = f"{post.text}"
        # unicode解码成中文
        msg = msg.encode().decode("unicode_escape")
        return msg


if __name__ == "__main__":
    check_in = HdhiveCheckIn(os.getenv("HDHIVE_AUTH"))
    main = check_in.main()
    print(main)
