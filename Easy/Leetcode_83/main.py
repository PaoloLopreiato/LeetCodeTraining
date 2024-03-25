class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)

def main():
    removed_sorted = remove_and_sort(head)
    print_linked_list(removed_sorted)


def remove_and_sort(head):
    current = head
    #Nested loop in the first i check current node is not none
    while current is not None:
        #if node exist i loop if the next node is not null(otherwisae i'm at the ed of the list)
        #and if my value is = to next value
        while current.next is not None and current.val == current.next.val:
            #if equal then i move the pointer from the next node to the next next node
            current.next = current.next.next
        #update current node to next node
        current = current.next
    #last update of current will briong current to none so i return head   
    return head
    
def print_linked_list(removed_sorted):
    while removed_sorted is not None:
        if removed_sorted.next is not None:
            print(f"{removed_sorted.val} ->", end=' ')            
        else:
            print(removed_sorted.val)
        removed_sorted = removed_sorted.next
            
if __name__ == "__main__":
    main()