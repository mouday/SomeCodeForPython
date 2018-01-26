from scipy.misc import imread
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 读入图片
bg_png=imread("heart.png")

# 配置词云参数
wordcloud=WordCloud(
     # 设置字体
    #font_path="BeaverScratches.ttf",
    background_color="white",# 设置背景色
    max_words=200,# 允许最大词汇
    mask=bg_png,# 词云形状
    max_font_size=100,# 最大号字体
    )

text=open("My Father.txt","r").read()
# 生成词云
wordcloud.generate(text)
# 保存图片
wordcloud.to_file("heartPNG.jpg")

plt.imshow(wordcloud)
plt.axis("off")
plt.show()