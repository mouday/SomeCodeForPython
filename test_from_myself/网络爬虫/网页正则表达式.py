import requests
import re
import os

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
    
url="http://www.nationalgeographic.com.cn/travel/destinations/7739.html"
r=requests.get(url)
r.encoding=r.apparent_encoding
#print(r.text)
text=r.text
pattern="<title>(.*?)</title>"
out=re.search(pattern,text,re.S).group(1)
print(out)
urls=re.findall("<img src=\"(.*?)\"",text,re.S)
#print(urls)
lst=[]
for url in urls:
    if url.find("http")>-1:
        lst.append(url)
        print(url)

root="D:\\image\\"
for l in lst:
    print(l)
    #print(getHttpImage(l,root))
    path=root+l.split("/")[-1]
   
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r= requests.get(l)
        with open(path,"wb") as f:
            f.write(r.content)
            f.close()
        print("保存成功",path)



