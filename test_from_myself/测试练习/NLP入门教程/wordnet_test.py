from nltk.corpus import wordnet
from nltk.stem import PorterStemmer  # 波特词干算法

# 获取定义
syn = wordnet.synsets("pain")
print(syn[0].definition())
print(syn[0].examples())

syn = wordnet.synsets("NLP")
print(syn[0].definition())

syn = wordnet.synsets("python")
print(syn[0].definition())


# 获取同义词
synonyms = []
for syn in wordnet.synsets("computer"):
    for lemma in syn.lemmas():
        synonyms.append(lemma.name())

print(synonyms)


# 获取反义词
antonyms = []
for syn in wordnet.synsets("small"):
    for lemma in syn.lemmas():
        if lemma.antonyms():
            antonyms.append(lemma.antonyms()[0].name())

print(antonyms)

# 词干提取
stemmer = PorterStemmer()
print(stemmer.stem("working"))
print(stemmer.stem("worked"))