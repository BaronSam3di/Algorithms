"""
----- Find Three Largest Numbers : Easy -----
------ BRIEF ------
Write a function that takes in an array of at least three integers and , withour sorting the input array, 
return a sorted array of the three largest integers in the input array.

The function should return duplicate integers if necessary; for example, 
it should return [10,10,12] for an array input of [10,5,9,10,12].

We would store and keep track of the three largest numbers as we go through the array.

Initialise an empty array for storeing the numbers. We will put the first number in as the first largest number ,
we then look at the 2nd number in the unsorted array and check if that is less than the first largest number 
we will place as the 2nd largest number regardless. If the third number from the unsorted list is greater than 
the 2nd number we will shift the number down ( or out if need be).


This algorithm will be checking an unsorted number against the each element of the sorted array and 
then shifting a sorted number along according to its size. 
------ Hints ------


------ Complexity ------ 
Time = O(N) we have to go through the entire array
Space = O(1) Storage will be slightly bigger than the size of the array so constant.

"""

def findThreeLargest(array):
    threeLargest = [None,None,None]         # initialise our final array
    for num in array:
        updateLargest(threeLargest, num )   # helper method to abstract updateing the largest
    return threeLargest                     # reset the threelargest


def updateLargest(threeLargest, num):
    # compare 1 by 1 each num against the largest number first
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num , 2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num , 1) 
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num , 0)

def shiftAndUpdate(array, number, index):
    for i in range(index + 1):
        if i == index                     # are we at the last index?
            array[i] =  number
        else:
            array[i] = array[i+1]       # this step moves the number down by 1 space