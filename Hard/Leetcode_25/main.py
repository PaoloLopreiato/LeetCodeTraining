# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#Input: head = [1,2,3,4,5], k = 2
#Output: [2,1,4,3,5]
head = [1,2,3,4,5]
k = 2

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0, head)
        groupPrev = dummy
        
        while True:
            kth = self.getK(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            
            #Reverse
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            #Tumor
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next
        
    def getK(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr