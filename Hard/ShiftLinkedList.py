"""
----- NAME: Shift Linked List  -----
----- Category: Linked List -----
----- Level : Hard -----

------ BRIEF ------
Write a function that takes in the head of a singly Linked List and an integer K,
shift the list in place (i.e., doesn't create a brand-new list) by K positions, and returns its new head.

Shifting links list means moving its needs forward or backward and wrapping them around the list where appropriate. 
For example, shifting a link to list forward by one position would make its tail become the new head of the links list.

Where is the nodes and moved forwards or backwards is determined by whether K is positive or negative.

Each Linked List node has an integer values as well as a next need pointing to the next night in the list or to None/null if it's the tail of the list.

You can assume that the input links list will always have at least one node; in other words, the head will never be None/null.

Example
k = 2
Input list : 0 -> 1 -> 2 -> 3 -> 4 -> 5  
Output list : 4 -> 5 -> 0 -> 1 -> 2 -> 3  

------ Hints ------

- Putting aside the cases where K is a negative integer, where K is zero, 
or where K is larger than the length of the link list; what does shifting the link list by K positions entail exactly?

- Putting aside the case is mentioned in the hint above, shifting the links list by K positions means moving the last K nodes in the link list to the front of the link list.
 What nodes in the link list will you actually need to mutate?

- There are four nodes that really matter in this entire process:
    - The original tale of the link list, which will point to the original head of the link list
    - The original heads of the link list which will be pointed to buy the original tire was a link placed
    - The new tail of the link list
    - The new head of the link list
    Note that the new head is the note that the new tail points to in the original, upshifted linked list

- You can find the original tale of the linked list by simply traversing the link list, starting at the original head of the link list that you are given. 
You can find the new tale of the link list by moving K positions from the original tale if K is positive (which means moving to the (lengthoflist – K)th position in the list, 
and you can easily count the length of the list as you traverse it to fin its original tail). you can access the new head of the linked list once you've found its new tail, 
since it's the new tail's original next node. How will you handle the trickier values of k?


Position of New Tail  = Length - k

Edge cases : 
- k == 0 
- k is longer than the list , eg  30. Answer: ListLength mod k 

- k is a negative number
"""

####################################################
## Time: O(n) - where n is the length of the linked
## Space: O(1) - no extra data needed
####################################################

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
    listLength = 1              
    listTail = head
    while listTail.next is not None:                                # figure out the length of the Linked list 
        listTail = listTail.next
        listLength +=1

    # calculate the offset we will be either from the end or the begining - some languages don't like mod on -numbers
    offset = abs(k) % listLength                                    
    
    if offset == 0:                                                 # edge case 
        return head                                                 # no mutations needed    
    newTailPosition = listLength - offset if k > 0 else offset      # turnery condition
    newTail = head

    for i in range(1, newTailPosition):                             # just need to go up to the new tail postion 
        newTail = newTail.next
    
    newHead = newTail.next                                          # get ref to new head
    newTail.next = None                                             # make the tail point to None
    listTail.next = head                                            # original tail is looped to the begining of the list
    return newHead
