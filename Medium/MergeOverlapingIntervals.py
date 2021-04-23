"""
----- NAME: Merge Overlaping Intervals -----
----- Category: Arrays -----
----- Level: Medium  -----
------ BRIEF ------

Write a function that takes in a non-empty array of arbitrary intervals,
merges any overlapping intervals, and returns the new intervals in no particular order.

Each interval interval is an array of two integers, with interval[0] as the start of the interval and interval[1] as the end of the interval.

Note the back-to-back intervals are considered to be overlapping. 
For example, [1,5] and [6,7] Aren't overlapping; however, [1,6] and [6,7] are indeed overlapping.

Also note that the start of any particular interval will always be less than or equal to the end of the interval.

Sample input:
intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]

Sample OutPut:
[[1, 2], [3, 8], [9, 10]]
// Merge the intervals [3, 5], [4, 7], [6, 8] into 1.
// The intervals could be ordered differently. 

------ Hints ------

- How can you determine it to intervals overlapping?

- So the intervals with respect to their starting values. 
This will allow you to merge all over lapping intervals in a single traversing through this sorted intervals.

- After sorting the intervals with respect to their starting values, traverse them, and at each iteration,
compare the start of the next interval to the end of the current interval to look for overlap.
If you find an overlap, you take the current intervals so as to merge the next interval into it.

------ Complexity ------ 
Time: O(n log(n)) because we sort the intervals which takes n log n 
Space: O(n) need extraa array length of the input array.

------ Approach ------

"""

####################################################
## O(n log(n)) because we sort the intervals which takes n log n , where n is the length of the input.
## Space: O(n) need extra array length of the input array.
####################################################

def mergeOverlappingIntervals(intervals):

    # Sort the intervals by starting value with a lambda func.
    sortedIntervals = sorted(intervals, key=lambda x: x[0])
    
    # initialise Output
    mergedIntervals = []
    currentInterval = sortedIntervals[0]
    mergedIntervals.append(currentInterval)

    for nextInterval in sortedIntervals:
        # currentIntervalEnd is the 2nd value in this current interval array
        _, currentIntervalEnd = currentInterval
        nextIntervalStart, nextIntervalEnd = nextInterval

        # look for overlap between the end of the current and the start of the next and update
        if currentIntervalEnd >= nextIntervalStart:
            currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)
        else:
            # look at the next interval pair and update the merged
            currentInterval = nextInterval
            mergedIntervals.append(currentInterval)
        
    return mergedIntervals
    