"""
----- NAME: Maximum Sum Submatrix -----
----- Category: Dynamic programming -----
----- Level: Hard -----
------ BRIEF ------

You're given a two-dimensional array (Matrix) of potentially unequal height and width that's filled with integers.
You are also given a positive integer: "size". 
Write a function that returns the maximum sum that can be generated from a sub matrix with dimensions [size * size].

For example, consider the following matrix:

[
    [2, 4],
    [5, 6],
    [-3, 2],
]

If size = 2, then the 2x2 submatricies to consider are:

[2, 4]
[5, 6]
-----
[5, 6]
[-3, 2]

Some of the elements in the first sub matrix is 17, and some of the elements in the second survey truth is 10. 
In this example, your function should return 17.

Note: Size will always be at least one, and the dimension of the input matrix will always be at least size * size.

Sample Input:

matrix = [
    [5, 3, -1, 5],
    [-7, 3, 7, 4],
    [12, 8, 0, 0],
    [1, -8, -8, 2],
]
size = 2

Sample Output:
18
# based up this matrix  => [
#     [., ., ., .],
#     [., 3, 7, .],
#     [., 8, 0, .],
#     [., ., ., .],
# ]

------ Hints ------

- The brute force approach to solve this problem involves simply considering all possible submatrices of [size * size],
determining their sums, and finally returning the maximum sum. This approach is acceptable, but it is not optimal. 
It's not optimal because it repeats some additions. When considering submatrices of any size larger than one, 
it's almost always the case that some of these matricies will have overlapping elements, 
meaning that will repeatedly add up the same numbers.
If we were to use the brute-force approach, we would get a time complexity of O(width * height * size).
To achieve a more optimal time complexity, we need to avoid reading elements that have already been added.
Can you think of a way to solve this problem in O(width * height) time?

- To avoid doing repeated addition, we have to use auxiliary space. Ideally, this extra space will allow us to determine the sum of a sub matrix of any size in Constantine.
Start by creating matrix with the same dimensions as the input matrix (recall this matrix sums).

------ Complexity ------ 
Time: O(w * h) 
Space: O(w * h)

------ Approach ------

"""

####################################################
## Time: O(w * h) - where w is width and h is height
## Space: O(w * h) - 
####################################################

def maximumSumSubmatrix(matrix, size):
    
    sums = createSumMatrix(matrix)
    maxSubMatrixSum = float("-inf")

    for row in range(size - 1, len(matrix)):
        for col in range(size - 1, len(matrix[row])):
            total = sums[row][col]                          # total value in the sums matrix

            touchesTopBorder = row - size < 0
            if not touchesTopBorder:
                total -= sums[row - size][col]

            touchesLeftBorder = col - size < 0
            if not touchesLeftBorder:
                total -= sums[row][col - size]
            
            touchesTopOrLeftBorder = touchesTopBorder or touchesLeftBorder
            if not touchesTopOrLeftBorder:
                total += sums[row - size][col - size]
            
            maxSubMatrixSum = max(maxSubMatrixSum, total)

    return maxSubMatrixSum

def createSumMatrix(matrix):
    # populate a same size matrix with the sums from (i,j) to the 
    sums = [[0 for _ in range(len(matrix[row]))] for row in range(len(matrix))]
    sums[0][0] = matrix[0][0]

    # Fill the first row
    for idx in range(1, len(matrix[0])):
        # Accumulate the sums for each location from the matrix row
        sums[0][idx] = sums[0][idx - 1] + matrix[0][idx]

    # Fill the first column
    for idx in range(1,len(matrix)):
        # Accumulate the sums for each location from the matrix col
        sums[idx][0] = sums[idx - 1][0] + matrix[idx][0]

    # Fill the rest of the matrix
    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[row])):
            # Add the Sum to the left, add the sum above, subtract the upper left corner value and add the matrix value
            sums[row][col] = sums[row - 1][col] + sums[row][col - 1] - sums[row - 1][col - 1] + matrix[row][col]
    return sums