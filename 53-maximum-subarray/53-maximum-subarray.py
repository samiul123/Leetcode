class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxEnding = nums[0]
        maxSum = maxEnding
        
        for i in range(1, len(nums)):
            maxEnding = max(maxEnding + nums[i], nums[i])
            maxSum = max(maxEnding, maxSum)
            
        return maxSum
        