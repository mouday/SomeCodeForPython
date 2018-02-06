# anagram字母易位词.py
'''
两个单词如果包含相同的字母，次序不同，则称为字母易位词(anagram)。
例如，“silent”和“listen”是字母易位词，而“apple”和“aplee”不是易位词。
请定义函数检查两个单词是否是字母易位词。
可以假设两个单词字母均为小写。要求算法复杂度尽量低。
'''
def judgeAnagram(s1,s2):
    #判断是否为字母易位词
    isAnagram=False
    # 长度不等就不用判断了
    if len(s1)!=len(s2):
        return False
    else:
        d={}
        for i in range(len(s1)):
            d[s1[i]]=d.get(s1[i],0)+1
            d[s2[i]]=d.get(s2[i],0)+1
        for key in d.keys():
            if d[key]!=2:
                break
        else:
            isAnagram=True  
    return isAnagram

def main():
    s1="silent1"
    s2="listen"
    ret=judgeAnagram(s1,s2)
    print(ret)

if __name__ == '__main__':
    main()