from nltk import tokenize

text= "Hello Adam, how are you? I hope everything is going well. Today is a good day, see you dude."
print(tokenize.sent_tokenize(text))


text2 ="Hello Mr. Adam, how are you? I hope everything is going well. Today is a good day, see you dude."
print("句子", tokenize.sent_tokenize(text2))

print("单词", tokenize.word_tokenize(text2))


text3 = "你好，我是中国人，你是谁？"   # 中文不行，可以试试jeiba库
print("句子", tokenize.sent_tokenize(text3))

print("单词", tokenize.word_tokenize(text3))

