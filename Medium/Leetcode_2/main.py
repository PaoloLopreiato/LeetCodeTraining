# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""
l1 = [2,4,3]
l2 = [5,6,4]

#Not My Sol but ofc is BETTER
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode()
        cur = dummy
        
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            val = v1 + v2 + carry
            
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)
            
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
        
        
#My solution
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Step 1: Reverse the linked lists and extract numbers as strings
        n1 = self.reverse_and_convert_to_string(l1)
        n2 = self.reverse_and_convert_to_string(l2)
        
        # Step 2: Convert strings to integers, calculate sum, and convert back to string
        sum_value = int(n1) + int(n2)
        sum_string = str(sum_value)
        
        # Step 3: Create a new linked list representing the sum in reverse order
        return self.create_linked_list_from_string(sum_string)
    
    def reverse_and_convert_to_string(self, head):
        """
        Reverse a linked list and convert its values to a string.
        """
        # Reverse the linked list
        reversed_list = []
        cur = head
        while cur:
            reversed_list.append(str(cur.val))
            cur = cur.next
        
        # Convert reversed list to a string
        return ''.join(reversed_list[::-1])
    
    def create_linked_list_from_string(self, s):
        """
        Create a linked list from a string of digits in reverse order.
        """
        # Convert string to list of integers
        values = [int(char) for char in s[::-1]]
        
        # Create the linked list from the list of values
        dummy_head = ListNode()
        cur = dummy_head
        for value in values:
            cur.next = ListNode(value)
            cur = cur.next
        
        return dummy_head.next  # Return the head of the new linked list
