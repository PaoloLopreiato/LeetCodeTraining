"""
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
"""

head = [1,2,3,4,5]
n = 2

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        