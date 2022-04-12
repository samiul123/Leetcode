class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        dups = set()
        numSet = {}
        for i in range(len(nums)):
            currentNum = nums[i]
            if currentNum not in dups:
                target = 0 - currentNum
                dups.add(currentNum)

                
                for j in range(i+1, len(nums)):
                    potential = target - nums[j]
                    if potential in numSet and numSet[potential] != i and numSet[potential] != j:
                        triplets.add(tuple(sorted([nums[i], potential, nums[j]])))
                    else:
                        numSet[nums[j]] = j
                    
        return triplets