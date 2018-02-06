#getjpg.py
#coding=utf-8
from urllib import request

def getHtml(url):
    page = request.urlopen(url)
    html = page.read()
    return html

html = getHtml("http://www.cnblogs.com/fnng/p/3576154.html")

print(html)
