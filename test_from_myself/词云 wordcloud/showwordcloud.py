
from scipy.misc import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
from collections import Counter
import os

'''
函数功能：显示并保存词云图片
Parameters:
    filename - 文件路径（编码utf-8）
    image - 图片路径（词云形状）
Returns:
    无
'''
def showWordCloud(filename,image="heart.png"):
    
    # 读入文件，windows 下过滤编码错误
    text=open(filename,encoding="utf-8",errors="ignore").read()
    
    # 使用 jieba 分词
    text_jieba=list(jieba.cut(text))
    
    # 使用 counter 做词频统计，选取出现频率前 100 的词汇
    counter=Counter(text_jieba)
    counter_common=counter.most_common(100)

    # for i in counter_common:
    #     print(i)

    # 读入图片
    bg_png=imread(image)

    # 配置词云参数
    wordcloud=WordCloud(
        font_path="msyh.ttf",# 设置字体
        background_color="white",# 设置背景色
        mask=bg_png,     # 词云形状
        max_words=200,   # 允许最大词汇
        max_font_size=100,  # 最大号字体
        )

    # 生成词云
    wordcloud.generate_from_frequencies(dict(counter_common))
    
    # 生成图片并显示
    plt.figure(filename)
    # plt.title("测试")
    # plt.font("微软雅黑")
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

    # 保存图片
    name=os.path.splitext(filename)[0]+".jpg"
    wordcloud.to_file(name)

def main():
    filename="习总书记十九大报告全文.txt"
    showWordCloud(filename)

if __name__ == '__main__':
    main()