"""
----- SmallestDifference : MEdium -----
------ BRIEF ------
Write a function that takes in two non-empty arrays of integers, 
finds the pair of numbers (one from each array) whose absolute difference is closest to zero, 
and returns an array containing these two numbers,
with the number from the first array in the first position. 

Note that the absolute difference if two integers is the distance between them on the real number line. 
For example, the absolute difference of -5 and 5 is 10, and the absolute difference of -5 and -4 is 1.

You can assume that there will only be one pair of numbers with the smallest difference.

------ Hints ------


------ Complexity ------ 
Time : O(n log(n)) + m log(m))

------ Approach ------

A)[-1,5,10,20,28,3]  B)[26,134,135,15,17]
The solution for this is are the numbers [28,26]. These have the smallest distance.

First sort the arrays into assending order. 
We then choose the first number from each sorted array. If number A is smaller than number B then choose a new pair by incrementing the choice from array A.
This is because decrementing the index of the next number from array A would make the difference even greater, which is the opposite of what we want.

The rule we follow is incrementing the side which has the smallest number. This is a strategic selection of pairs as appposed to a brute force approach. 

"""
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()                         # assumeing this is ok to sort the arrays in place
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    smallest = float("inf") # set to infinity because after the first iteration this will be updated.
    current = float("inf")
    smallestPair = []
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxTwo += 1
        else:
            return [firstNum, secondNum]
        if smallest > current:
            smallest = current
            smallestPair = [firstNum,secondNum]
    return smallestPair


# NEED TO REVIEW