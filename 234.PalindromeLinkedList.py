""""
Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.

#solution
1.to solve in O(n) we can use stack after appending all values to stack then we compare to ourlinked values using poping from the stack

2. but if we want with O(1) space 
we can reverse the second half of the linked list and comparing the values with first half
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
    
    def reverse_list(self):
        cur = self.head
        prev = None
        while cur:
            after = cur.next
            cur.next = prev
            prev = cur
            cur = after
        self.head = prev
        
    
    def middle_node(self):
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(slow.value)
    
    def isPalindrome(self):
        
        #getting the middle node
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
         # reversing the second half of the linkedlist
        second = slow
        prev = None
        while second:
            after = second.next
            second.next = prev
            prev = second
            second = after
        
        second = prev
        first = self.head
        while second:
            if first.value != second.value:
                return False
            second = second.next
            first = first.next
        return True

        

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(2)
my_linked_list.append(1)
# my_linked_list.append(2)

print(my_linked_list.isPalindrome())
