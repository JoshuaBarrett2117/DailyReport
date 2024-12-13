#!/usr/bin/env python3
# cron:0 0/1 * * *
# new Env("爱Q生活网")

import requests
from lxml import etree

from util.test import test_get_news_body


class IQshow(object):
    def __init__(self) -> None:
        super().__init__()
        self.url = "https://www.iqnew.com"

    def get_all_news_iter(self):
        # 请求url指定中文编码
        get = requests.get(self.url)
        get.encoding = 'gbk'
        html = get.text
        # 使用xpath解析
        element = etree.HTML(html)
        # 取/html/body/div[4]/div[2]/div[1]/div[2]/div[1]/ul[1]元素、
        nodes1 = element.xpath('/html/body/div[4]/div[2]/div[1]/div[2]/div[1]/ul[1]/li')
        nodes2 = element.xpath('/html/body/div[4]/div[2]/div[1]/div[2]/div[1]/ul[2]/li')

        nodes = nodes1 + nodes2
        for node in nodes:
            a_list = node.xpath('.//a')
            if len(a_list) >= 1:
                a = a_list[0]
                curr_url = self.url + a.attrib['href']
                node_text_list = node.xpath('.//text()')
                curr_title = node_text_list[1]
                curr_date = node_text_list[3]
                yield (curr_title, curr_url, curr_date)

    def get_all_news_body(self):
        news_iter = self.get_all_news_iter()
        # 遍历所有新闻
        # [支付宝问卷领1+2元转账红包 亲测1元秒到](https://www.iqnew.com/activity/201744.html) **07-19**
        md_body_list = ["[" + str(news[0]) + "](" + str(news[1]) + ") **" + str(news[2]) + "**" for news in news_iter]
        return "\n".join(md_body_list)


if __name__ == '__main__':
    test_get_news_body()
    i_qshow = IQshow()
    all_news = i_qshow.get_all_news_body()
    print(all_news)
