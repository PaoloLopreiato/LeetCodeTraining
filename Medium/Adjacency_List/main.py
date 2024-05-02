import collections

class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

#AshMap Option <-- MUCH MORE COOMON WAY
adjList = {"A" : [], "B" : []}

#They Give you a eges list and then build the adjList by myself
edges = [["A","B"],["B","C"],["B","E"],["C","E"],["E","D"]]

adjList = {}

for src, dst in edges:
    if src not in adjList:
        adjList[src] = []
    if dst not in adjList:
        adjList[dst] = []
    adjList[src].append(dst)
    
    
#DFS Count paths (backtraking)
def dfs(node, target, adjList, visit):
    if node in visit:
        return 0
    if node == target:
        return 1
    
    count = 0 
    visit.add(node)
    for neighbor in adjList[node]:
        count += dfs(neighbor, target, adjList, visit)
    visit.remove(node)
    
    return count
print(dfs("A","E",adjList, set()))

#BFS (shortest path from nodem to target)
def bfs(node, target, adjList):
    length = 0
    visit = set()
    visit.add(node)
    queue = collections.deque()
    queue.append(node)
    
    while queue:
        for i in range(len(queue)):
            cur = queue.popleft()
            if cur == target:
                return length
            
            for neighbor in adjList[cur]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    queue.append(neighbor)
        length += 1
    return length

print(bfs("A","E", adjList))