class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        count = 0
        nums.sort()
        
        for i in range(len(nums) - 2):
            left, right = i+1, len(nums) - 1
            
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                
                if sum < target:
                    count += right - left
                    left += 1
                
                else:
                    right -= 1  
        
        return count
                    