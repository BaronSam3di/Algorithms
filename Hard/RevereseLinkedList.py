"""
----- NAME: Reverse Linked List -----
----- Category: Linked Lists -----
----- Level : Hard -----
------ BRIEF ------
Write a function that takes in the head of a Singly Linked Lists such as 0 -> 1-> 2-> 3-> 4-> 5
and reverses the list in place (ie:, doesn't create a brand new list), 
and returns its new head ; eg 5 out of 5 -> 4 -> 3 -> 2 -> 1.

Each LinkedList node has an integer value as well as a 
next node pointing to the next node in the list or to None/null if it's the tail of the list.

You can assume that the input linked List will always have at ;wast pne node; in other words, the head will never be None / null.

------ Hints ------
- You can iterate through the Linked List from head to tail and reverse it in place along the way. 

- you need to manipulate three nodes at once at every step.

 - Imagine you have three variables pointing to three consecutive nodes in a Linked Lists. 
Start by setting the "next" property of the second node to the first node. Then, set the first variable to the second node, 
and set the second variable to the third node. Finally, set the third variable tp the second variable's "next" property) at this point ,
the second variable is the original third node). Repeat this process until you're at the tail of the linked List.

------ Complexity ------ 
Time: O() 
Space: O()

------ Approach ------
Ultimately, reverse the direction of the pointers.
Not many Algo's use threee pointers like thes. 
the ordering id important to not loose track of variables. 

"""

####################################################
## Time: O(n) - where n is the length of the Linked List
## Space: O(1) - because we are doing this in place
####################################################

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    
    # pointerOne is None because it needs to be one back from pointerTwo which needs to be the "current node in question" at any one time. 
    pointerOne, pointerTwo = None, head           

    while pointerTwo is not None:   
        pointerthree = pointerTwo.next            # declare pointerthree here because we will need this at the end
        pointerTwo.next = pointerOne              # this reverses the pointer to point back to the node behind it
        pointerOne = pointerTwo                   # this needs to happen once we have recorded pointerOne above
        pointerTwo = pointerthree                 # this needs to happen once we have recorded pointerTwo above
    return pointerOne                             # pointerTwo will be passed the head and pointerOne will be the new and final head pf the LinkedList