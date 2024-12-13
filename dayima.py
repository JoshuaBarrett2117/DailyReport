# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# cron:0 0/1 * * *
# new Env("大姨妈提示")

import json
import math
import time

import requests


class DayimaCheckIn(object):
    def __init__(self, token):
        self.token = token

    def main(self):
        session = requests.session()
        session.headers.update(
            {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/63.0.3239.108",
                "Referer": "https://www.bilibili.com/",
                "Connection": "keep-alive",
            }
        )
        post = session.post(
            "https://uicapi.yoloho.com/user/getinfo_v2?" +
            "device=1249100c51529b465b8eb0268b63094175b57a3d" +
            "&ver=600" +
            "&screen_width=1080" +
            "&screen_height=2206" +
            "&model=Mi+10+Pro" +
            "&sdkver=31" +
            "&platform=android" +
            "&releasever=12" +
            "&channel=" +
            "$channel" +
            "&latt=0" +
            "&lngt=0" +
            "&networkType=0" +
            "&period=2" +
            "&period_index=2" +
            f"&token={self.token}" +
            "&userStatus=0")
        load = json.loads(post.text)
        last_calendar_period = str(load["data"]["last_calendar_period"])
        cycle = int(load["data"]["cycle"])
        period = int(load["data"]["period"])
        time_struct = time.strptime(last_calendar_period, "%Y%m%d")
        time_stamp = int(time.mktime(time_struct)) + (cycle - 1) * 24 * 60 * 60
        strftime = time.strftime("%Y年%m月%d日", time.localtime(time_stamp))
        time_time = time.time()
        next_time_day = (time_stamp - time_time) / 60 / 60 / 24
        next_time_day = math.ceil(next_time_day)
        msg = f"距离经期还有{next_time_day}天\n\n大姨妈日：{strftime}"

        return msg


# check_in = DayimaCheckIn("275918897-c56a6c27d221ec7efc7b63ab65216b3e")
# check_in.main()
