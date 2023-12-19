import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nodes = []
        counter = Counter(nums)
        for value, count in counter.items():
            # as heapq.heapify constructs minheap, but we have to construct maxheap, count is made negative here.
            nodes.append((-count, value))

        heapq.heapify(nodes)

        result = []
        for i in range(k):
            # extract top k value
            result.append(heapq.heappop(nodes)[1])

        return result
