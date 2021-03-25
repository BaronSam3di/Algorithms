"""
----- NAME: Find Loop  -----
----- Category: Linked Lists -----
----- Level : Hard -----
------ BRIEF ------

Write a function that takes in the head of a Singly Linked List that contains a loop,
(in other words, the list's tail node points to some node in the list instead of None/ null).
The function should return the node (the actual node not just its value) from which the loop originates in constant space.

Each LinkedList node has an integer value as well as a next node pointing to the next node in the list.


------ Hints ------


------ Complexity ------ 
Time: O() 
Space: O()

------ Approach ------

- Use 2 pointers, 
    F(first) - this will move ONE space at a time 
    S(second)- this will move TWO spaces at a time 

    ONce the pointers meet again , then we have done one loop AND more importantly

    F has travelled X, and S has travelled 2X
    IF we turn these into variables, F has rtavelled ot every node on the way and 
    



"""

####################################################
## Time: O(n) - where n is 
## Space: O(1) - because this is done in place
####################################################

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    first = head.next
    second = head.next.next
    while first != second:            # unil they become the same node
        first = first.next
        second = second.next.next
    
    first = head                             # reset to the head

    while first != second:            # now, when they become the same they are at the loop start point
        first = first.next            
        second = second.next
    return first                      # this must be the start of the loop