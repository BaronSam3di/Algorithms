"""
----- Name: Invert Binary Tree -----
# Has a recursive solution 
----- Category: Binary Trees -----
----- Level : Medium -----

------ BRIEF ------
Write a function that takes in a Binary Tree and invers it, In other words, 
the function should swap every left node in the tree for its corresponding right node.

Each BinaryTree node has an integer value, a left child node, and a right child node. 
Children node can either be BinaryTree nodes themselves or None / null.


Inverting really means swapping horizontally. 

------ Hints ------


------ Complexity ------ 

------ Iterative Approach ------
Time: O(n) - where n is the number of nodes in the tree
Space: O(n) - 
Similar with Breadth first search.

We need to initialise a queue. 
Swap the children of each node. 
Swap None nodes juts to be sure no? 

------ Recursive Formula ------
Time: O(n) - where n is the number of nodes in the tree
Space: O(d) - where d is the depth/height of the tree aka O(log(n))

Base case is are we at a null



"""

####################################################
## Iterative approach - Space & Time: O(n)
####################################################
def invertBinaryTree(tree):
    queue = [tree]
    while len(queue):                       # while the queue has length
        current = queue.pop(0)              # get the front value of the queue
        if current is None:                 # nothing to swap
            continue
        swapLeftAndRight(current)
        queue.append(current.left)
        queue.append(current.right)

def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


####################################################
## Recursive approach 
####################################################
def invertBinaryTree(tree):
    #base case
    if tree is None:
        return

    # main case 
    swapLeftAndRight(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)

    # helper function
def swapLeftAndRight(tree):
    tree.left, tree.right = tree.right, tree.left

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None