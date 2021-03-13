"""
----- NAME: Permutations -----
----- Category: Recursion  -----
----- Level: Medium  -----

------ BRIEF ------
Write a function that takes in an array of unique integers and returns an array of all permutations of those integers in no particular order. 
If the input array is empty, the function should return an empty array.

------ Hints ------


------ Complexity ------ 


------ Approach ------

1st approach : Create a helper which will take 2 things: array of number, perm we are currently building  and the entire permutations we have made.
If we run out of numbers in the list of numbers, we have finished the permutations - The base case.

2nd approach : " Do we need to create all these new arrays every time?" We will build the permutations for the array, 
in the array; take a snapshot and then continue. Useing pointers. 
Helper will take as argumants: index, array, and permutations. IF the index is the last position, append the permutations. 
"""

####################################################
## 1st Solution : Upper Bound: O(n^2*n!) time | O(n*n!) space
####################################################


def getPermutations(array):
    permutations = []                                                    # result permutations
    permutationsHelper(array, [], permutations)
    return permutations



def permutationsHelper(array, currentPermutation, permutations):
    # base case
    if not len(array) and len(currentPermutation):                      # is the array empty and len of the currentPerm has data. We don't want to append empty arrays
        permutations.append(currentPermutation)

    else:
        for i in range(len(array)):
            newArray = array[:i] + array[i + 1:]                         # generate new array of remaining numbers. Slice up to i, plus the inputArray of everything after i + 1
            newPermutation = currentPermutation + [array[i]]            # Create a new permutation adding the element index i
            permutationsHelper(newArray, newPermutation, permutations)

####################################################
## 2nd (Best) Solution: Roughly: O(n*n!) time | O(n*n!) space
####################################################

def getPermutations(array):
    permutations = []                                                    # result permutations
    permutationsHelper( 0, array, permutations)                              # takes in the current index of the current peermutation we are building
    return permutations

def permutationsHelper(i, array, permutations):
    if i == len(array) -1:                                               # are we at the end of hte array
        permutations.append(array[:])
    else:
        for j in range(i, len(array)):
            swap(array, i , j)
            permutationsHelper(i + 1, array, permutations)                # pass in the next number 
            swap(array, i , j)                                            # swap back to get back to the original position

def swap(array, i , j):
    array[i] , array[j] = array[j] , array[i]                   