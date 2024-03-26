class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

#root = [1,None,2,3]
#Output: [1,3,2]

def main():
    #inorder_traversal(root)
    inorder_traversal_0(root)


#Recursive Function
def inorder_traversal(root):
    result = []

    def inorder_helper(node):
        if node:
            inorder_helper(node.left)
            result.append(node.val)
            inorder_helper(node.right)

    inorder_helper(root)
    return result

#Iterative Solution
def inorder_traversal_0(root):
    result = []
    stack = []
    current = root
    while current is not None and stack is not None:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.val)
        current = current.right
        
    return result

if __name__ == "__main__":
    main()