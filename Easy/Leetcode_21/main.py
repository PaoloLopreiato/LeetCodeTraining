class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
   
# Example usage:
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

def main():
    #merged_list = merge_linked_lists(list1, list2)
    #print_list(merged_list)
    mergedlist = mergeLists(list1,list2)
    print_linked_list(mergedlist)

#Correct
def mergeLists(list1,list2):
    #create a fake node
    dummy = ListNode()
    #fake node in list is our starter node
    tail = dummy
    #cicla fino a quando una delle 2 liste é vuota
    while list1 is not None and list2 is not None:
        #se il valore nella prima lista é minore significa che il nodo successivoi al dummy punta alla lista1
        if list1.val <= list2.val:
            tail.next = list1 #il puntatore punta alla lista1
            list1 = list1.next #la lista 1 punta allelemeto successivo e come se avessi fatto i++ in modo da paragonare lelemento successivo al prossimo loop altrimeti ripeto la stessa operazione all'infinito
        else:
            tail.next = list2
            list2 = list2.next
        #Ogni volta che faccio il check aggiorno il puntatore in tail
        tail = tail.next
    if list1 is not None:
        tail.next = list1
    if list2 is not None:
        tail.next = list2
    
    #returns not indicidual node but all nodes of dummy
    return dummy.next

def print_linked_list(mergedlist):
    while mergedlist is not None:
        if mergedlist.next is not None:
            print(f"{mergedlist.val} ->", end=' ')            
        else:
            print(mergedlist.val)
        mergedlist = mergedlist.next
        
if __name__ == "__main__":
    main()