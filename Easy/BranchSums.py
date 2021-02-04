"""

------ BranchSums : Easy----- 
Time: O(n) because we have to do constant time operations as we traverses all nodes.
Space: = O(log n) Multiple recursive calls on the call stack at once.

------ BRIEF ------
Write a function that takes in a Binary tree and a list of its branch sums ordered from 
the leftmost branch sum to the rightmost branch sum.

A branch sum is the sum of all values in a Binary Tree branch.
A Binary Tree branch is a path of nodes in a tree that starts at the rootOfBst node 
and ends at any leaf node.f

Each BinaryTree Node has an integer value, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves. or None/null.


The best way to calculate the number of branch sums based on the BST, 
You will never have more than N branch sums as there are N nodes. IN a balance BST , almost half the nodes will be in the leaf nodes. 

Notes: https://math.stackexchange.com/questions/664608/number-of-nodes-in-binary-tree-given-number-of-leaves
"""

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# O(n) time | O(n) space
def branchSums(rootOfBst):
    branchSums = []                                               # 
    calculateBranchSums(rootOfBst, 0 , branchSums)
    return branchSums

def calculateBranchSums(node, runningSum, branchSums):            # Recursive function
    if node is None:                                              # check incase we are at a None/null value(leaf)
        return

    newRunningSum = runningSum + node.value                       # calculate the branch sum 
    if node.left is None and node.right is None:                  # are we at a leaf node...?
        branchSums.append(newRunningSum)                          # ..then append the branch sum to the sums
        return
    
    calculateBranchSums(node.left, newRunningSum, branchSums)     # recurse down to the left, passing the runningSum and the sums list
    calculateBranchSums(node.right, newRunningSum, branchSums)    # recurse down to the right, passing the runningSum and the sums list


