"""
----- NAME: Min Rewards -----
----- Category: Arrays -----
----- Level :  -----
------ BRIEF ------

Imagine that you're a teacher who's just graded the final exam in a class.

You have a list of student scores on the final exam in a particular order (Not necessarily sorted), and you want to reward your students. 
You decide to do so fairly by giving them arbitrary rewards ( maybe apples? ) following two rules:

1. All students must receive at least one reward.

2. Any student must receive strictly more awards than the adjacent student (a student immediately to the left or to the right) with a lower score and
must receive strictly fewer awards than an adjacent student with a higher score.

Write a function that takes in a list of schools and returned the minimum number of rewards that you must give out to students to satisfy the two rules.

You can assume that all students have different scores; in other words, the scores are all unique.

Q: Are there negative numbers? No
Q: Could students have the same grade? No
Q: Does the order matter? Yes. You cannot sort the array.

Sample input:
scores = [ 8, 4, 2, 1, 3, 6, 7, 9, 5]

Sample output:
25 // 25 is the minimum number of rewards. You would give out the following rewards: [4, 3, 2, 1, 2, 3, 4, 5, 1]

Compare the socres and the rewards per person. Cna you see the pattern?
scores = [ 8, 4, 2, 1, 3, 6, 7, 9, 5]
rewards: [ 4, 3, 2, 1, 2, 3, 4, 5, 1]


-----

Could you just give a socres out, starting with 1, giving more or less than the last. 
Even if this goes to negative numbers, at the end you find the range and add it to all score values.

------ Hints ------
- You could try iterating through the input list of scores and incrementing the number of rewards you give each student if they
 have a greater score than the previous student's score. 
However, if you reach a student with a smaller school than the previous student school, 
you'll have to backtrack through the array to fix previous reward assignments.
During this backtrack, is it correct to simply increment the rewards of a student who score is greater than the next student score 

- Noticed that there are local mins and local maxes in the input list of scores: Scores that are smaller than both scores next to them and scores that are greater than both scores next to them.
Find a local mins, and try expanding away from them until you reach local maxes, assigning (and incrementing) rewards as you go.

- Do you actually need to find a local mins mentioned above? Can you simply do two sweeps of the input list of scores, one from left to right, and one from right to left?


------ Complexity ------ 
Time: O() 
Space: O()

------ Approach ------r

"""

####################################################
## OPTIMAL SOLUTION
## Time: O(n) - 
## Space: O(n) -
# ### mimic locla min expansion , but without local Mins 
####################################################

def minRewards(scores):
    rewards = [1 for _ in scores]
    for i in range(1, len(scores)):                             # only compare previous values
        if scores[i] > scores[i - 1]:                           # are we in an upward trend?
            # make the reward greater than the reward that came before. No need for max check as all rewards are set to 1
            rewards[i] = rewards[i - 1] + 1                 

    for i in reversed((range(len(scores) - 1))):                # compare from the other end. Exclude the last value to start
        if scores[i] > scores[i + 1]:                           # are we in an backward upward trend? 
            rewards[i] = max(rewards[i], rewards[i + 1] + 1)    # ????
    return sum(rewards)


####################################################
## not as optimal solution
## Time: O(n) - 
## Space: O(n) - 
# Find local mins, expand of the left, expand of the right and do the max check.
####################################################

def minRewards(scores):
    rewards = [1 for _ in scores]
    localMinIdxs = getLocalMinIdx(scores)               
    for localMinIdx in localMinIdxs:
        expandFromLocalMinIdx(localMinIdx, scores, rewards)
    return sum(rewards)

def getLocalMinIdx(array):
    if len(array) == 1:
        return [0]
    localMinIdxs = []
    for i in range(len(array)):
        if i == 0 and array[i] < array[i + 1]:
            localMinIdxs.append(i)
        if i == len(array) - 1 and array[i] < array[i - 1]:             # end of array
            localMinIdxs.append(i)
        if i == 0 or i == len(array) - 1:                               # if i was the first or last 
            continue
        if array[i] < array[i + 1] and array[i] < array[i - 1]:         
            localMinIdxs.append(i)
    return localMinIdxs

def expandFromLocalMinIdx(localMinIdx, scores, rewards):
    
    leftIdx = localMinIdx - 1
    while leftIdx >= 0 and scores[leftIdx] > scores[leftIdx + 1]:               # as long as we are on an incresing trend
        rewards[leftIdx] = max(rewards[leftIdx], rewards[leftIdx + 1] + 1)
        leftIdx -= 1

    rightIdx = localMinIdx + 1                                                  # as long as we are on an decresing trend
    while rightIdx < len(scores) and scores[rightIdx] > scores[rightIdx -1]:

        # no need for the max check like above. Going right will have the initial values.
        rewards[rightIdx] = rewards[rightIdx - 1] + 1                       
        rightIdx += 1


    ####################################################
## Naive approach
## Time: O(n^2) - where n is 
## Space: O(n) - because of th erewards array that is the length of the input array
####################################################

def minRewards(scores):
    rewards = [1 for _ in scores]

    for currentScoreIdx in range(1, len(scores)):
        lastScoreIdx = currentScoreIdx - 1                  

        if scores[currentScoreIdx] > scores[lastScoreIdx]:
            rewards[currentScoreIdx] = rewards[lastScoreIdx] + 1
        else:
            while lastScoreIdx >= 0 and scores[lastScoreIdx] > scores[lastScoreIdx + 1]:
                rewards[lastScoreIdx] = max(rewards[lastScoreIdx], rewards[lastScoreIdx + 1] + 1)   # caveat check
                lastScoreIdx -= 1
    return sum(rewards)
