# -*- coding: utf-8 -*-
# !/usr/bin/env python3
# cron:0 0/1 * * *
# new Env("影巢签到")

import json

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
    check_in = HdhiveCheckIn(
        f'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTc0ODg0MTQ0MCwianRpIjoiNWZmN2U4NDYtNTgxZC00Mzk3LTg0Y2ItZTQ0YzM1NDFlYThmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MzY2NTMsIm5iZiI6MTc0ODg0MTQ0MCwiY3NyZiI6IjRlYzM5MzBiLTE3MjktNGQ1Mi04MDE2LWU0ODE5OTc4YjhlZCIsImV4cCI6MTc0OTQ0NjI0MH0.K9A_FcsS-RPy1QxJXAnYdqJmh1FPKU-KQMlnBes25q0')
    # check_in = HdhiveCheckIn(os.getenv("DAYIMA_TOKEN"))
    main = check_in.main()
    print(main)
