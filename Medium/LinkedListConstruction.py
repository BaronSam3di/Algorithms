"""
----- NAME:  -----
----- Category:  -----
----- Level :  -----
------ BRIEF ------
Write a DoublylinkedList class that has a head and a tail, both of  which point either to 
a link list Node or None/null. The class should support:

- Setting the head and tail of the links.
- Inserting nodes before and after of the nodes as well as at given positions (the position of the head node is 1)
- Removing given nodes and removing nodes with given values.
- Searching for nodes with given values.

Note that the < MEthods> Methods all taking actual nodes as input parameters –– not 
integers (except for insert that position, which also takes in an insecure representing the position); 
this means that you don't need to create any new nodes in these methods.

The input nodes can be either standalone nodes or nodes that are already in the link list.
If they're nodes that are already in the link list, the methods will effectively be moving the notes within the link list.



You won't be told if the input notes are already in the link list, so your code will have to defensively handle this scenario.

If you're doing this problem in a non-typed language like passion or JavaScript, you may want to look at the 
various function signatures in a type language like Java or typescript to get a better idea what each input parameters is.

Each node has an integer value as well as a Previous node and next node, both of which can point to either another night or None/null.


------ Notes ------

It's important to be careful when updating the pointers of nodes in the link list. 
You should update the previous nodes next pointer before you disconnect the current node from the previous node.
If we are talking about node 3, we would make sure that nodes 2 qnd 4 point ot their correct next and previous 
before we set 2 and 4 to null as the prev and next of 3. 



------ Hints ------


------ Complexity ------ 

"""

####################################################
##
####################################################


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # O(1) Time | O(1) space
    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)
    
    # O(1) Time | O(1) space
    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    # O(1) Time | O(1) space
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev                       # needs setting before it is overwrittern
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    # O(1) Time | O(1) space
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node                       # needs setting before it is overwrittern
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert
    
    # O(p) Time | O(1) space - where p is the position value
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)
    
    # O(n) Time | O(1) space
    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)
 
    
    # O(1) Time | O(1) space
    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removeNodeBindings(node)
        
    # O(n) Time | O(1) space
    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None

    # helper method
    def removeNodeBindings(self, node):
        # the order of these function is important
        if node.prev is not None:
            # Needs to happen first to update the previous nodes next before we loose node.prev
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None