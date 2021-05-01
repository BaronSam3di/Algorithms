"""
----- NAME: Waterfall streams -----
----- Category: Arrays -----
----- Level : Very Hard -----
------ BRIEF ------

You're given 
- a two dimensional array that represents the structure of an indoor waterfall
- a positive integer that represents the column that the waterfalls watersource will start at.

More specifically, the water source will start directly above the structure and will flow downwards. 

Each row in the array contains 0's and 1's, where a 0 represents a free space and 1 represents a block that water can't pass through.
You can imagine that the last row of the array contains buckets that the water will eventually flow into; thus, the last rate of the array will always contain only 0's.
You can also imagine that there are walls on both sides of the structure, meaning that water will never leave the structure; 
it will either be trapped against the wall or flow into one of the buckets in the last row.

As water flows down which, if it hits a block, it's split evenly into the left and right hand side of that block.
In other words, 50% of the water flows left and 50% of it flows right. If the water streaming is unable to fly to the left or to the right (because of a block or a wall), 
the water stream in question becomes trapped and can no longer continue to flow in that direction;
It's affectively get stuck in the structure to no longer flow downwards, meaning that 50% of the previous water stream is forever lost.

Lastly, the input array will always contain at least two rows and one column, 
and the space directly below the water source (in the first row of the array) will always be empty,
allowing the water to start flying downwards.

Write a function that returns the percentage of water inside each of the bottom buckets after the water has flowed through the entire structure.

Sample input:

array = [
    [0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0],
]
source= 3   ( column 3)

Sample Output:
[0, 0, 0, 25, 25, 0, 0]
// The water will flow as follows:
// [
//   [0, 0, 0, ., 0, 0, 0],
//   [1, ., ., ., ., ., 0],
//   [0, ., 1, 1, 1, ., 0],
//   [., ., ., ., ., ., .],
//   [1, 1, 1, ., ., 1, 0],
//   [0, 0, 0, ., ., 0, 1],
//   [0, 0, 0, ., ., 0, 0],
// ]


------ Hints ------
-Try not to overthink the solution to this problem.
If you were to manually go through an example of water flowing downwards through the waterfall structure, what steps would you follow exactly? 
Can you simply transcribe these steps into code?


- To start, consider how you would solve this problem if there were only two rows. How would you make water flow from the first row to the second row with your code? 
Can you make a slight modification to this approach in order to solve this problem for any number of rows?

- You'll want to traverse through the input array, All the while keeping track where and how much water flows. 
To do this, you'll need to represent water with some value (-1, for example, to distinguish it from the other the values in the array).

Iterate through the input array, row by row, column by column, specifically looking at each current row and the row above it.

When you see water in the row above, you'll have to reiterate through both the ow above and the current row to see 
where the water will flow to next (i.e; wheather there are open spaces allowing the water to flow sideways and / or downwards),
mutating these rows along the way whenever water does flow. 

You'll have to make sure to keep track of the percentage of water that's flowing whenever water gets split in half.


------ Complexity ------ 
Time: O() 
Space: O()

"""

####################################################
## Time: O(n) - where n is 
## Space: O(n) - 
####################################################


def waterfallStreams(array, source):
    rowAbove = array[0][:]
    # Will use -1 to represent water, since one is used for a block.
    rowAbove[source] = -1

    for row in range(1, len(array)):
        currentRow = array[row][:]      # copy the current row so we can modify the copy and not the input

        for idx in range(len(rowAbove)):
            valueAbove = rowAbove[idx]

            hasWaterAbove = valueAbove < 0          # tells us if there is water above
            hasBlock = currentRow[idx] == 1

            if not hasWaterAbove:
                continue

            if not hasBlock:
                # If there is not block in the current column, move the water down.
                currentRow[idx] += valueAbove
                continue

            splitWater = valueAbove / 2

            # Move water right. 
            rightIdx = idx
            while rightIdx + 1 < len(rowAbove):             # make sure we havn't gone off the RHS
                rightIdx += 1
                if rowAbove[rightIdx] == 1:
                    break
                if currentRow[rightIdx] != 1:
                    currentRow[rightIdx] += splitWater      # update the water stream at the idx
                    break

            # Move water left similar to the above.          
            leftIdx = idx
            while leftIdx - 1 >= 0:                         # left hand end check
                leftIdx -= 1
                if rowAbove[leftIdx] == 1:
                    break
                if currentRow[leftIdx] != 1:
                    currentRow[leftIdx] += splitWater
                    break
            
        rowAbove = currentRow

    finalPercentages = list(map(lambda num: num * -100, rowAbove))

    return finalPercentages
