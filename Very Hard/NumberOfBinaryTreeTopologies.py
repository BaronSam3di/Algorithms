"""
----- NAME: Number of Binary Tree Topologies  -----
----- Category: Recursion -----
----- Level : Very Hard -----
# Has a recursive solution 
------ BRIEF ------


------ Hints ------


------ Complexity ------ 
Time: O(n^2) 
Space: O(n) - storeing n total values in a cache

------ Recursive Approach ------
L = left
R = right

Slow version
for 

Famous formula "Catalan Number " Formula    >>>   2n! / n!( n+1)!


Memoise version
for L in range(o, n):
    R = n - 1 - L
    nL = f(L)
    nr = f(R)
    T += nL x nR
"""

####################################################
## Optimal version
## Time: O(n^2)  
## Space: O(n) - 
####################################################

def numberOfBinaryTreeTopologies(n, cache = {0 : 1}):
    
    # base case
    if n in cache:
        return cache[n]

    numberOfTreesTopologies = 0
    for leftTreeSize in range(n):               
        rightTreeSize = n - 1 - leftTreeSize                                    # - 1 for the root node
        numberOfLeftTrees = numberOfBinaryTreeTopologies(leftTreeSize,cache)
        numberOfrightTrees = numberOfBinaryTreeTopologies(rightTreeSize,cache)
        numberOfTreesTopologies += numberOfLeftTrees * numberOfrightTrees
    cache[n] = numberOfTreesTopologies
    return numberOfTreesTopologies

####################################################
## Optimal version
## Time: O(n^2)  
## Space: O(n) - 
####################################################

def numberOfBinaryTreeTopologies(n, cache = {0 : 1}):
    cache = [1]
    
    for m in range(1, n+1):
        numberOfTreesTopologies = 0
        for leftTreeSize in range(m):                                   # - 1 for the root node
            rightTreeSize = m - 1 - leftTreeSize
            numberOfLeftTrees = cache[leftTreeSize]
            numberOfRightTrees = cache[rightTreeSize]
            numberOfTreesTopologies += numberOfLeftTrees * numberOfRightTrees
    return numberOfTreesTopologies

####################################################
## slow recursive Catalan version
## Time: O(n) - where n is 
## Space: O(n) - 
####################################################

def numberOfBinaryTreeTopologies(n):
    
    # base case
    if n == 0:
        return 1

    numberOfTreesTopologies = 0
    for leftTreeSize in range(n):               
        rightTreeSize = n - 1 - leftTreeSize                                    # - 1 for the root node
        numberOfLeftTrees = numberOfBinaryTreeTopologies(leftTreeSize)
        numberOfrightTrees = numberOfBinaryTreeTopologies(rightTreeSize)
        numberOfTreesTopologies += numberOfLeftTrees * numberOfrightTrees
    return numberOfTreesTopologies