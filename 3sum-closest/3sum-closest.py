class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closestSum = math.inf
        nums.sort()
        
        for i in range(len(nums)-2):
            curr = nums[i]
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                currentSum = curr + nums[left] + nums[right]
                
                if currentSum == target:
                    return currentSum
                
                diffCurrentSumTarget = abs(target - currentSum)
                diffClosestSumTarget = abs(target - closestSum)
                
                if diffCurrentSumTarget < diffClosestSumTarget:
                    closestSum = currentSum
                
                if currentSum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closestSum