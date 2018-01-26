# URL：https://unsplash.com/
import requests,json,time,sys
from contextlib import closing

class getPhotos(object):

    def __init__(self):
        self.photosIds=[]
        self.downloadServer="https://unsplash.com/photos/xxx/download?force=trues"
        self.target="http://unsplash.com/napi/feeds/home"
        self.headers={"authorization":"Client-ID c94869b36aa272dd62dfaeefed769d4115fb3189a9d1ec88ed457207747be626"}

    '''
    函数说明:获取页面内容
    Parameters:
        url - 页面地址(string)
    Returns:
        html - 页面内容(string)
    Modify:
        2017-11-13
    '''
    def getHTML(self,url):
        # try:
        #authorization 基于AAA模型中的身份验证信息允许访问一种资源的行为
        r=requests.get(url,verify=False,headers=self.headers)
        # r.raise_for_status()#抛出异常
        r.encoding=r.apparent_encoding #设置编码
        html=r.text
        return html

    """
    函数说明:获取图片ID
    Parameters:
        无
    Returns:
        无
    Modify:
        2017-09-13
    """
    def getIds(self):
        html=self.getHTML(self.target)
        jsonParser=json.loads(html)
        next_page=jsonParser["next_page"]
        #print("下一页地址：",next_page)
        for each in jsonParser["photos"]:
            self.photosIds.append(each["id"])
        time.sleep(1)#1s延时

        for i in range(4):
            html=self.getHTML(next_page)
            jsonParser=json.loads(html)
            next_page=jsonParser["next_page"]
            for each in jsonParser["photos"]:
                self.photosIds.append(each["id"])
            time.sleep(1)#1s延时
    """
    函数说明:图片下载
    Parameters:
        无
    Returns:
        无
    Modify:
        2017-09-13
    """ 
    def download(self,photosId,filename):
        headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36"}       
        target=self.downloadServer.replace("xxx",photosId)
        with closing(requests.get(url=target,stream=True,verify=False,headers=self.headers)) as r:
            with open("%d.jpg"%filename,"ab+") as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()

def main():
    gp=getPhotos()
    print("获取图片链接中。。。")
    gp.getIds()
    print("图片下载中。。。")
    for i in range(len(gp.photosIds)):
        print("正在下载第%d张图片"%(i+1))
        gp.download(gp.photosIds[i],(i+1))

if __name__ == '__main__':
    main()

# print(html)
