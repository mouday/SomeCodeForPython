
# 小说网站笔趣看  《一念永恒》

import requests
import sys
import getHtml
from bs4 import BeautifulSoup

'''
类说明:下载《笔趣看》网小说《一念永恒》
Parameters:None
Returns:None
Modify:2017-11-13
'''
class Downloader(object):

    def __init__(self):
        self.server = "http://www.biqukan.com"
        self.target = "http://www.biqukan.com/1_1094/"
        self.names = []     #存放章节名
        self.urls = []      #存放章节链接
        self.nums = 0;      #章节数
    """
    函数说明:获取章节内容
    Parameters:
        target - 下载连接(string)
    Returns:
        texts - 章节内容(string)
    Modify:
        2017-09-13
    """
    def getPage(self,target):
        html=getHtml.getHTML(target)
        bs=BeautifulSoup(html,"html.parser")
        # find_all( name , attrs , recursive , string , **kwargs )
        showTxt=bs.find_all("div",class_="showtxt")#返回一个列表
        texts=showTxt[0].text.replace("\xa0"*8,"\n\n")  #剔除空格，替换为回车
        return texts

    """
    函数说明:获取下载链接
    Parameters:
        无
    Returns:
        names   #章节名(string)
        urls    #章节连接(string)
    Modify:
        2017-09-13
    """
    def getList(self):
        html = getHtml.getHTML(self.target)
        soup = BeautifulSoup(html,"html.parser")
        listmain = soup.find_all("div",class_="listmain")
        #print(listmain[0])
        soup_a = BeautifulSoup(str(listmain[0]),"html.parser")
        a = soup_a.find_all("a")
        self.nums = len(a[15:]) #剔除不必要的章节，并统计章节数
        for each in a[15:]:
            self.names.append(each.string)
            self.urls.append(self.server+each.get("href"))
        print("nums:",self.nums)

    """
    函数说明:将爬取的文章内容写入文件
    Parameters:
        name - 章节名称(string)
        path - 当前路径下,小说保存名称(string)
        text - 章节内容(string)
    Returns:
        无
    Modify:
        2017-09-13
    """
    def writer(self,name,path,text):
        writeFlag=True
        with open(path,"a",encoding="utf-8") as f:
            f.write(name + "\n")
            f.writelines(text)
            f.write("\n\n")


def main():
    downloader=Downloader()
    downloader.getList()
    print("《一年永恒》开始下载：")
    for i in range(downloader.nums):
        #print("nums[%d]= %d"%(i,downloader.nums[i]))
        #print(i)
        downloader.writer(downloader.names[i],"一念永恒.txt",downloader.getPage(downloader.urls[i]))

        sys.stdout.write("  已下载:%.3f%%\r" %  (float(i/downloader.nums)*100))
        sys.stdout.flush()
    print("《一年永恒》下载完成")
    

if __name__ == '__main__':
    main()
