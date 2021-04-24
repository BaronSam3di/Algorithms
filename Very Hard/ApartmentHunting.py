"""
----- NAME: Apartment Hunting -----
----- Category: Arrays -----
----- Level: Very Hard -----
------ BRIEF ------
- You are looking to move into a new apartment on a specific Street, 
and you're given a list of contiguous blocks on that street where each block contains an apartment that you could move into.

You also have a list of requirements:
- A list of buildings that are important to you. For instance, you might value having a school and gym near your apartment.
The list of blocks that you have contains information that every block about all of the buildings that are present and absent at the block in question.
For instance, for every block, you might know whether the school, a pool, an office, and a gym at present.

In order to optimise your life, you want to pick an apartment block such that you minimise the farthest distance 
you to have to walk from your apartment to reach any of your required buildings.

Write a function that takes in a list of contiguous blocks on a specific street and a list of your required buildings, 
and that returns to location (the index) of the block that's most the optimal for you.

If there are multiple most optimal blocks, your function can return the index of any one of them.

--- Sample input: --- 

blocks = [
    {
    "gym": false,
    "school": true,
    "store": false
    },
    {
    "gym": true,
    "school": false,
    "store": false
    },
    {
    "gym": true,
    "school": true,
    "store": false
    },
    {
    "gym": false,
    "school": true,
    "store": false
    },
    {
    "gym": false,
    "school": true,
    "store": true
    },
]
reqs = ["gym","school","store"]

---  Sample output: --- 
index 3 
// The farthest you'd have to walk to reach the gym, school, or a store is one block. 
At any other index, you'd have to walk further
------ Hints ------


------ Complexity ------ 
Time: O() 
Space: O()

------ Approach ------
"""
####################################################
## Optimal 
## Time: O(br) - where b is hte blocks and r is the requirements
## Space: O(br)  
####################################################

def apartmentHunting(blocks, reqs):
    # precompute all the nearest reqs at each block.
    minDistancesFromBlocks = list(map(lambda req: getMinDistances(blocks, req), reqs))
    maxDistancesAtBlocks = getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks)
    return getIdxAtMinValue(maxDistancesAtBlocks)

def getMinDistances(blocks,req):
    # precompute method
    minDistances = [0 for block in blocks]
    closestReqIdx = float("inf")

    for i in range(len(blocks)):
        if blocks[i][req]:
            closestReqIdx = i
        minDistances[i] = distanceBetween(i, closestReqIdx)
    
    for i in reversed(range(len(blocks))):
        if blocks[i][req]:
            closestReqIdx = i
        minDistances[i] = min(minDistances[i], distanceBetween(i, closestReqIdx))
    return minDistances

def getMaxDistancesAtBlocks(blocks, minDistancesFromBlocks):
    maxDistancesAtBlocks = [0 for block in blocks]
    for i in range(len(blocks)):
        minDistancesFromBlock = list(map(lambda distances: distances[i], minDistancesFromBlocks))
        maxDistancesAtBlocks[i] = max(minDistancesFromBlock)
    return maxDistancesAtBlocks

def getIdxAtMinValue(array):
    idxAtMinValue = 0
    minValue = float("inf")
    for i in range(len(array)):
        currentValue = array[i]
        if currentValue < minValue:
            minValue = currentValue
            idxAtMinValue = i
    return idxAtMinValue

def distanceBetween(a,b):
    return abs(a - b)


####################################################
## Less optimal
## Time: O(b^2 * R) - where b is the blocks, R is the requirements. nested for loop of B 
## Space: O(B) - 
####################################################

def apartmentHunting(blocks, reqs):
    maxDistanceAtBlocks = [float("-inf") for block in blocks]
    for i in range(len(blocks)):                                                            # better to keep of track of the indices of the blocks
        for req in reqs:
            closestReqDistance = float("inf")                                               # initialise to inf will make the code cleaner when comapreing to a min
            for j in range(len(blocks)):
                if blocks[j][req]:                                                          # if this block has the req as true
                    closestReqDistance = min(closestReqDistance, distanceBetween(i, j))     # min between the requirement and the current block
            maxDistanceAtBlocks[i] = max(maxDistanceAtBlocks[i], closestReqDistance)
    return getIdxAtMinValue(maxDistanceAtBlocks)

def getIdxAtMinValue(array):
    idxAtMinValue = 0
    minValue = float("inf")
    for i in range(len(array)):
        currentValue = array[i]
        if currentValue < minValue:
            minValue = currentValue
            idxAtMinValue = i
    return idxAtMinValue


def distanceBetween(a, b):
    return abs(a - b)