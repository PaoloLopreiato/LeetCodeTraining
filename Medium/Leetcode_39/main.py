class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, cur, total):   
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total> target:
                return
            #add
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            #No add 
            cur.pop()
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res