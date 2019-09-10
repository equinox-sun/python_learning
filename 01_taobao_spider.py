# coding=utf-8
import requests
from lxml import etree
import json

#中文编码，价格提取

class TaobaoSpider:
	def __init__(self, keyword):
		self.keyword=keyword
		self.start_url = "https://list.tmall.com/search_product.htm?q="+keyword
		self.part_url = "http://list.tmall.com/"
		self.headers= {"User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}

	def parse_url(self, url):  # 发送请求，获取响应
		print(url)
		response = requests.get(url, headers=self.headers)
		return response.content

	def get_content_list(self,html_str):
		html = etree.HTML(html_str)
		a_list = html.xpath("//a[contains(@class,'list_item')]")
		content_list = []
		for i in a_list:
			item = {}
			item["title"] = (i.xpath("//h3/text()")[0]).strip('\n ')  if len(i.xpath("//h3"))>0 else None
			item['href'] = i.xpath("@href")
			item['img'] = (i.xpath("//img/@src")[0]) if len(i.xpath("//img"))>0 else None
			item['shop_name'] = i.xpath("div/p/span/text()")
			item['sale_num'] = i.xpath("div/p/text()")[0].strip("\n月销笔 ")
			# 价格部分提取有问题
			item['price'] =(i.xpath("//div[@class='lii_price']//text()")[0]).strip('\n ') if len(i.xpath("//div[@class='lii_price']"))>0 else None
			content_list.append(item)
		return content_list

	def save_content_list(self,content_list):
		file_path = self.keyword+'.txt'
		with open(file_path,"a",encoding="utf-8") as f:
			for content in content_list:
				f.write(json.dumps(content,ensure_ascii=False,indent=2))
				f.write("\n")
		print('ok')

	def run(self):
		#1.获取首地址数据
		next_url = self.start_url
		#2.发送请求，获取响应
		html_str = self.parse_url(next_url)
		#3.提取数据
		content_list = self.get_content_list(html_str)
		self.save_content_list(content_list)

if __name__ == '__main__':
	taobao_spider = TaobaoSpider("充电宝")
	taobao_spider.run()