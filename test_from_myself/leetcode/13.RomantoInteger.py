# Given a roman numeral, convert it to an integer.
# Input is guaranteed to be within the range from 1 to 3999.
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 

        romans={"I": 1,"V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
        ret=0
        pre=0
        for i in s[::-1]:
            # print(i)
            current = romans.get(i,0)
            if current < pre:
                ret -= current
            else:
                ret += current
            pre = current 
        return ret


if __name__ == '__main__': 
    s=Solution()
    ret=s.romanToInt("IV")
    print(type(ret),ret)

