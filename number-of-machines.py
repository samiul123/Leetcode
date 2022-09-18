
from queue import PriorityQueue
import heapq

def findNumberOfMachines(intervals):
    if len(intervals) == 0:
        return 0
    intervals.sort()
    min_heap = []
    heapq.heappush(min_heap, intervals[0][1])

    for i in range(1, len(intervals)):
        interval = intervals[i]

        if interval[0] >= min_heap[0]:
            heapq.heappop(min_heap)
        
        heapq.heappush(min_heap, interval[1])
    
    return len(min_heap)


print(findNumberOfMachines([[1, 5], [5, 10], [4, 12]]))