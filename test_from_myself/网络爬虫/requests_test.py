import requests
def getHttpText(url):
    try:
        r= requests.get(url)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "except"

def main():
    url="http://www.baidu.com"
    print(getHttpText(url))

if __name__ =="__main__":
    main()


