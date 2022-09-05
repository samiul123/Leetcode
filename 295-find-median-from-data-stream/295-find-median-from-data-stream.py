class MedianFinder:

    def __init__(self):
        self.store = []
        
    def addNum(self, num: int) -> None:
        self.insert(num)
        
    def findMedian(self) -> float:
        length = len(self.store)
        
        return self.store[length//2] if length % 2 else (self.store[length//2 - 1] + self.store[length//2]) * .5
    
    def insert(self, num):
        left, right = 0, len(self.store) - 1
        positionToInsert = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if self.store[mid] > num:
                right = mid - 1
            
            elif self.store[mid] < num:
                left = mid + 1
            else:
                positionToInsert = mid
                break
        
        if positionToInsert == -1:
            positionToInsert = left
        
        self.store.insert(positionToInsert, num)
        
        

# Sort Everytime while reading
# Space - O(n)

# class MedianFinder:

#     def __init__(self):
#         self.store = []
        
# # O(1) - Amortized
#     def addNum(self, num: int) -> None:
#         self.store.append(num)
        
# # O(nlogn) - Time
#     def findMedian(self) -> float:
#         self.store.sort()
#         length = len(self.store)
        
#         return self.store[length//2] if length % 2 else (self.store[length//2 - 1] + self.store[length//2]) * .5
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()