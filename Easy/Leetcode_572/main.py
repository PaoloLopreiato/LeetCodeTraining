# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if not subRoot:
            return True

        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
                
    
    def sameTree(self, p, q):

        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            # Recursively check left and right subtrees
            return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
        
        return False
            