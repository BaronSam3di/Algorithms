"""
----- NAME:Rearrange Linked List  -----
----- Category: Linked Lists   -----
----- Level : Very HArd -----
------ BRIEF ------

Write a function that take in the head if a Singly Linked List and an integer k , 
rearranges the list in place (i,e, doesn't create a brand new list ) around nodes with value k, and returns its new head.

Rearranging a Linked List around node with value k means moving all nodes with a value smaller than k before all nodes with value k, 
and moving all nodes with a value greater than k after all nodes with value k.

All moved nodes should maintain their original relative ordering if possible. 

Note that the linked list should be rearranged even it if doesn't have any nodes with value k.

Each LinkedList node has an integer value as well as a next node pointing to the next node in the list or to None/null if it's the tail of the list.

You can assume that the input Linked List will always have at least one node; in other words, he head will never be None/null.

head = 3 -> 0 -> 5 -> 2 -> 1 -> 4 # the head node with the value 3
k = 3

OP: 0 -> 2 -> 1 -> 3 -> 5 -> 4 # the new head node with value 0

Note that the nodes with values 0 ,2 , and 1 have maintained their original relative ordering,
and so have the nodes with values of 5 and 4 


------ Hints ------

1. Final link to list that you have to return essentially consists of three links lists attached to one another:
 - One with Notes his values are smaller than K
 - One with notes his values are equal to K
 - One with nature values are greater than K

2. Iterate through the links list once, build the three link list mentioned above as you go, and finally connect these three link list.

3. To build the three link list Mentioned above, you'll have to keep track of their heads and tales,
and update the appropriate link list tail with each note that you traverse as you iterate through the main link list.

4. Connecting the three link lists mentioned above won't be as simple as it sounds,
mainly because one or two of the linked lists might actually be empty,
depending on the various nodes values and the value of K.
------ Complexity ------ 
Time: O() 
Space: O()

------  Approach ------

make three linnked lists: >K , K and <K

We need to build all three linked lists in one go, not sequentially. 

"""

####################################################
## Time: O(n) - where n is the lentgth of the linked List
## Space: O(1) - 
####################################################

# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def rearrangeLinkedList(head, k):
    smallerListHead = None
    smallerListTail = None
    equalListHead = None
    equalListTail = None
    greaterListHead = None
    greaterListTail = None

    node = head
    while node is not None:         # filter out node values and then update each head or tail
        if node.value < k:
            smallerListHead, smallerListTail = growLinkedList(smallerListHead, smallerListTail , node)
        elif node.value > k:
            greaterListHead, greaterListTail = growLinkedList(greaterListHead, greaterListTail, node)
        else:
            equalListHead, equalListTail = growLinkedList(equalListHead, equalListTail, node)

        prevNode = node
        node = node.next
        prevNode.next = None

    # connect the smallerList with the equalList
    firstHead , firstTail = connectLinkedLists(smallerListHead,smallerListTail,equalListHead,equalListTail)

    # connect the new first list from above with with the greater than list
    finalHead , _ = connectLinkedLists(firstHead,firstTail, greaterListHead, greaterListTail)
    return finalHead

def growLinkedList(head, tail , node):
    newHead = head
    newTail = node                      # update the lists tail value to be the latest node added

    if newHead is None:                 # this means we are in a new list
        newHead = node
    if tail is not None:                # the new tail is the new node
        tail.next = node

    return (newHead, newTail)

def connectLinkedLists(headOne, tailOne, headTwo, tailTwo):
    # with this helper we need to consider edge cases such as no node values are smaller than k, so an empty 'smaller than list'
    # so we wouldn't None as a list head.
    newHead = headTwo if headOne is None else headOne
    newTail = tailOne if tailTwo is None else tailTwo

    if tailOne is not None:              # this does the connections
        tailOne.next = headTwo
    
    return (newHead, newTail)