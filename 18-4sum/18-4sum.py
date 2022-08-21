# [1, 0, -1, 0, -2, 2] target = 0
# [-2, -1, 0, 0, 1, 2]
# i = 0, j = i+1
# left, right = j+1, len(nums) - 1
# sum = target -> push (nums[i], nums[j], nums[left], nums[right])
# sum < target: left ++
# else: right --



class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = set()
        
        for i in range(len(nums) - 3):
            for j in range(i+1, len(nums) - 2):
                left, right = j+1, len(nums) - 1
                
                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if sum == target:
                        result.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    
                    elif sum < target:
                        left += 1
                    
                    else:
                        right -= 1
        
        return result
                
        