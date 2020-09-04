from Node import Node
# A Linked List class with a single head node
class List:
  def __init__(self):  
    self.head = None
  
  # insertion method for the linked list
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  
  # print method for the linked list
  def printList(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next
