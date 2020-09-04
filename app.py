from List import List
from Node import Node
import random

list = List()

opt=["snake", "snail"]
listType = random.choices(opt,cum_weights = [0.5,1.0])

if (listType == opt[0] or True): 
  nextNode = random.choices([None,random.randrange(50)],cum_weights = [0.01,1.0])
  while(nextNode[0] is not None) : 
    list.insert(nextNode[0])
    nextNode = random.choices([None,random.randrange(50)],cum_weights = [0.01,1.0])
else :
 while(Continue) :
  list.insert(random.randrange(50))
  Continue = random.choices([False,True],cum_weights = [0.15,1.0]) 
 while(not last) :
  last = random.choices([True,False],cum_weights = [0.15,1.0])

list.printList()
# SnackorSnail(L)

# def SnackorSnail(L):

