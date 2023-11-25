""""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 #solution 
 as we see the pattern the problem is to take alterante node from the first and then last then frist one from  the fist and first last from the last and so on
 so i first divide the linked list in to two the first half and second half.
 1 fist find the node before middle using slow and fast pointer but fast will start from the head.next
 2.then reverseing the second half and 
 3 then taking alternate value from the two lists 
"""

class ListNode():
    def __init__(self,value,next=None):
        self.value = value
        self.next = next
        
class LinkedList():
    def __init__(self,value):
        new_node = ListNode(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def append(self,value):
        new_node = ListNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next
    
    def reorder_list(self):
        
        #first lets find the node the node before the middle node to find the second half of the linked list using slow and fast pointers
        slow = self.head
        fast = slow.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        
        prev = None
        while second:
            after = second.next
            second.next = prev
            prev = second
            second = after
        
        first = self.head
        second = prev
        
     
        while second:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2
    
    def remove_duplicate(self):
        temp1 = self.head
        
        while temp1 and temp1.next:
            temp2 = temp1.next
            while temp2 and temp1.value == temp2.value:
                temp2 = temp2.next
        
            temp1.next = temp2
            temp1 = temp1.next
        



my_linked_list = LinkedList(1)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(2)
my_linked_list.append(3)



my_linked_list.remove_duplicate()

print('*****')

# my_linked_list.print_list()


