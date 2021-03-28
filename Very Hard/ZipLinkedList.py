"""
----- NAME: Zipped Linked List  -----
----- Category: Linked Lists  -----
----- Level : Very Hard -----
------ BRIEF ------

You given the heads of a singly linked list of arbitrary links K. 
Write of function that zips the link list in place i.e. doesn't create a brand-new list and returns its head.

A linked list is zipped if it's nodes are in the following order, where K is the length of the links list:

1st Node >> kth Node >> 1st Node >> (kth -1) Node >> 1st Node >> (kth -2) Node >> 1st Node >> (kth -3) Node >> ...

Each LinkedList node has an integer "value" as well as a "next" node pointing to the next node in the list or to none/null if it's the tail of the list.

You can assume that the input links list to always have at least one night; in other words, the heads will never be none/null.

Sample input : LinksList = 1 -> 2 -> 3 -> 4 -> 5 -> 6 // head node with value 1 
Sample output : 1 -> 6 -> 2 -> 5 -> 3 -> 4 // head node with value 1


------ Hints ------
- Imagine how you would solve this problem if you were given two distinct lists. For example, how would you zip up the list 1 -> 2 -> 3 with the list 4 -> 5 to get 1 -> 5 -> 2 -> 4 -> 3 ?

- One of the most straightforward ways to solve this problem is to split the original link list into two link lists and you reverse the second link list before interweaving it was the first one.
Ultimately, you want the first node, with the kth-node, then the 2nd node etc, so reversing the second link list before interweaving it with the first one makes things simple.

- After you split the linked list into to two halves and reverse the second half, you'll have something like 1 -> 2 - > 3 and 5 -> 4;
at this point, you can simply add the first node of the reversed second half into the first half between 1 and 2 as in 1 -> 5 -> 2.
Simply continue this process until you've inserted all of the notes from the reverse second half into the first.

------ Complexity ------ 
Time: O(n) -  
Space: O(1)

------ Approach ------
1. split LL - to find the middle use a "slow and fast " pointers.
2. Reverse LL2
3. Interweave LL and LL2

"""

####################################################
## Time: O(n) - where n is 
## Space: O(n) - 
####################################################

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def zipLinkedList(linkedList):
    # main zipping function
    if linkedList.next == None or linkedList.next.next == None:     # check if the list is of length 1 or 2 
        return linkedList                                           # return the supplied linked list as is

    firstHalfHead = linkedList
    secondHalfhead = splitLinkedList(linkedList)

    reversedSecondHalfHead = reverseLinkedList(secondHalfhead)

    return interweaveLinkedLists(firstHalfHead, reversedSecondHalfHead)



def splitLinkedList(linkedList):
    # this will find the middle of the list and return its second half
    slowIterator = linkedList
    fastIterator = linkedList
    while fastIterator is not None and fastIterator.next is not None:
        slowIterator = slowIterator.next
        fastIterator = fastIterator.next.next

    secondHalfhead = slowIterator.next
    slowIterator.next = None
    return secondHalfhead

def interweaveLinkedLists(linkedList1,linkedList2):

    linkedList1Iterator = linkedList1
    linkedList2Iterator = linkedList2

    while linkedList1Iterator is not None and linkedList2Iterator is not None:
        linkedList1IteratorNext = linkedList1Iterator.next                          # temp1 var
        linkedList2IteratorNext = linkedList2Iterator.next                          # temp1 var

        linkedList1Iterator.next = linkedList2Iterator
        linkedList2Iterator.next = linkedList1IteratorNext
		
        linkedList1Iterator = linkedList1IteratorNext
        linkedList2Iterator = linkedList2IteratorNext
    
    return linkedList1

def reverseLinkedList(linkedList):
    previousNode, currentNode = None, linkedList
    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode
    return previousNode 