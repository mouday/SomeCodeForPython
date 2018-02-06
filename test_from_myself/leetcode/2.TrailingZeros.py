"""
Example
11! = 39916800, so the out should be 2
"""

class Solution:
    
    def factorial(self, n):
        #bad
        if n>0:
            return n*self.factorial(n-1)
        else:
            return 1
    
    def foo(self,n):
        #good
        ret=1
        for i in range(1,n+1):
            ret=ret*i
        return ret

    def trailingZeros_old(self, n):
        """
        @param: n: An integer
        @return: An integer, denote the number of trailing zeros in n!
        """
        # write your code here, try to do it without arithmetic operators.
        
        ret=1
        for i in range(1,n+1):
            ret=ret*i
        f=ret
        zero=0
        while (f//10 == f/10):
            f=f/10
            zero=zero+1
        return zero

    def trailingZeros(self, n):
        count=0
        while n > 0:
            ans = n // 5
            count+=ans
            n = ans
        return count

if __name__ == '__main__':
    s=Solution()
    # ret=s.trailingZeros(11)
    x=15
    print(s.foo(x))
    ret=s.trailingZeros(x)
    
    print(ret)