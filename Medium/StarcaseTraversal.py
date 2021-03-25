"""
----- NAME: StairCase Traversal -----
# Has a recursive solution 
----- Category: Recursion -----
----- Level : Medium -----
------ BRIEF ------
You are given two positive integers representing the height of a staircase and the maximum number of steps that you can advance up the startcase at a time. 
Write a function that returns the number of ways in which you can climb the staircase.

For example, if you were given a staircase of "height = 3" and "maxsteps =2" you could climb the staircase in 3 ways. 
- You could take 1 step, 1 step, then 1 step
- You could also take 1 step, then 2 steps;
- You could take 2 steps, then 1 step. 

note that maxSteps <= height will always be true. 

------ Hints ------

------ Complexity ------ 

------ Solution 1 ------

Time: O(k^n) - where K is the max number of steps we can take ;and n ih the height.
Space: O(n)
Because this is a good problem to solve recursively, if we reduce the problem to 2 or 3 steps, then we can scale it up. 
The pattern to get to a height of h, is to work out how many ways there are to get to (h-1) + (h-2). 

if the height == 0 or 1:
    return 1
return FUNC(h-1) + FUNC(h-2) + ... +FUNC(h-s) # where s is the max steps

------ Solution 2 ------
Time: O(n) | Space: O(n)
Use memoisation : Cache the results to save time and space.
Time: O(k*n) - where K is the max number of steps we can take ;and n ih the height.
------ Iterative Approach ------
"""

####################################################
## Solution 1:  O(k^n) Time | (O(n) Space
####################################################

def startcaseTraversal(height, maxSteps):
    return numberOfWaysToTop(height, maxSteps)

def numberOfWaysToTop(height, maxSteps):
    if height <=1 :
        return 1
    
    numberOfWays = 0
    for step in range(1,min(maxSteps, height) +1 ):          # The min function is there for when the the height is smaller than the max steps
        numberOfWays += numberOfWaysToTop(height - step, maxSteps)
    
    return numberOfWays



####################################################
## Solution 2 :O(k * n) Time | (O(n) Space
####################################################
# As above but with Memoisation

def startcaseTraversal(height, maxSteps):
    return numberOfWaysToTop(height, maxSteps, { 0:1, 1:1 })        # adding the memoise base case

def numberOfWaysToTop(height, maxSteps, memoize):                   # memoise is the cache
    if height in memoize:
        return memoize[height]                                      # return the existing awnser
    
    numberOfWays = 0
    for step in range(1,min(maxSteps, height) +1 ):          # The min function is there for when the the height is smaller than the max steps
        numberOfWays += numberOfWaysToTop(height - step, maxSteps)

    memoize[height] = numberOfWays
    
    return numberOfWays

####################################################
## Solution 3 :O(k * n) Time | (O(n) Space
####################################################
# As above but with Memoisation

def startcaseTraversal(height, maxSteps):
    waysToTop = [0 for _ in range(height + 1)]          # initialize data structure for cache
    waysToTop[0] = 1
    waysToTop[1] = 1

    for currentHeight in range (2, height + 1):
        # this is where we do the k work
        step = 1
        while step <= maxSteps and step <= currentHeight:
            # below line looks backward in data structure and see how the previous were solved and add that
            waysToTop[currentHeight] = waysToTop[currentHeight] + waysToTop[currentHeight + step] 
            step += 1

        return waysToTop[height]  


####################################################
## Solution 4: O(k * n) Time | (O(n) Space
####################################################
# As above but with Memoisation

def startcaseTraversal(height, maxSteps):
    currentNumberOfWays = 0 
    waysToTop = [1]

    for currentHeight in range(1, height + 1):
        startOfWindow = currentHeight - maxSteps - 1        # calculating the number we need to subtract . We want the value from the previous window
        endOfWindow = currentHeight - 1
        if startOfWindow >= 0:                              
            currentNumberOfWays -= waysToTop[startOfWindow]  

        currentNumberOfWays += waysToTop[endOfWindow]       # This is the new value we are adding
        waysToTop.append(currentNumberOfWays)

    return waysToTop[height]
