"""
----- NAME: Quick Sort -----
----- Category: Sorting -----
----- Level: Hard -----
# Has a recursive solution 
------ BRIEF ------
Write a function that takes in an array of integers and returns assorted version of the array.
Use the quicksort algorithm to sort the array.

Sample input:
array = [8, 5, 2, 9, 5, 6, 3]

Sample output: 
[2, 3, 5, 5, 6, 8, 9]

------ Hints ------


------ Complexity ------ 
Time: O() 
Space: O()

------ Approach ------
- PIck one value as your pivot , for example , the first value.
sort every number with respect tot the pivot.
eventually, the pivot will be in its final sorted position.
"""

####################################################
## Time: O(n) - where n is 
## Space: O(n) - 
####################################################

def quickSort(array):
    quickSortHelper(array, 0, len(array) - 1)
    return array

def quickSortHelper(array, startIdx, endIdx):
    if startIdx >= endIdx:
        return
    
    # Pointers
    pivotIdx = startIdx                         
    leftIdx = startIdx + 1
    rightIdx = endIdx                           # right points should be greater than pivot

    while rightIdx >= leftIdx:
        if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
            swap(leftIdx, rightIdx, array)
        if array[leftIdx] <= array[pivotIdx]:
            leftIdx += 1
        if array[rightIdx] >= array[pivotIdx]:
            rightIdx -= 1
			
    swap(pivotIdx, rightIdx, array)

    leftSubArrayIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx + 1)

    if leftSubArrayIsSmaller:
        quickSortHelper(array, startIdx, rightIdx - 1)
        quickSortHelper(array,  rightIdx + 1, endIdx)
    else:
        quickSortHelper(array, rightIdx + 1, endIdx)
        quickSortHelper(array, startIdx, rightIdx - 1)

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]