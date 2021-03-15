"""
----- NAME: Binary Search Tree Construction -----
----- Category: Binary Search Trees -----
----- Level : Medium -----
------ BRIEF ------

Write a BST class for a Binary Search Tree. The class should support:
- inserting values with the insert method.
- removing values with the remove method; those method should only remove the first instance of a given value. 
- searching for values with the contains method.

Note that you can't remove values from a single-node tree. 
In other words, calling the remove method on a single-node tree should simply not do anything.

Each BST node has an integer value, a left child node and a right child node. 
A node is said to be a valid BST node if and only of it satisfies the BST property :
- A node's value is strictly greater than their values of every node to its left;
- A node's value is less than or equal to the values of every child node to its right
- A node's children are either valid BST nodes themselves or None/null.

Main methods of a BST: insertion, deletion, searching.
Insertion: IS this value greater 

------ Hints ------
- As you try to insert, find, or remove a value into, in , or from a BST, you will have to traverse the tree's nodes. 
The BST property allows you to eliminate half of the remainign tree at each node that you traverses: if the target value is strictly smaller than a node's value, 
then it must be (or can only be) located to the left of the node, otherwise it must be (or can only be) to the right of that node.

- Traverse the BST all the while applying the logic described in Hint#1. For insertion, add the target value to the BST once you reach a leaf (None/ null) node. 
For searching, if you reach a leaf node without having found the target value that means the value isn't in the BST.

For removal, consider the various cases that you might encounter: 
- the node you need to remove might have two children nodes, one , or none;
- it might also be the root node; 
make sure to account for all of the cases.


------ Complexity ------ 


------ Recursive Formula ------

------ Iterative Approach ------

"""

####################################################
# Recursively
## Average Case: Time and Space: O(log(n)) - log of n because we keep eliminateing half of the tree
## worst Case: Time and Space: O(n) - imagine a single line tree where we have to traverse every node
# Iteratively
## Average Case: Time O(log(n)) and Space: O(1) - log of n because we keep eliminateing half of the tree
## worst Case: Time O(n) and Space: O(1) - imagine a single line tree where we have to traverse every node
####################################################


# iterative 
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average: O(log(n)) time | O(1) space
    # Worst; O(n) time | O(1) space
    def insert(self, value):
        # Write your code here.
        currentNode = self                              # allows us to keep track
        while True:                                     # until we use a break statement    
            if value < currentNode.value:               # we then want to explore the left 
                if currentNode.left is None:            # are we at the end of a branch?
                    currentNode.left = BST(value)       # then make the following node a new BST with out value    
                    break
                else:
                    currentNode = currentNode.left
            else:                                       # we then want to explore the right
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self                                     # this allows us to chain the calls to insert

    # Average: O(log(n)) time | O(1) space
    # Worst; O(n) time | O(1) space
    def contains(self, value):
        currentNode = self
        while currentNode is not None: 
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True                            # if we get to here then the value is in the tree 
        return False
        
    # Average: O(log(n)) time | O(1) space
    # Worst; O(n) time | O(1) space
    def remove(self, value, parentNode = None):
        currentNode = self
        while currentNode is not None:
            # bookeeping section
            if value < currentNode.value:
                parentNode = currentNode                    # to keep track of the current node
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode                   
                currentNode = currentNode.right
            else:
                # Here we go! we have found our node and we have two child nodes present
                if currentNode.left is not None and currentNode.right is not None:
       class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Average: O(log(n)) time | O(1) space
    # Worst; O(n) time | O(1) space
    def insert(self, value):
        # Write your code here.
        currentNode = self                              # allows us to keep track
        while True:                                     # until we use a break statement    
            if value < currentNode.value:               # we then want to explore the left 
                if currentNode.left is None:            # are we at the end of a branch?
                    currentNode.left = BST(value)       # then make the following node a new BST with out value    
                    break
                else:
                    currentNode = currentNode.left
            else:                                       # we then want to explore the right
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self                                     # this allows us to chain the calls to insert

    # Average: O(log(n)) time | O(1) space
    # Worst; O(n) time | O(1) space
    def contains(self, value):
        currentNode = self
        while currentNode is not None: 
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True                            # if we get to here then the value is in the tree 
        return False
        
    # Average: O(log(n)) time | O(1) space
    # Worst; O(n) time | O(1) space
    def remove(self, value, parentNode = None):
        currentNode = self
        while currentNode is not None:
            # bookeeping section
            if value < currentNode.value:
                parentNode = currentNode                    # to keep track of the current node
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode                   
                currentNode = currentNode.right
            else:
                # Here we go! we have found our node and we have two child nodes present
                if currentNode.left is not None and currentNode.right is not None:
                    currentNode.value = currentNode.right.getMinValue()         # we swap the current node with the Minimum value
                    currentNode.right.remove(currentNode.value, currentNode)
                elif parentNode is None:                                        # we are at the root node , because there is no parent
                    # we don't have two child nodes present, so two subcases: root node or has parent node 
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left        # overwrite this last so we don't overwrite it before we stp needing it
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right     # for the same reason as above
                    else:
                        currentNode.value = None                        # Banal edge case to delete the root node 
						pass		# this is a single node tree; do nothing
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                break
        return self

    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value             currentNode.value = currentNode.right.getMinValue()         # we swap the current node with the Minimum value
                    currentNode.right.remove(currentNode.value, currentNode)
                elif parentNode is None:                                        # we are at the root node , because there is no parent
                    # we don't have two child nodes present, so two subcases: root node or has parent node 
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left        # overwrite this last so we don't overwrite it before we stp needing it
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = currentNode.right.right     # for the same reason as above
                    else:
                        currentNode.value = None                        # Banal edge case to delete the root node 
						pass		# this is a single node tree; do nothing
                elif parentNode.left == currentNode:
                    parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right
                elif parentNode.right == currentNode:
                    parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right
                break
        return self

    def getMinValue(self):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value