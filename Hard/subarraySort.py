"""
----- NAME: SubArray Sort -----
----- Category: Arrays -----
----- Level : Hard -----
------ BRIEF ------

Write a function that takes in an array of at least two integers and that returns an array of the starting and ending indices of 
the smallest subarray in the input array that needs to be sorted in place in order for the entire input array to be sorted (in ascending order). 

If the input array is already sorted, the function should return [-1, -1].

Sample Input:
array = [1 ,2 ,4 ,7 ,10 ,11, 7, 12 ,6 , 7, 16, 18, 19]
Sample Output:
[3, 9] // If we sort the values from index 3 to index 9, the entire array will be sorted. 

------ Hints ------
- Realise that even a single out-of-order number in the input array can call for a large subarray to have to be sorted.
This is because, depending on how out of place the number is, 
it might need to be moved very far away from its original position in order to be in its sorted position.

- Find the smallest and largest numbers that are out-of-order in the end array.
You should be able to do this in a single pass through the array.

- Once you found the smallest and largest out-of-order numbers mentioned above, find their final sorted positions in the array.
This should give you the extremities of the smallest subarray that needs to be sorted. Then sort this sub array.

------ Complexity ------ 
Time: O() 
Space: O()

------ Approach ------

"""

####################################################
## Time: O(n) - where n is the length of the array
## Space: O(1) - 
####################################################

def subarraySort(array):
    minOutOfOrder = float("inf")                            # "inf" makes comparisons easier , especially for the base case.
    maxOutOfOrder = float("-inf")

    for i in range(len(array)):
        num = array[i]
        if isOutOfOrder(i, num, array):                    # returns bool if the current num is out of order
            minOutOfOrder = min(minOutOfOrder, num)        # hence initialised with inf as num will be assigned for both
            maxOutOfOrder = max(maxOutOfOrder, num)

    if minOutOfOrder == float("inf"):                      # Edge case -  array must be sorted
        return [-1, -1]

    # --- get the start and end index of the range
    subarrayLeftIdx = 0
    while minOutOfOrder >= array[subarrayLeftIdx]:         # until we find a number smaller than out minimum keep looking
        subarrayLeftIdx += 1
    
    subarrayRightIdx = len(array) - 1
    while maxOutOfOrder <= array[subarrayRightIdx]:        # until we find a number bigger than out maximum keep looking
        subarrayRightIdx -= 1

    return [subarrayLeftIdx, subarrayRightIdx]             # we want ot return index of the range values
    # ------------ 

def isOutOfOrder(i, num, array):
    if i == 0:
        return num > array[i + 1]                          # first num - assert if num is > than the following num in the array
    if i == len(array) - 1:
        return num < array[i - 1]                          # last num - assert if num is < than the previous num in the array
    return num > array[i + 1] or num < array[i - 1]        # compare with previous and next num