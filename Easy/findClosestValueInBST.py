"""
------Find Closet Value in BST : Easy----- 
------ BRIEF ------

Write a function that takes ina Binary Search Tree (BST) 
and a single target integer value and returns the closest value to tha target value containted in the BST.

Each BST node has an integer value, a left child node and a right child node. A node is said to be a valid BST if and only if
it satisfies the BST property: 
- its value is strictly greater than the values of every node to its left
- its value is less than or equal to the value of every node to its right
- its children node are either valid BST nodes themselves or Non / null. 

------ Solution ------
First we should initialise a "Closest value" which will hold the best candiadate. 
We could initialise this to an arbitrary value of 0. 

We will calculate the absolute value of the difference between our Target Value and the current value we are at.

Time: O(log(n)) on average because we eliminate half the tree on every pass. In the worst case it has the potential to get to O(n) because we have to pass every node.
Space: If we solve this recursively, it will be the same as the time complexity, Avg O(log(n)), worst O(n).

IIteratively solving this would reduce the space complexity 0(1) because we wont be storeing much.
We will need ot write a helper method to keep track of the closests value so far. 
"""

## --- recursive approach ----
## Average: O(log(n)) time | O(log(n)) space
## Worst: O(n) time | O(n) space
def findCLosestValueInBST(tree,target):
    return findClosestValueInBSTHelper(tree, target, tree.value)


def findClosestValueInBSTHelper(tree, target, closest):
    """ Base case: when we reach the bottom of the node ( eg: null or none')"""
    if tree is None:
        return closest
    if abs(target - closest) > abs (target - tree.value):
        closest = tree.value
    """ Recursive case: Compare node value and decide which sub tree we are going ot explore"""
    if target < tree.value:
        return findClosestValueInBSTHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBSTHelper(tree.right, target, closest)
    """ Last case: we have found the closest value """
    else :
        return closest



## ---- Non-recursive approach ----
## Average: O(log(n)) time | O(1) space
## Worst: O(n) time | O(1) space
def findCLosestValueInBST(tree,target):
    return findClosestValueInBSTHelper(tree, target, tree.value)


def findClosestValueInBSTHelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs (target - currentNode.value):
            closest = currentNode.value
        """ Main case: Compare node value and decide which sub tree we are going ot explore"""
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        """ Last case: we have found the closest value """
        else:
            break
    return closest