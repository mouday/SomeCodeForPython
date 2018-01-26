from wordcloud import WordCloud
import matplotlib.pyplot as plt

#value相当于权重
text_dict={
    'you': 1,
    'and': 2,
    'in': 3,
    'was': 4,
    'the': 5,
}

wordcloud=WordCloud().generate_from_frequencies(text_dict)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
wordcloud.to_file("text_dict.jpg")