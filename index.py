#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2020/12/29 11:16
# @Author : liufei
# @Version：V 0.1
# @File : index.py
# @desc :
import os
import time

import requests

from bili import BiliBiliCheckIn
from kny import KnyCheckIn
from dayima import DayimaCheckIn
from except_common import except_decorate
from mail import MailSender


def main_handler(event, context):
    msg = ''
    bilibili_cookies = "buvid3=19D7A144-6A87-629C-78CB-AA45AAF12EE312205infoc; b_nut=1690177212; _uuid=76A8BD66-A7F5-D910C-FAF4-D2C25CEB9BF916071infoc; buvid4=F64CFCF3-FD80-0BF9-E354-160BCD1D6F1013876-023072413-QXvvn0NnbsKmX6pkhQ91Vw%3D%3D; i-wanna-go-back=-1; b_ut=7; header_theme_version=CLOSE; DedeUserID=37963116; DedeUserID__ckMd5=70ea542e9b637ff1; buvid_fp_plain=undefined; CURRENT_FNVAL=4048; bp_video_offset_37963116=827677495457218592; rpdid=|(JYYRl||uRu0J'uYmkY~m||R; fingerprint=4f6c0d68665048f8cd746b634cc3e00f; innersign=0; b_lsid=919362FA_18A69BDDBFD; home_feed_column=4; buvid_fp=4f6c0d68665048f8cd746b634cc3e00f; SESSDATA=088e4a78%2C1709543164%2Cf7eb4%2A916n-EAWFmrPzBrVLqrkmP165VvEOvpB5cQ8qO1pcFg5N_3fIseIR6cdvWUHZMFKdoSlJBrQAAEAA; bili_jct=f177ba581b4d10728eec020fb3975c55; sid=88gn8w8u; browser_resolution=1122-196"
    msg = msg + "==============bilibili助手====================\n\n"
    bilibili = BiliBiliCheckIn(bilibili_cookie_list=[{"coin_num": 0,"coin_type":0,"money":0, "bilibili_cookie": bilibili_cookies}])
    msg = msg + except_decorate(bilibili.main)()
    msg = msg + "==============大姨妈助手==================\n\n"
    dayima = DayimaCheckIn(token="275918897-c56a6c27d221ec7efc7b63ab65216b3e")
    dayima_msg = f"{except_decorate(dayima.main)()}\n\n"
    msg = msg + dayima_msg
    msg = msg + "==============柯南云公告和订阅信息=============\n\n"
    ccb = KnyCheckIn(
        email="943034773@qq.com", password="jcboom17", host="kny88.shop"
    )
    msg = msg + f"{except_decorate(ccb.main)()}\n\n"
    msg = msg + "=============助手执行完成=================\n\n"
    msg = msg + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print(msg)

    server_jiang = "https://sctapi.ftqq.com/SCT11150TZR7otiynPSompg3cOcLcsuIQ.send"
    server_jiang_data = {'title': '签到执行结果', 'desp': msg,'channel':9}

    try:
        post = requests.post(url=server_jiang, data=server_jiang_data)
        print(post.text)
    except:
        print('server酱推送失败')

    mail_sender = MailSender("smtp.qq.com", "185849031@qq.com", "ffoeckfhisuycbdi")
    dayima_msg = f"""\
                <!DOCTYPE html>
                <html>
                    <body>
                        {dayima_msg}
                    </body>
                </html>
                """
    #
    mail_sender.send_to("大姨妈提醒", dayima_msg, [os.getenv("DAYIMA_SEND_TO_EMAIL")])


if __name__ == '__main__':
    main_handler(None, None)
