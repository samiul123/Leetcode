class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        count = 0
        nums.sort()
        
        for i in range(len(nums) - 2):
            left, right = i+1, len(nums) - 1
            
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                
                if sum < target:
                    # IMPORTANT
                    # TRICKY PART HERE
                    # IF THREESUM < TARGET, THEN BECAUSE THEE ARRAY IS SORTED
                    # ALL NUMBERS IN BETWEEN WILL ALSO BE LESS OR EQUAL TO K
                    # AND THEREFORE BE VALID ANSWERS
                    count += right - left
                    left += 1
                
                else:
                    right -= 1  
        
        return count