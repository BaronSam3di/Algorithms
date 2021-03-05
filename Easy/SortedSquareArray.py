"""
----- Sorted Squared Array :  -----
------ BRIEF ------
Write a function that takes in a non empty array of integers that are sorted in ascending order and returns a new array of
the same length with the squares of the original integers also sorted in asscending order.

------ Hints ------


------ Complexity ------ 


------ Recursive Formula ------

------ Iterative Approach ------

"""
def sortedSquaredArray(array):
    return sorted([number ** 2 for number in array])    # and that is it