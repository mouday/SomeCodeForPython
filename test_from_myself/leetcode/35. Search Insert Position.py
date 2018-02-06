"""
35. Search Insert Position
Given a sorted array and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Example 1:
Input: [1,3,5,6], 5
Output: 2

Example 2:
Input: [1,3,5,6], 2
Output: 1

Example 3:
Input: [1,3,5,6], 7
Output: 4

Example 1:
Input: [1,3,5,6], 0
Output: 0
"""

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums = sorted(nums)
            return nums.index(target)

if __name__ == '__main__':
    s= Solution()
    nums = [1,3,5,6]
    target = 4
    res = s.searchInsert(nums, target)
    print(res)