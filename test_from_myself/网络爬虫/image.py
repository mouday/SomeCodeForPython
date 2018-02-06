#-*- coding:utf-8 -*-
import re
import requests
import os

##url = 'http://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1460997499750_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%B0%8F%E9%BB%84%E4%BA%BA'
url="http://www.nationalgeographic.com.cn/travel/destinations/7739.html"

html = requests.get(url).text
pic_url = re.findall('"objURL":"(.*?)",',html)
i = 0
for each in pic_url:
    print(each)
    try:
        pic= requests.get(each, timeout=10)
    except requests.exceptions.ConnectionError:
        print ('【错误】当前图片无法下载')
        continue
    if not os.path.exists("D:\\pictures\\"):
        os.mkdir("D:\\pictures\\")
    string = 'D:\\pictures\\'+str(i) + '.jpg'        
    fp = open(string,'wb')
    fp.write(pic.content)
    fp.close()
    i += 1
