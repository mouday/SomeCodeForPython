# getHtml.py
import requests

'''
函数说明:获取页面内容
Parameters:
    url - 页面地址(string)
Returns:
    html - 页面内容(string)
Modify:
    2017-11-13
'''
def getHTML(url):
    try:
        r=requests.get(url,verify=False,headers=headers)
        r.raise_for_status()#抛出异常
        r.encoding=r.apparent_encoding #设置编码
        html=r.text
        return html
    except:
        return "<<<<<下载错误>>>>>"

# indent:缩进