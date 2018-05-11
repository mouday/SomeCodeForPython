# -*- coding: cp936 -*-
#加载词典
def load_dic(filename):
    f=open(filename)
    word_dic=set()
    max_length=1
    for line in f:
        word=unicode(line.strip(),'utf-8')
        word_dic.add(word)
        if len(word)>max_length:
            max_length=len(word)
    f.close()
    return max_length,word_dic

#正向最大匹配中文分词
def fmm_word_seg(sent,word_dic,max_len):
    begin=0
    words=[]
    sent=unicode(sent,'utf-8')

    while begin<len(sent):
        for end in range(begin + max_len,begin,-1):
            if sent[begin:end] in word_dic:
                words.append(sent[begin:end])
                break
        begin=end
    return words

#主函数开始
filename="lexicon.dic"
max_length,word_dic=load_dic(filename)
print max_length
print word_dic
#sent=raw_input("input a sentence:\n")
sent="我爱北京天安门"
words=fmm_word_seg(sent,max_length,word_dic)
for word in words:
    print word
