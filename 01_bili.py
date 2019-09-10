# coding=utf-8
import requests, re
from lxml import etree

class biliSider:
    def __init__(self,url):
        self.url = url
        # 哔哩哔哩弹幕url
        self.danmu_url= 'https://comment.bilibili.com/{}.xml'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }

    def get_html(self,url):
        return requests.get(url,headers=self.headers).content.decode("utf-8")

    def run(self):
        #send request,get the result
        bl_html = self.get_html(self.url)

        with open('./bilibili.html', 'a',encoding='utf-8') as f:
            f.write(bl_html)
            f.write("\n")


if __name__ == '__main__':
    url = 'https://www.bilibili.com/video/av35219233'
    bili = biliSider(url)
    bili.run()