# מיקי מאירסון 207349010
# נעם תשובה 207576109

# This code uses the Floyd's Cycle detection ("Hare and Tortoise") algorithm -
# https://en.wikipedia.org/wiki/Cycle_detection

import random


class Node:
    """ A single node of a singly linked list """

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


class List:
    """ A Linked List class with a single head node """

    def __init__(self, head=None):
        self.head = head

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
    is_snake = random.randint(0, 1)  # Snake - 1, Snail - 0

    if is_snake:  # Snake list   
        list = List()
        while random.randint(1, 100) != 1:  # Should create another node
            list.insert(data=random.randint(1, 100))

    else:  # Snail list
        list = List(Node(random.randint(1, 100)))
        start_of_loop = None
        curr_p = list.head

        # create until reaching start of loop
        while start_of_loop is None:

            # Set start of loop if not set yet
            if random.randint(1, 1000) <= 15 and start_of_loop is None:
                start_of_loop = curr_p
            else:
                list.insert(random.randint(1, 100))
                curr_p = curr_p.next

        # create until reaching last node
        while random.randint(1, 100) > 2:
            list.insert(random.randint(1, 100))
            curr_p = curr_p.next

        curr_p.next = start_of_loop  # Close loop
    return list


def snake_or_snail(list):
    meet = False
    one_step = list.head
    two_step = list.head
    while one_step and two_step and two_step.next:
        if not meet:  # Set first meeting - different pace
            one_step = one_step.next
            two_step = two_step.next.next
            if one_step == two_step:
                one_step = list.head
                meet = True
        else:  # Set second meeting - same pace
            one_step = one_step.next
            two_step = two_step.next
            if one_step == two_step:
                return one_step
    return None


def print_list(head, start_of_loop):
    list_size = 0
    list_str = ''
    if start_of_loop:
        print("SNAIL LIST:")
        current = head
        reached_loop = False
        loop_size = 0

        # Go through list until reaching start of loop for the second time
        while not (current == start_of_loop and reached_loop):
            list_size += 1

            # Print start of loop arrow
            if current == start_of_loop:
                reached_loop = True
                list_str = list_str[:-1]
                list_str += '↱'

            list_str += str(current.data) + '→'

            # Print end of loop arrow
            if current.next == start_of_loop and reached_loop:
                list_str = list_str[:-1]
                list_str += '↲'

            if reached_loop:
                loop_size += 1

            current = current.next

        print("Loop size: {0}".format(loop_size))
    else:
        print("SNAKE LIST:")
        current = head
        while current:
            list_size += 1
            list_str += str(current.data) + '→'
            current = current.next
        list_str += 'null'
    print("List size : {0}".format(list_size))
    print(list_str)


if __name__ == '__main__':
    list = create_list()
    start_of_loop = snake_or_snail(list)
    print_list(list.head, start_of_loop)
