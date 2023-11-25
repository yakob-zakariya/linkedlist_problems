""""
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

#solution 
since our head may also be deleted we need a dummy node at the begning and using two pointer actually three pointers prev,current,after to delete the node 
the trick here is that we do not change the prev pointer when the delete the value(node)
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
    
    def remove_element(self,value):
        dummy = ListNode(value=0,next=self.head)
        
        prev = dummy
        cur = self.head
        while cur:
            after = cur.next        
            if cur.value == value:
                prev.next = after
            else:
                prev = cur
            cur = after
        self.head = dummy.next

my_linked_list = LinkedList(1)
my_linked_list = LinkedList(1)
my_linked_list = LinkedList(1)



my_linked_list.remove_element(1)
my_linked_list.print_list()

print(my_linked_list.head)