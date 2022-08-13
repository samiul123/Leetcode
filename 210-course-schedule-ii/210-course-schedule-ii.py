# 0 -> 1
# 0 -> 2
# 1 -> 3
# 2 -> 3
#     0
#   1   2
#     3
# 0 1 2 3
# 0 2 1 3
# 0 - [1, 2] - [1, 2, 0] -> [0, 1, 2]
# 2 - [0] 
# 
# States
# 0 - Not visited
# 1 - In Process
# 2 - Done
# 

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = collections.defaultdict(list)
        
        for item in prerequisites:
            adjList[item[1]].append(item[0])
        
        NOT_VISITED = 0
        IN_PROCESS = 1
        VISITED = 2
        
        status = [NOT_VISITED] * numCourses
        isPossible = True
        orderedResult = []
        
        def dfs(courseToVisit, status):
            nonlocal isPossible
            
            if not isPossible:
                return
                
            status[courseToVisit] = IN_PROCESS
            
            for adjCourse in adjList[courseToVisit]:
                if status[adjCourse] == NOT_VISITED:
                    dfs(adjCourse, status)
                elif status[adjCourse] == IN_PROCESS:
                    isPossible = False
            
            status[courseToVisit] = VISITED
            orderedResult.append(courseToVisit)
        
        for i in range(numCourses):
            if status[i] == NOT_VISITED:
                dfs(i, status)
        
        return orderedResult[::-1] if isPossible else []