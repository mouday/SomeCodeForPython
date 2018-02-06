# Write a function to find the longest common prefix string amongst an array of strings.
from functools import reduce

class Solution:
    def longestCommonPrefix1(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        miniPrefix = min(strs) # 找到最短的字符
        isprefix=False
        while not isprefix:
            for s in strs:
                if miniPrefix ==s[:len(miniPrefix)]:
                    isprefix=True
                else:
                    isprefix=False                
                    miniPrefix=miniPrefix[:len(miniPrefix)-1]
                    break
        return miniPrefix

    def longestCommonPrefix(self, strs):
        def lcp(s, t):
            if len(s)>len(t):
                s, t = t, s
            for i in range(len(s)):
                if s[i]!=t[i]:
                    return s[:i]
            return s
        return reduce(lcp,strs) if strs else ""

def main():
    s=Solution()
    names=["xxoxoo","xxoxoo","xxoxxoo","xxoxoo"]
    ret=s.longestCommonPrefix(names)
    print(ret)


if __name__ == '__main__':
    main()