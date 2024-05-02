class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i : [] for i in range(numCourses)}
        
        for course, prerequisite in prerequisites:
            adjList[course].append(prerequisite)
            
        visit = set()
        
        def dfs(course):
            if course in visit:
                return False
            if adjList[course] == []:
                return True
            
            visit.add(course)
            for pre in adjList[course]:
                if not dfs(pre): 
                    return False      
            visit.remove(course)
            adjList[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
        