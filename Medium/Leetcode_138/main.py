# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

#Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
#Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
head = [[7,null],[13,0],[11,4],[10,2],[1,0]]


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        oldToCopy = { None : None }
        
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next
        
        return oldToCopy[head]