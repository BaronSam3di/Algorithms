"""
----- NAME: Disk Stacking -----
----- Category: Dynamic programming -----
----- Level :  -----
------ BRIEF ------

You're given a non-empty array of arrays where each subarray holds three integers and represents a disk.

These integers denote each discs width, depth, and height, respectively. 
Your goal is to stack up the disks to form the tallest tower possible and to maximize the total height of the stack. 

A disk must have a strictly smaller width, depth and height than any other disc below it.

Write a function on the return is an array of the disks in the final stack, starting with the top desk and ending with the bottom desk. 
Note that you can't rotate discs; in other words, the integers in each separate must represent [ width, depth, height ] at all times.

You can assume that there will only be one stack with the greatest total height. 

Sample Input 
disks = [[2, 1, 2], [3, 2, 3], [2, 2, 8], [2, 3, 4], [1, 3, 1], [4, 4, 5]]

Sample OutPut
[[2, 1, 2], [3, 2, 3], [4, 4, 5]]
// 10 ( 2 + 3 + 5 ) is the tallest height we can get by stacking disks following the rules laid ot above.

------ Hints ------
- Try building an array of the same length as the array of discs. 
At each index I in this new array, store the height of the tallest tower that can be created with the disc located at index I at the bottom.

- Consider sorting the disks by width, depth, or height for a slight optimisation.

- Can you efficiently keep track of potential towers in another array?
Instead of storing in title sequences of discs, try storing the indices of previous discs.
For example, at index three on this other array, story index of the before-last disc in the tallest tower who's bass is the disk index 3.

------ Complexity ------ 
Time: O() 
Space: O()

------ Approach ------
Sort the input array by the heights and 

"""

####################################################
## Time: O(n^2) - where n is the length of the arrrya 
## Space: O(n) - 
####################################################

def diskStacking(disks):
    
    disks.sort(key = lambda disk: disk[2])      # This Lambda function will sort the disks by height (index two)
    heights = [ disk[2] for disk in disks ]          
    sequences = [ None for disk in disks ]
    maxHeightIdx = 0

    for i in range(1, len(disks)):              # start at index one for the first tower
        currentDisk = disks[i]
        for j in range(0, i):
            otherDisk = disks[j]
            if areValidDimensions(otherDisk, currentDisk):
                if heights[i] <= (currentDisk[2] + heights[j]):
                    heights[i] = currentDisk[2] + heights[j]
                    sequences[i] = j
                    
        if heights[i] >= heights[maxHeightIdx]:
            maxHeightIdx = i
	return buildSequence(disks,sequences,maxHeightIdx)



def areValidDimensions(otherDisk, currentDisk):
    return otherDisk[0] < currentDisk[0] and otherDisk[1] < currentDisk[1] and otherDisk[2] < currentDisk[2]

def buildSequence(array,sequences, currentIdx):
    sequence = []
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequences[currentIdx]
    return list(reversed(sequence))