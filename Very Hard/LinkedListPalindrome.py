"""
----- NAME: Linked List Palindrome -----
# Has a recursive solution 
----- Category: Linked Lists -----
----- Level : Very HArd -----
------ BRIEF ------



Write a function that takes in the head of a Singly Linked List and returns at boolean representing whether the link list needs form a palindrome.
You function shouldn't make use of any auxillary data structure.

A palindrome is usually defined as a string that's written the same forwards and backwards.
For a link list notes to form a palindrome, their values must be the same when read from left to right and from right to left.

Note that single-the character strings are palindromes, which means the single-node links lists for palindromes.

Each Linked List node has an integer value as well as the next node pointing to the next node in the list or to none/null if it's the tail of the list.

You can assume that the input links list will always have at least one node; in other words, the head will never be none/null.

------ Hints ------

- Think about comparing two nodes at a time. To determine if the links lists nodes form a palindrome, which two nodes should we compare?
- Compare the first and last node the second and 2nd-to-last node, the third and 3rd-to-last-node, etc. How can we compare all of these nights recursively?

------ Complexity ------ 
Time: O() 
Space: O()

------ Recursive Approach ------

------ Iterative Approach ------

"""


####################################################
## Recursive approach, but not optimal 
## Time: O(n) - where n is the number of nodes in the linked 
## Space: O(n) - because of the recursive stack space 
####################################################

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def linkedListPalindrome(head):
    isPalindromeResults = isPalindrome(head, head)
    return isPalindromeResults.outerNodesAreEqual


def isPalindrome(leftNode, rightNode):
    # base case
    if rightNode is None:
        return LinkedListInfo(True,leftNode)


    recursiveCallResults = isPalindrome(leftNode,rightNode.next)
    leftNodeToCompare = recursiveCallResults.leftNodeToCompare
    outerNodesAreEqual = recursiveCallResults.outerNodesAreEqual

    recursiveIsEqual = outerNodesAreEqual and leftNodeToCompare.value == rightNode.value
    nextMatchingLeftNode = leftNodeToCompare.next

    return LinkedListInfo(recursiveIsEqual, nextMatchingLeftNode)


class LinkedListInfo:
    def __init__(self, outerNodesAreEqual, leftNodeToCompare):
        self.outerNodesAreEqual = outerNodesAreEqual
        self.leftNodeToCompare = leftNodeToCompare

####################################################
## Optimal iterative approach
## Time: O(n) - where n is 
## Space: O(n) - 
####################################################

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def linkedListPalindrome(head):
    slowNode = head
    fastNode = head
    while fastNode is not None and fastNode.next is not None:
        # when fast node is at the end of the list , slow node will be at the centre
        slowNode = slowNode.next
        fastNode = fastNode.next.next   # twice as fast

    reversedSecondhalfNode = reverseLinkedList(slowNode)
    firstHalfNode = head

    while reversedSecondhalfNode is not None:
        if reversedSecondhalfNode.value != firstHalfNode.value:
            return False
        reversedSecondhalfNode = reversedSecondhalfNode.next
        firstHalfNode = firstHalfNode.next 

    return True




def reverseLinkedList(head):
    # see other exercise file on this 
    previousNode, currentNode = None, head
    while currentNode is not None:
        nextNode = currentNode.next
        currentNode.next = previousNode
        previousNode = currentNode
        currentNode = nextNode
    return previousNode
    


