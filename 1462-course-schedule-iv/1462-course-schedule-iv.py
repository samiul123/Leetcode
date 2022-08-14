# 1 -> [2, 0]
# 2 -> 0
# 
# pseudo algo
# build the adjacency list (edge will be directed from the course on whch others are depended towards the dependants)
# Recurse through only non_visited nodes to determine the dependecy in queries

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = collections.defaultdict(list)
        
        for src, dest in prerequisites:
            adjList[src].append(dest)
            
        NOT_VISITED = 0
        VISITED = 2
        
        answer = [False] * len(queries)
        
        def dfs(course, status, queryIndex):
            nonlocal answer
            
            if answer[queryIndex]:
                return        
            
            for dependantCourse in adjList[course]:
                if status[dependantCourse] == NOT_VISITED:
                    if dependantCourse == queries[queryIndex][1]:
                        answer[queryIndex] = True
                        return
                    dfs(dependantCourse, status, queryIndex)
            
            status[course] = VISITED
        
        
        for index, query in enumerate(queries):
            status = [NOT_VISITED] * numCourses
            dfs(query[0], status, index)
    
        return answer
            
        
        