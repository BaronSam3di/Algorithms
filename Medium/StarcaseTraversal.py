"""
----- NAME: StairCase Traversal -----
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

Use memoisation : Cache the results to save time and space.
Time: O(k*n) - where K is the max number of steps we can take ;and n ih the height.
------ Iterative Approach ------

"""

####################################################