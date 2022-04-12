class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()
        for index, currentNumber in enumerate(nums[:-2]):
            remaining = 0 - currentNumber
            left = index + 1
            right = len(nums)-1
            while left < right:
                sumLeftRight = nums[left] + nums[right]
                if sumLeftRight < remaining:
                    left += 1
                elif sumLeftRight > remaining:
                    right -= 1
                else:
                    result.add((currentNumber, nums[left], nums[right]))
                    left += 1
                    right -= 1
        return result
#         nums.sort()
#         triplets = set()
#         for i in range(len(nums) - 2):
#             left = i + 1
#             right = len(nums) - 1
            
#             while left < right:
#                 trip_sum = nums[i] + nums[left] + nums[right]
#                 if trip_sum == 0:
#                     triplets.add((nums[i], nums[left], nums[right]))
                
#                 # If the current triplet sum is negative, or if we already have a triplet of 0 and want to try another combination
#                 # advance the right pointer
#                 # The left pointer will advance non decreasingly
#                 # The right pointer will advance non increasingly
#                 if trip_sum <= 0:
#                     left += 1
#                 else:
#                     right -= 1
                    
                    
#         return list(triplets)
#         triplets = set()
#         dups = set()
#         numSet = {}
#         for i in range(len(nums)):
#             currentNum = nums[i]
#             if currentNum not in dups:
#                 target = 0 - currentNum
#                 dups.add(currentNum)

                
#                 for j in range(i+1, len(nums)):
#                     potential = target - nums[j]
#                     if potential in numSet and numSet[potential] != i and numSet[potential] != j:
#                         triplets.add(tuple(sorted([nums[i], potential, nums[j]])))
#                     else:
#                         numSet[nums[j]] = j
                    
#         return triplets


        