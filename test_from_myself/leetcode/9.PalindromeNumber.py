class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y=str(x)[::-1]
        if y == str(x):
            return True
        else:
            return False
        

if __name__ == '__main__':
    s=Solution()
    x=12345654321
    print(s.isPalindrome(x))