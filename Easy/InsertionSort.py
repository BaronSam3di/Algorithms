"""
----- Insertion Sort : Easy -----
------ BRIEF ------
Take a list of unsorted numbers. To sort in assending order, starting from the left hand side, take a number and check if it is lower than the number to its right.

------ Hints ------


------ Complexity ------ 
Time O(n^2)
Space O(1)

"""
# import random
# testData = [random.randint(-200, 200) for _ in range(100)]

# ## Space O(n^2) | Time O(1)
# for i in range(1, len(array)):              # starting at index 1 
#             j = i
# 		while j > 0 and array[j] < array[j -1]: # while the current number is out of position
# 			swap(j,j-1, array)				    # helper function to swap with the previous number
# 			j -= 1
# 	return array
			
# def swap(i , j , array):                        # this doesn't have to be a helper function
# 	array[i], array[j] = array[j], array[i]       

# Test1 = [8, 5, 2, 9, 5, 6, 3]


# insertionSort(testData)



import random
testData = [random.randint(-200, 200) for _ in range(100)]

## Space O(n^2) | Time O(1)
def insertionSort(array):
    for i in range(1, len(array)):
	    j = i
	    while j > 0 and array[j] < array[j - 1]: 
		    swap(j , j -1 , array)
		    j -= 1
    return array

def swap(i, j , array):
	array[i], array[j] = array[j], array[i] 



insertionSort(testData)