class Solution:
    def missingNumber(self, nums: List[int]) -> int:
#         numSet = set()
        
#         for i in nums:
#             numSet.add(i)
        
#         for i in range(len(nums)+1):
#             if i not in numSet:
#                 return i
        length = len(nums)
        sumInRange = 0
        for i in range(length+1):
            sumInRange += i
        
        sumInNums = 0
        for i in nums:
            sumInNums += i
        
        return sumInRange - sumInNums
        