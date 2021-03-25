"""
----- Node Depths : Easy -----
# Has a recursive solution 
------ BRIEF ------

The distance between a node in Binary Tree and the tree's root is called the nodes's depth.

Write a function that takes in a Binary Tree and returns the sum of its nodes depths.

Each BinaryTree node has an integer value, a left child node and a right child node. 
Children nodes can either be BinaryTree nodes themselves or None/null.

------ Hints ------
To Solve this  you will need to figure our how to compute the depth of any give node; once you know how to do that, 
you can compute all of the depths and add them up to obtain the desired output. 

To compute the depth of a given node, you need information about its position in the tree, Can you pass this information down from the node's parent?

The depth of any node in the tree is equal to the depth of its parent node plus 1. By starting at the root node whose depth is 0, you can pass down to 
every node in the tree its respective depth, and you can implement the algorithm that does this 
and that sums up all of the depths either recursively or iteratively.

------ Complexity ------ 
Average case when the tree is balanced:
- Time O(n) where n == nodes 
- Space O(h) where h == height

------ Recursive Formula ------
Recursive formula: f(n,d) = d + f(left, d+1) + f(right, d+1) 
Base case : Hitting a null/None value

------ Iterative Approach ------

"""

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


## Iterative approach
def nodeDepths(root):
    sumOfDepths = 0
    stack = [{"node": root, "depth": 0}]                    # Needed to store the nodes and the depth
    while len(stack) > 0:
        nodeInfo = stack.pop()
        node,depth = nodeInfo["node"] , nodeInfo["depth"]               
        if node is None:
            continue
        sumOfDepths += depth
        stack.append({"node": node.left, "depth": depth + 1})
        stack.append({"node": node.right, "depth": depth + 1})
        print(stack)
    return sumOfDepths

## Recursive approach
def nodeDepths(root, depth = 0):  # here we are useing an optional parameter of depth, initialised to zero.
    # Base case 
    if root is None:
        return 0
    # Recursive case         
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)

