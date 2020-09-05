

import random

class Node:
    """ A single node of a singly linked list """

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


class List:
    """ A Linked List class with a single head node """

    def __init__(self, head=None):
        if head:
            self.head = head
        else:
            self.head = None

    def insert(self, data):
        """ insert to end of linked list """
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

def create_list():
    list = List(head=Node(random.randint(1, 100)))
    is_snake = random.randint(0, 1)  # Snake - 1, Snail - 0

    if is_snake :  # Snake list
        while random.randint(1, 100) != 1:  # Should create another node
            list.insert(data=random.randint(1, 100))
     
    else:  # Snail list
        start_of_loop = None
        curr_p = list.head

        while random.randint(1, 100) > 2:  # Should create another node
            list.insert(data=random.randint(1, 100))
            curr_p = curr_p.next  # Point to last node

            # Set start of loop if not set yet
            if random.randint(1, 1000) <= 15 and start_of_loop is None:  # Is this the start of loop
                start_of_loop = curr_p

        if start_of_loop is None:  # Set random start of loop if necessary
            start_of_loop = list.head
            temp_p = list.head

            while temp_p and start_of_loop == list.head:
                if random.randint(0, 1):
                    start_of_loop = temp_p
                temp_p = temp_p.next

        curr_p.next = start_of_loop  # Close loop
    return list

def SnackorSnail(list) :
  one_step_pointer = list.head
  two_step_pointer = list.head
  while(one_step_pointer and two_step_pointer and two_step_pointer.next): 
        one_step_pointer = one_step_pointer.next
        two_step_pointer = two_step_pointer.next.next
        if one_step_pointer == two_step_pointer: 
          return one_step_pointer
  return None    

def print_list(head, start_of_loop):
    size_of_list = 0
    if start_of_loop:
        print("SNAIL LIST:")
        current = head
        reached_loop = False
        size_of_loop = 0
        # Go through list until reaching start of loop for the second time
           # Go through list until reaching start of loop for the second time
        while not (current == start_of_loop and reached_loop):
            size_of_list += 1
            print(current.data)
            if current == start_of_loop:
                reached_loop = True
                print("Start of loop above")
            if reached_loop:
                size_of_loop += 1
            current = current.next
        print(current.data)  # Print start of loop again to close it
        print("The size of the loop is : {0}".format(size_of_loop))
    else:
        print("SNAKE LIST:")
        current = head
        while current:
            print(current.data)
            current = current.next
            size_of_list += 1
    print("The size of the list is : {0}".format(size_of_list))
  

if __name__ == '__main__':
    list = create_list()
    start_of_loop = SnackorSnail(list)
    print_list(list.head, start_of_loop)
