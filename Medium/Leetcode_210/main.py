class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = {c : [] for c in range(numCourses)}
        
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        output = []
        visit, cycle = set(), set()
            
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True #skip course
            
            cycle.add(crs)
            for pre in adjList[crs]:
                if not dfs(pre):
                    return False
            
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return output
                