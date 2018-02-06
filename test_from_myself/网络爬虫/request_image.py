import requests
import os
import re
def getHttpText(url):
    try:
        r= requests.get(url)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "except"

def getHttpImage(url,root):
    path=root+url.split("/")[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r= requests.get(url)
            with open(path,"wb") as f:
                f.write(r.content)
                f.close()
            return "文件保存成功"+path
        else:
            return "文件已经存在"+path
##        r.encoding = r.apparent_encoding
        
    except:
        return "except"
    
def main():
    url="http://www.baidu.com"
    imageurl="http://image.nationalgeographic.com.cn/2017/0617/20170617015100605.jpg"
    root="D:\\123\\"
    #图片地址过滤
##src="http://image.nationalgeographic.com.cn/2014/0710/20140710010928470.jpg"    
    reg=r'<img\ssrc=.{,80}.[jpg|png|gif]'
    #imgre = re.compile(reg)
    img_src0 = re.findall(reg,getHttpText(imageurl))
    img_src1=[img_src[10:] for img_src in img_src0]
    for img in img_src1:
        print(img)
##        print(getHttpImage(imageurl,root))

if __name__ =="__main__":
    main()


