import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        allotted_rooms = []
        
        heapq.heappush(allotted_rooms, intervals[0][1])
        for i in intervals[1:]:
            if allotted_rooms[0] <= i[0]:
                heapq.heappop(allotted_rooms)
            heapq.heappush(allotted_rooms, i[1])
            
        return len(allotted_rooms)
        
        