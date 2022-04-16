class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numSet = set()
        
        for i in nums:
            numSet.add(i)
        
        for i in range(len(nums)+1):
            if i not in numSet:
                return i
        