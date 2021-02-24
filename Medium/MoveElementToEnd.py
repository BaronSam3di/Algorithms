"""
----- Move Element To End  : Medium -----
------ BRIEF ------
You're give nan array of integers and an integer. (But this could be used on any data when looking for similar)

Write a function that move all instances of that integer in the array to the right hand end 
of the array and returns the array. 

The function should perform this in place (i.e, it should mutate the input array) and 
doesn't need to maintain the order of the other integers.

Sample input : array = [ 2,1,2,2,23,4,2,]
toMove = 2
result = [1,3,4,2,2,2,2,2] // oder of 'other' numbers not important
------ Hints ------


------ Complexity ------ 
O(n) time | O(1) space - where n is the length of the array

------  Approach ------

Put two pointers, one at each end. 


If the right hand pointer is NOT pointing at the Target, move the righthand pointer along one.
If the left hand point IS pointing at a target then we can swap the values a the two pointers so that the target value is moved the the right hand end.

"""
def moveElementToEnd(array, toMove):
    LeftPointer = 0
    RightPointer = len(array) - 1
    while LeftPointer < RightPointer:
        while LeftPointer < RightPointer and array[RightPointer] == toMove:  # nested while keep RightPointer decrementing AND checks that Left < Right. 
            RightPointer -= 1
        if array[LeftPointer] == toMove:
            array[LeftPointer], array[RightPointer] = array[RightPointer], array[LeftPointer]
        LeftPointer += 1
    return array