#爬虫爬取小说《芈月传》.py
#http://www.136book.com/mieyuechuanheji/

import requests
from bs4 import BeautifulSoup
import bs4

def getHtml(url):
	try:
		kv={"user-agent":"Mozilla/5.0"}
		r=requests.get(url,headers=kv)
		r.raise_for_status()
		r.encoding=r.apparent_encoding
		return r.text
	except:
		return ""

def getList(html):#《芈月传》
	lst=[]
	soup=BeautifulSoup(html,"html.parser")
	div=soup.find("center").find("div").find_next("div")
	for link in div.ol.children:
		if isinstance(link,bs4.element.Tag):	#排除非标签元素	
			lst.append([link.get_text(),link.a.get("href")])
	return lst

def getText(html):#《芈月传》
	soup=BeautifulSoup(html,"html.parser")
	div=soup.find("div",id="main_body")
	#标题
	head=div.find("h1")
	#内容
	content=div.find("div",id="content")
	content.script.extract()#extract()排除无效标签script
	return head.string,content.text

def main():
	#获取文章列表
	print("获取文章列表中。。。")
	url="http://www.136book.com/mieyuechuanheji/"
	html=getHtml(url)
	lst=getList(html)
	with open("芈月传目录.txt","w") as f:
		for l in lst:
			f.write(l[0]+","+l[1]+"\n")
	print("保存文章列表成功！")

	#获取文章内容
	print("获取文章内容中。。。")
	f=open("芈月传.txt","w") 
	for l in lst:
		html=getHtml(l[1])
		head,content=getText(html)
		f.write(head+"\n")
		f.write(content+"\n")
	f.close()

	print("保存文章内容成功！")
	
main()