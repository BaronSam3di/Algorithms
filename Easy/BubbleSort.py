"""
----- Bubble Sort : Easy -----
------ BRIEF ------
Write a function that tales in an array of integers and returns a sorted version of that array. use the Bubble Sort algorithm to sort the array.

The goal is to sort a list of numbers in assending order. 
On each iteration we will swap if  the number on right of the current number larger than the current number ;ie are they sorted.
If they are not in the correct order, we will swap the number in place ( we are not useing a helper array like other sort algos).


------ Hints ------


------ Complexity ------ 
Space = O(1) because it is done in place, not storage needed
Time = O(n^2) could be at worst 

"""
## Time o(n^2) | Space O(1)  
def bubbleSort(array):
    isSorted = False
    counter = 0    #  Very small optimization 
    while not isSorted:
        isSorted = True
        for i in range(len(array) - 1 - counter):
            if array[i] > array[i + 1]:
                swap(i, i + 1 , array)
                isSorted = False
        counter += 1
    return array

def swap(i, j , array):
    array[i], array[j] = array[j], array[i]     # putting this in the main function is better for python 