
import urllib.request
from bs4 import BeautifulSoup  # 安装beautifsoup4
import nltk
from nltk.corpus import stopwords

# 抓取页面
response = urllib.request.urlopen("http://php.net/")
html = response.read()
# print(html)

# 内容清洗
soup = BeautifulSoup(html, "html5lib")  # 安装html5lib

text = soup.get_text(strip=True)
# print(text)

# 转为单词
tokens = text.split()
# print(tokens)

# 处理停用词
clean_tokens = list()
words = stopwords.words("english")
for token in tokens:
    if token not in words:
        clean_tokens.append(token)

# 词频统计
freq = nltk.FreqDist(clean_tokens)
for key, val in freq.items():
    print(str(key) + ":" + str(val))

# 频率分布图
freq.plot(20, cumulative=False)  # 安装 matplotlib

