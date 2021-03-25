"""
----- NAME: Merged Linked List-----
----- Category: Linked List ----- Includes Recursion
----- Level : Hard -----
------ BRIEF ------

Rights of function that takes in the head of two Singly Linked Lists that are in sorted order, respectively.
The function should merge the lists in place (i.e., it shouldn't create a brand-new list) and return the head of the merged list; 
the merged list should be in sorted order.

Each links list now it has an integer value as well as a "next" node pointing to the next "node" in the list or to None/null if 
it's the tail of the list.

You can assume that the input links list will always have at least one night; in other words, the None/null.

Sample input : 
headOne = 2 -> 6 -> 7 -> 8                  # The headnode with value 2
headTwo = 1 -> 3 -> 4 -> 5 -> 9 -> 10       # The headnode with value 1

Sample Output:
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10 
Notes :
Similar to reveresing a linked list.
------ Hints ------
- You can iterate through the link list from head to tail and merge them along the way by
 inserting notes from the second link list into the first link list.

- You'll need to manipulate three nodes at once every step.

- At every step, you'll need to have three variables (P1, P2, and P1prev) Pointing to the current node in the first link list (P1),
The current note in the second link list (P2), and the previous node in the first link list (P1prev). 
If the value of P1 is smaller than the value of P2, then you can just "move forward "in the first link list by moving P1 and P1prev forward by one position (P1prev Becomes P1 and P1 becomes P1.next).
If the value of P1 is greater than the value of P2, then you need to insert P2 before P1.
You'll have to first make P1 press point to P2, then make P2 points of P1, all the while not losing track of P2's "next" node, which you'll need to move to right after. 
You'll also have to handle edge cases when you're dealing with the head nodes or tail loads. 

------ Iterative Approach ------



------ Recursive Approach ------
rather than a while loop, we have a recursive function which we pass in P1, p2 , P2.next. 
Time: O() 
Space: O()


I need to go back ver the code walkthrough of this
"""

####################################################
## Iterative 
## Time: O(n + m) - where n and m are the lengths of the 2 linked lists. We iterate through each once.
## Space: O(1) - although we keep track of a few vars, they are small and mutation is happening in place so its constant time.
####################################################

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    p1 = headOne
    p1Prev = None
    p2 = headTwo
    while p1 is not None and p2 is not None:
        if p1.value < p2.value:
            p1Prev = p1
            p1 = p1.next
        else:
            if p1Prev is not None:
                p1Prev.next = p2
            p1Prev = p2
            p2 = p2.next
            p1Prev.next = p1
    if p1 is None:                                  # we have run out of p1 values. The p1 list has finished
        p1Prev .next = p2
    
    return headOne if headOne.value < headTwo.value else headTwo


####################################################
## Recursive 
## Time: O(n) - where n is 
## Space: O(n) - 
####################################################

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def mergeLinkedLists(headOne, headTwo):
    recursiveMerge(headOne, headTwo, None)
    return headOne if headOne.value < headTwo.value else headTwo           # As in the iterative approach 

def recursiveMerge(p1,p2, p1Prev):
    # base case 
    if p1 is None:
        p1Prev.next = p2
        return
    if p2 is None:
        return


    if p1.value < p2.value:
        recursiveMerge(p1.next, p2, p1)
    else:
        if p1Prev is not None:
            p1Prev.next = p2
        newP2 = p2.next
        p2.next = p1
        recursiveMerge(p1, newP2, p2)

