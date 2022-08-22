# The largest num + smallest < key, so we have 2 choices: 1. move right down, all elements are satisfied since r is the current largest one; => all the sum btw l and r is r-l.
# 2. move left up, we need to check if it is satisfied.

# for example,  we have -21, -3, -2, 2, 4,  5   target=2; 
# For the 1st nums[0] = -21, => key = 2+21 = 23
#     -3+5<23 ==> we know -3+5, -3+4, -3+2 and -3+-2 must be valid. That's why sum+= (hi-lo);
# Then move lo++, to check if ( (lo++) + hi) still < key.

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
                    # ALL NUMBERS IN BETWEEN WILL ALSO BE LESS OR EQUAL TO right
                    # AND THEREFORE BE VALID ANSWERS
                    count += right - left
                    left += 1
                
                else:
                    right -= 1  
        
        return count