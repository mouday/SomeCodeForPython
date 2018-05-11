class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,numi in enumerate(nums):
            for j,numj in enumerate(nums):
                if (numi+numj== target) and (numi!=numj):
                    return [i,j]

def main():
    s=Solution()
    nums=[3,2,4]
    target=6
    ret=s.twoSum(nums,target)
    print(ret)

if __name__=="__main__":
    main()
            
        