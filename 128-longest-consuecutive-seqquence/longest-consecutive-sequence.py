import math
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(nlogn)
        # if len(nums) == 0:
        #     return 0

        # nums.sort()
        # length = 1
        # max_length = -math.inf
        # for i in range(1, len(nums)):
        #     if nums[i] - nums[i-1] == 1:
        #         length += 1
        #     elif nums[i] - nums[i-1] == 0:
        #         continue
        #     else:
        #         max_length = max(max_length, length)
        #         length = 1
        # return max(max_length, length)

        # O(n)
        numSet = set(nums)
        max_length = 0

        for num in nums:
            if (num - 1) not in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1
                max_length = max(length, max_length)

        return max_length
