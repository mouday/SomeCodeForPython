# -*- coding: cp936 -*-
#���شʵ�
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

#�������ƥ�����ķִ�
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

#��������ʼ
filename="lexicon.dic"
max_length,word_dic=load_dic(filename)
print max_length
print word_dic
#sent=raw_input("input a sentence:\n")
sent="�Ұ������찲��"
words=fmm_word_seg(sent,max_length,word_dic)
for word in words:
    print word
