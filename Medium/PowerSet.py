"""
----- NAME: Powerset -----
# Has a recursive solution 
----- Category: Recursion -----
----- Level : Medium -----
------ BRIEF ------
Write a function that takes in an array of unique integers and returns its powerset.

The powereset P(X) of a set is the set of all subsets of X. 
Powerset: The set of all subsets of another set.
For example. the powerset of [1,2] is [[],[1],[2],[1,2]].

Note that the sets in the powerset do not need ot be in any particular order.


------ Hints ------


------ Complexity ------ 

------ Iterative Approach ------
Time: O(2^n * n) as every value of n, doubles the amount of subsets, but ehn we half that new amount. 
Space: O(2^n)

Simpler than the recursive, more intuitive and fewer lines of code. 

You take the input array.
Iterate through the numbers and at each number, then
Iterate through the subsets and create a new subset with the new number.
------ Recursive Formula ------
A bit tougher.
P([1,2,3,4,... x]) -> P([1,2,3,4,..., x -1]) + [x]



"""

####################################################
## Time: O(2^n * n) as every value of n, doubles the amount of subsets, but ehn we half that new amount. 
## Space: O(2^n)
####################################################

from typing import SupportsBytes


def powerset(array):
    subsets = [[]]     
	print("array",array)# decare the subsets array
    for element in array:               
        for i in range(len(subsets)):  # only generate subsets on the current elements we have
            currentSubset = subsets[i]
            print("subset: ",subsets)
            subsets.append(currentSubset + [element])
    return subsets

####################################################
## Time: O(2^n * n) as every value of n, doubles the amount of subsets, but ehn we half that new amount. 
## Space: O(2^n)
####################################################

def powerset(array, idx = None):
    # base case
    if idx is None:
        idx = len(array) - 1                        # set the index to the last element in the array. 
    if idx < 0:
        return [[]]     
    # recursive case 
    element = array[idx]
    subsets = powerset(array, idx - 1)              #
    for i in range(len(subsets)):
        currentSubset = subsets[i]
        subsets.append(currentSubset + [element])   # 
    return subsets