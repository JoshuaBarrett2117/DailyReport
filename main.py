#!/usr/bin/env python3
# new Env("MIUI-Auto-Task 环境配置")

from iQshow import IQshow
from ijingniu import IJingNiu

if __name__ == '__main__':
    i_qshow = IQshow()
    all_news = i_qshow.get_all_news_body()
    IJingNiu.send(all_news)
    #print(all_news)
