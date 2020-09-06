import random


# A single node of a singly linked list
class Node:
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

    def print_snake(self):
        """ print method for the snake list """

        print("SNAKE LIST:")

        current = self.head
        while current:
            print(current.data)
            current = current.next

    def print_snail(self, start_of_loop):
        """ print method for the snail list """

        print("SNAIL LIST:")
        current = self.head
        reached_loop = False

        # Go through list until reaching start of loop for the second time
        while not (current == start_of_loop and reached_loop):
            print(current.data)
            if current == start_of_loop:
                reached_loop = True
                print("Start of loop above")
            current = current.next

        print(current.data)  # Print start of loop again to close it


def create_list():
    list = List(head=Node(random.randint(1, 100)))
    is_snake = random.randint(0, 1)  # Snake - 1, Snail - 0

    if is_snake:  # Snake list
        while random.randint(1, 100) != 1:  # Should create another node
            list.insert(data=random.randint(1, 100))
        list.print_snake()

    else:  # Snail list
        start_of_loop = None
        curr_p = list.head

        # create until reaching start of loop
        while start_of_loop is None:
            list.insert(data=random.randint(1, 100))
            curr_p = curr_p.next

            # Set start of loop if not set yet
            if random.randint(1, 1000) <= 15 and start_of_loop is None:  # Is this the start of loop
                start_of_loop = curr_p

        # create until reaching last node
        while random.randint(1, 100) > 2:
            list.insert(data=random.randint(1, 100))
            curr_p = curr_p.next

        curr_p.next = start_of_loop  # Close loop
        list.print_snail(start_of_loop)


if __name__ == '__main__':
    create_list()
