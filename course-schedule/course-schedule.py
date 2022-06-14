class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         build the graph
        
        dependencyMap = collections.defaultdict(list)
        
        for prerequisite in prerequisites:
            course, prevCourse = prerequisite[0], prerequisite[1]
            dependencyMap[prevCourse].append(course)
            
        checked = [False] * numCourses
        path = [False] * numCourses
        for course in range(numCourses):
            if self.isCyclic(course, dependencyMap, path, checked):
                return False
        return True
    
    def isCyclic(self, currCourse, dependencyMap, path, checked):
        if checked[currCourse]:
            return False
        
        if path[currCourse]:
            return True
        
        path[currCourse] = True
        
        isCyclic = False
        for child in dependencyMap[currCourse]:
            isCyclic = self.isCyclic(child, dependencyMap, path, checked)
            if isCyclic:
                break
        
        path[currCourse] = False
        
        checked[currCourse] = True
        
        return isCyclic
                
            