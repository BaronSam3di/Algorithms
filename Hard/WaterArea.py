"""
----- NAME: Water Area -----
----- Category: Dynamic programming -----
----- Level :Hard -----
------ BRIEF ------
You're given an array of non-negative integers where each non-zero integer represents the height of a pillar of width one.

Imagine water being poured over all of the pillars; right to function retains the surface area of the water trapped between the pillars viewed from the front.
Note that spilled water should be ignored.

------ Hints ------

- In order to calculate the amount of water above a single point in the input array, 
you must know the height of the tallest pillar to its left and the height of the tallest pillar to his right.

- If a point can hold water above it, and the smallest of the two heights mentioned above minus the height at
 the respective point should lead due to the amount of water above it.

- Try building an array of the left and right max height to each point in the input array.
You should be able to build disarray and to compute the final amount of water above each point in just two loops over the input array.

Sample input: [0,8,0,0,5,0,0,10,0,0,1,1,0,3] , Sample Output: 48
      
Below is a visual representation of the sample input. The dots and vertical lines represent trapped water and pillars, respectively. Note that there are 48 dots.
      
      |
      |
      |
|.....|
|.....|
|.....|
|..|..|
|..|..|
|..|..|
|..|..|.....|
|..|..|..||.|


------ Complexity ------ 
Time: O() 
Space: O()

------ Approach ------
For each index in the array, calculate the amount of water above that index. 
The highest pilar is the most important.

"""

# ------- BEST solution ----------
####################################################
## Time: O(n) - where n is the length of the input array, heights
## Space: O(n) - 
####################################################

def waterArea(heights):
    maxes = [0 for x in heights]
    leftMax = 0
    for i in range(len(heights)):
        height = heights[i]
        maxes[i] = leftMax
        leftMax = max(leftMax, height)
    
    rightMax = 0 
    # resuse maxes array to store right maxes
    for i in reversed(range(len(heights))):                 # going backawards       
        height = heights[i]
        minHeight = min(rightMax, maxes[i])                  # maxes currently has left maxes stored in it
        if height < minHeight:
            maxes[i] = minHeight - height
        else:
            maxes[i] = 0
        rightMax = max(rightMax, height)
    return sum(maxes)



# ------- Broken solution ----------
####################################################
## Time: O(n) - where n is the length of the input array, heights
## Space: O(n) - 
####################################################

def waterArea(heights):
    if len(heights) == 0:
        return 0

    leftIdx = 0
    rightIdx = len(heights) - 1
    leftMax = heights[leftIdx]
    rightMax = heights[rightIdx]
    surfaceArea = 0

    while leftIdx < rightIdx:
        if heights[leftIdx] < heights[rightIdx]:
            leftIdx += 1
            leftMax = max(leftMax, heights[leftIdx])
            surfaceArea += leftMax - heights[leftIdx]
        
        else:
            rightIdx += 1
            rightMax = max(rightMax, heights[rightIdx])
            surfaceArea += rightMax - heights[rightIdx]

    return surfaceArea

