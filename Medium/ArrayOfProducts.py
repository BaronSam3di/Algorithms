"""
----- Array Of Products  : Medium -----
------ BRIEF ------

Write a function that tales in a non-empty array of integers and returns an array of 
the same length, where each element in the output array is equal to the product of every other number in the input array.

In other words , the value at `output[i]` is equal to the product of every number in the input array other than input[i]

>>>> Note that you're expected to solve this problem WITHOUT USING DIVISION. <<<<

values can be + . - pr zero.

eg; [5,1,4,2] will result in [8,40,10,20]. Index 0 is 8 because 1 x 4 x 2 = 8 , and so on. 
------ Hints ------
- Think about the most naive approach to solving this problem. 
How can we do exactly what the problem wants us to do without focusing at all time and space complexity? 

- Understand how output[i] is being calculated. 
How can we calculate the product of every element other than the one at the current index? 
Can we do this with just one loop through the input array, or do we have to do multiple loops?

- For each index in the input array, try calculateing the product of every element to the left and the product of every element to the right.
You can do this with two loops through the array: one from left to right and one from right to left. How can these products help us?

------ Complexity ------ 
Brute force: Space = O(n) , Time - On^2)
Optimal : Space - O(n) , Time = O(n) where n is the length of the arrya. 

------ Approach ------

"""
## Brute force approach ( without using division :-/ ) 
## Space = O(n), Time - O(n^2)
def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]      # fill it with values of 1's to start
    for i in range(len(array)):                     # set up outer traversal
        runningProduct = 1
        for j in range(len(array)):                 # inner traversal 
            if i != j:                  # except for the index of the outer traversal current element , add the products
                runningProduct *= array[j]
        products[i] = runningProduct
    return products



## Optimal solution
'''  Multiple Linear traversals and gather data through each traversal. '''
## O(n) Time | O(n) Space
def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]      # fill it with values of 1's to start
    leftProducts = [1 for _ in range(len(array))] 
    rightProducts = [1 for _ in range(len(array))] 

    leftRunningProduct = 1
    for i in range(len(array)):
        leftProducts[i] = leftRunningProduct
        leftRunningProduct *= array[i]

    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        rightProducts[i] = rightRunningProduct
        rightRunningProduct *= array[i]

    for i in range(len(array)):
        products[i] = leftProducts[i] * rightProducts[i]

    return products


## improved - removeing the left right Products array. Reduced by two arrays and 1 travesal. 

def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]      # fill it with values of 1's to start

    leftRunningProduct = 1
    for i in range(len(array)):
        products[i] = leftRunningProduct
        leftRunningProduct *= array[i]

    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        products[i] *= rightRunningProduct
        rightRunningProduct *= array[i]

    # for i in range(len(array)):
    #     products[i] = leftProducts[i] * rightProducts[i]

    return products