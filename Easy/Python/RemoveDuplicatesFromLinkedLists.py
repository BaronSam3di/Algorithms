"""
----- Remove Duplicates from Linked List : Easy -----
------ BRIEF ------
You're given the head of a Singly Linked List whose nodes are in sotred order with respect to their values. 
Write a function that returns a modified version of the Linked List tha doesn't containt any nodes with duplicate values.
The Linked List should be modified in place (i,e; you shouldn't create a brand newList) and the modified Linked List should still have its nodes sorted with respect to their values.

Each LinekdList node has an integer value as well as a next node pointing to the next node in the list or to None/Null only if its the tail of the list.  

------ Hints ------

- The Brute-force approach to this problem is to use a hash table or a set to keep all node value that exist while 
traversing the linked list and to simply remove nodes that have a value that already exists.
 This approach works, but can you solve this problem with using an auxillary data structure?

- What does the fact tha the nodes are sorted tell you about the location of all duplicate nodes? 
How can you use this fact to solve this problem with constan space? 

- Since the linked lists nodes ae sorted , you can lop through them and , at each iteration, simply remove all successive nodes that have the same value as the cirrent node. 
FOr each node, change its next pointer to the next node in the linked list tat has a different value This will remove all duplicate-value.
------ Complexity ------ 
Time O(n)
Space O(1)
------  Approach ------
currentNode = head
temp = currentNode.next.next
currentNode.next = temp

"""

# This is an input class.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    currentNode = linkedList                            
    while currentNode is not None:                                                  # end of the list
        nextDistinctNode = currentNode.next 
        while nextDistinctNode is not None and nextDistinctNode.value == currentNode.value: 
            ''' if the next node and the current node have the same value we are not intersted in that '''
            nextDistinctNode = nextDistinctNode.next                                # and we shall move on
        
        currentNode.next = nextDistinctNode                                         # Now we set out new current node
        currentNode = nextDistinctNode
    
    return linkedList                                                               # having swapped all the next values t obe unique we return our LinkedList