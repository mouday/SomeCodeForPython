
from wordcloud import WordCloud
import matplotlib.pyplot as plt

text=open("My Father.txt","r").read()
# 生成词云
wordcloud=WordCloud().generate(text)
# 显示词云图片
plt.imshow(wordcloud)
plt.axis("off") #轴线关闭
plt.show()
# 保存图片
wordcloud.to_file("text.jpg")