# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#Input: root = [1,2,3,4,5]
#Output: 3
#Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

#Recursive DFS using hight and diameter
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        
        def dfs(root):
            if not root:
                return -1
                    
            left = dfs(root.left)
            right = dfs(root.right)
            
            res[0] = max(res[0], 2 + left + right)
        
            return 1 + max(left, right)
        dfs(root)
        return res[0]