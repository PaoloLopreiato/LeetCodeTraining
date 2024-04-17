# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
"""
head = [3,2,0,-4]
pos = 1

#MY SOLUTION O(n)
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ash = {}
        cur = head
        while cur:
            if cur in ash:
                return True
            ash[cur] = cur
            cur = cur.next
        return False
    
#GODTIER O(1)
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        s, f = head, head
        while f and f.next:
            s = s.next
            f = f.next.next
            if f == s:
                return True
        return False