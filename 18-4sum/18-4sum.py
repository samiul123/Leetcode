# [1, 0, -1, 0, -2, 2] target = 0
# [-2, -1, 0, 0, 1, 2]
# i = 0, j = i+1
# left, right = j+1, len(nums) - 1
# sum = target -> push (nums[i], nums[j], nums[left], nums[right])
# sum < target: left ++
# else: right --


# [-5,-4,-3,-2,1,3,3,5] target = -11
# 

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = set()
        
        for i in range(len(nums) - 3):
            if i == 0 or nums[i] != nums[i-1]:
                self.threeSum(nums, i, result, target - nums[i])
        
        return result
    
    
    def threeSum(self, nums: List[int], i: int, result: List[List[int]], target: int):
        for j in range(i+1, len(nums) - 2):
            if j == i+1 or nums[j] != nums[j-1]:
                self.twoSum(nums, i, j, result, target - nums[j])
            
    
    def twoSum(self, nums: List[int], i: int, j: int, result: List[List[int]], target: int):
        left, right = j+1, len(nums) - 1

        while left < right:
            sum = nums[left] + nums[right]

            if sum == target:
                result.add((nums[i], nums[j], nums[left], nums[right]))
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1

            elif sum < target:
                left += 1

            else:
                right -= 1
            
        