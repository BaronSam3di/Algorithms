"""
----- NAME: Min number of Jumps -----
----- Category: Dynamic programming -----
----- Level : Hard -----
------ BRIEF ------
You're given a non-empty array of positive integers where each interger represents the maximum number of steps you can take forward in the array.

For example, if the element at index 1 is 3 you can go from index 1 to index 2, 3, or 4. 

Write a function that returns the minimum number fo jumps needed to reach the final index. 

Note that jumping from index i to index i + x always constitutes one, jump, no matter how large x is.

Sample Input:
array = [3,4,2,1,2,3,7,1,1,1,3]

sample output: 
4 // 3
------ Hints ------
- try building an array of the minimum number of jumps needed to go from index 0 to all indices. Start at index 0 and progressively build up the array,
using previously calculated values to find next ones.

- Building the array mentioned above should be feasible using two for loops. In an effort to optimise your algorithm, realise that at any point in
the array you know the farthest index that you can reach as well as the number of steps that you have left until you must "consume" a jump.

- After initializing your maximum reach as well as your current number of steps to the value stored at index 0, 
you can easily update your maximum reach as you traverse the input array by simply comparing it to the value stored at each index.

You can also remove one step from your current number of steps at each index, since moving from one index to the next uses up one step.
When your steps reach zero, find a way to calculate how many steps you actually have left using the maximum reach and the index that you're at.

------ Complexity ------ 
Time: O() 
Space: O()

------ Approach ------

"""



####################################################
## Optimal - Use the concept of max reach and steps
# ## Time: O(n) - where n is 
## Space: O(1) - only ever storing 3 values 
####################################################

def minNumberOfJumps(array):
    if len(array) == 1:
        return 0
    jumps = 0 
    maxReach = array[0]
    steps = array[0]
    for i in range(1, len(array) - 1):
        maxReach = max(maxReach, i + array[i])
        steps -= 1
        if steps == 0:
            jumps += 1
            steps = maxReach - i
    return jumps + 1 # once here we are at a len(array) - 1




####################################################
## Time: O(n^2) - where n is 
## Space: O(n) - 
####################################################
def minNumberOfJumps(array):
    jumps = [float("inf") for x in array]
    jumps[0] = 0
    for  i in range(1, len(array)):
        for j in range(0, i):
            if array[j] + j >= i:
                jumps[i] = min(jumps[j] + 1, jumps[i])
    return jumps[-1]