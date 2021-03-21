"""
----- NAME: Sum of Linked List -----
----- Category: Linked Lists -----
----- Level : Medium -----
------ BRIEF ------
You're given two Linked lists of potentially unequal length. Each link list represents a non-negative integer,
where each node in the Linkedlist is a digit of the integer, and the first night in each Linkedlist always represents the least significant digit of the integer.
Write a function returns the head of the new links list that represents some of the integers represented by the two implants list. 

Each Linkedlist node has an integer value as well as the "next" node pointing to the next node in the list or to none/null if it's the tail of the list. 
The value of each Linkedlist node is always in the range 0–9.

Note: Your function must create and return a new LinkedList, and you're not allowed to modify either of the input lists.

------ Hints ------
- If you can determine the integers that each individual links list represents, 
then all you need to do is add these integers and create a new link list that represents the sums value.

- If you go with the approach mentioned in the above, you need to break down some of the tooling lists numbers into its individual digits. 
Once you know these digits you can create the new link list using them this approach is fine,
 but you can solve this problem more elegantly, with a single iteration through the list.

 - It is necessary to know the entire number is represented by both Linkedlists in order to calculate their sum? 
 I think back to your elementary-school maths class; how did you add two numbers together?

- Since each Linkedlists digits are ordered from the significant digit to most significant digit, 
you can simply look through both Linkedlists, consider digits with the same significance, 
and add these digits together while keeping track of any carry that comes out of the addition.
At each iteration, when you add the two Linkedlist digits, also had to carry from the previous iteration.
Create a new link list night at the store is the calculated value, and that that's your new little list. 
Keep iterating until you reach the end of my clinic list and have no remaining carry.
------ Complexity ------ 


------ Approach ------

- Create dummy pointer that lets us keep track of the head of the OP linked list.
- for each number calculate 
value = (nums ) % 10 
carry = (nums ) // 10 

"""

####################################################
## Time & Space: O(max(n,m)) = MAximum of the length of the longest LinkedList
####################################################


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    newLinkedListHeadPointer = LinkedList(0)                        # dummy that allows to access the head of the pointer
    currentNode = newLinkedListHeadPointer                          # 
    carry = 0

    nodeOne = linkedListOne
    nodeTwo = linkedListTwo

    while nodeOne is not None or nodeTwo is not None or carry != 0:
        valueOne = nodeOne.value if nodeOne is not None else 0      # makes sure we have a node to get a value from
        valueTwo = nodeTwo.value if nodeTwo is not None else 0
        sumOfValues = valueOne + valueTwo + carry                   # adds the value associated with the linked list node + carry

        newValue = sumOfValues % 10                                 # To make sure we handle the carry
        newNode = LinkedList(newValue)                              # make the new value for the new node and
        currentNode.next = newNode                                  # updates the current Node's next to be new Node
        currentNode = newNode               

        carry = sumOfValues // 10                           
        nodeOne = nodeOne.next if nodeOne is not None else None     # next node else set it to None so we don't error
        nodeTwo = nodeTwo.next if nodeTwo is not None else None

    return newLinkedListHeadPointer.next                            # Return next as its after the first Dummy node