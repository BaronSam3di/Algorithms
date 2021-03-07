"""
----- Longest Peak : Easy -----
------ BRIEF ------
Write a function that 
- takes in an array of integers 
- returns the length of the longest peak in the the array.

A peak is defined as at least three adjacent intergers in the array that are strictly increasing until they reach
a tip (the highest value in the peak), at which point they become strictly decreasing. 



For example, the integers 1, 4, 10, 2 form a peak (at 10) , 
but the intergers 2,0,10 don't and neither do the integers 1,2,2,0. 
Similarly, the integers 1,2,3 don't form a peak because there aren't any strictly decreasing integers after the 3. 

Separate this into two tasks 
- find all the peaks
- compare all peaks to get the longest

--- Finding all peaks---
To find a peak it must be greater than its two adjacent values. 
Starting from the 2nd index up unto the penultimate index, check each value for "peak" status.

Next, how far can we go from the tips until we reach a "no longer decreaseing number", therefore giving us the length of our peak.


------ Hints ------

- You can solve this question by iterating through the array from left =ro right once.

- Iterate through the array from left to right, and treat every integer as the potential top of a peak. 
To be the top of a peak, an interger has to be strictly greater than its adjacent integers. 
What can you do when you find an actual tip?

- As you iterate through the array from left ro right, whenever you find a tip of a peak, 
expand outwards from the tip until you no longer have a peak. 
Given what peaks look like and how many peaks can therefore fit in an array, realize that this process results in a linear-time algorithm.
Make sure to keep track of the longest apeak you find as you iterate though the array.

------ Complexity ------ 
Time O(n)

------ Recursive Formula ------

------ Iterative Approach ------

"""
## O(n) time | O(1) Space
def longestPeak(array):
    longestPeakLength = 0
    i = 1                                                           # not 0 because we need a left hand value to this potential peak
    while i < len(array) - 1:
        isPeak = array[i -1] < array[i] and array[i] > array[i + 1] # ? current value great than its adjacent values?
        if not isPeak:
            i += 1
            continue
        
        # start expanding out from the peak
        leftIdx = i - 2                                             # within here we already know that leftIdx is smaller 
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]: # as long as the value to the left is getting smaller
            leftIdx -= 1                                            # ... we keep looking left

        rightIdx = i + 2
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]: # as long as the value to the right is getting smaller
            rightIdx += 1                                           # ... we keep looking right

        currentPeakLength = rightIdx = leftIdx - 1                  # gets the length
        longestPeakLength = max(longestPeakLength,currentPeakLength)

        i = rightIdx                                                # we have been desending up until this point so start the next peak from here
    
    return longestPeakLength