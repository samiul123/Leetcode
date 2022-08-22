class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # O(NlogN + N^2) -Time
        # O(1) - Space
        nums.sort()
        minDiff = math.inf
        resultSum = 0
        
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                diff = abs(target - sum)
                
                if diff < minDiff:
                    minDiff = diff
                    resultSum = sum
                    
                if sum == target:
                    return resultSum
                
                elif sum > target:
                    right -= 1
                else:
                    left += 1
                    
        return resultSum