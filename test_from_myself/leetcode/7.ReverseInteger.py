"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only hold integers 
within the 32-bit signed integer range. For the purpose of this problem, 
assume that your function returns 0 when the reversed integer overflows.
"""
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret=0
        if x>=0:
            ret= int(str(x)[::-1])
        else:
            ret= int(str(-x)[::-1])*(-1)
        
        if (-2)**31< ret <2**31:
            return ret
        else:
            return 0


if __name__ == '__main__':
    i=120
    s=Solution()
    x=s.reverse(i)
    print(x)
    print(type(x))

        