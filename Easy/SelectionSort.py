"""
----- SelectionSort : Easy -----

------ BRIEF ------
Write a function that takes in an array of integers and erturns a sorted version of that array. Use the Selection Sort Algorithm, to sort the array.


Divide the input array into two subarrays in place, the sub array should be sorted at alltimes and should start with a length of 0
, while the second subarray should be unsorted. 

Find the smallest (or largest ) element in the unsorted subarray and insert it into the sorted sub array with a swap. 
Repeat this process of finding the smallest (or largest ) element in the unsorted subarrray and inserting it in its correct position in the sorted subarray with a swap until the entire array is sorted. 


TO start the entire list will represent the unsorted list. at each iteration we will og through and find the smallest value and place it at the left hand end in the "sorted sub list" section. 
We will then repeat this for the remainder of the "unsorted list " that remains in the array. The swapping will be done in place.


We will store the value of " the smallest so far" and step through the list. once we have realised that a value is the smallest of the Unorderd list, we will send it to the left hand  " sorted" end of the list .
------ Complexity ------ 


------ Recursive Formula ------

------ Iterative Approach ------

"""
## O(n^2) time | O(1) space
def SelectionSort(array):
    currentIdx = 0 # Another way to look at this is like the devider between the sroted and the unsorted sub arrays
    '''
    Beneath our current index gets all the way to the final index, 
    the last number is going to be the highest number so we need go no further 
    '''
    while currentIdx < len(array) - 1: 
        # here we want to find the smallest numbers index in the unsorted sub-list
        smallestIdx = currentIdx
        for i in range(currentIdx + 1, len(array)): # from the second number in the sublist 
            if array[smallestIdx] > array[i]:
                smallestIdx = i
        swap(currentIdx, smallestIdx, array)
        currentIdx += 1
    return array

def swap(i, j, array):
    print("pre Swap",array)
    array[i],array[j] = array[j], array[i]
    print("Post swap",array)