"""
----- Minimum Waiting Time : Level -----
------ BRIEF ------
You are give a non-empty array of positive integers representing the amounts of time that specific queries take to execute. Eg 
Only one query can be executed at a time, but the queries can be executed in any order. 

A query's waiting time is defined as the amount of time that it must wait before its execution starts. 

In other words, if a query is executed second, then its waiting time is the duration of the first query; if a query is executed third, 
then its waiting time is the sum of the durations of the first two queries.

Write a function that returns the minimum amount of total waiting time for all queries. For example, if you're given the queries of durations [1,4,5],
then the total waiting time if the queries were executed in the order of [5,1,4] would be "(0) + 5 + (5+1) = 11". 

The first query of duration 5 would be executed immediately, so its wating time could be 0, 
the second query of duration 1 would have to wait 5 seconds (the duration of the first query) to be executed, 
and he last query would have to wait the duration of the first two queries before being executed. 

Note: you are allowed to mutate the array.

------ Hints ------
- Even though you don't need to return the actual order in which the queries will be executed to minimize the total waiting time, 
its important to determine what this order should be. Start by doing so.

- can you solve this problem inn constant space? What advantage does being able to mutate the input array provide?

- Sort the array in place , and execute the shortest queries in their sorted order. This should allow you to calculate the minimum waiting time.

- Create a variable to store the total waiting time, and iterate through the sorted input array.
At each iteration, multiply the number of queries left by the duration of the current query, and add that to the total waiting time. 


uses a greedy algorithm because it picks the shortest number . 

(Multiply [i:] len(array-1) and then pop i  )
------ Complexity ------ 
Time: O(n log(n)) where is the len of input array.  
Space: O(1) - no extra space needed

"""

###########################################################################
### My Solution after 10 mins of writing the problem, watching the explanation with out the code.
###########################################################################
def minimumWaitingTime(queries):
    total = 0
	new = sorted(queries)
	leng = len(queries)
	for i in range(len(new[1:])):
		total += (leng-1)*new[i]
		leng -= 1
    return total

###########################################################################
### My Solution after 10 mins of writing the problem, watching the explanation with out the code.
###########################################################################
time O(n log(n)) | O(1) Space
def minimumWaitingTime(queries):
    queries.sort()
    totalWaitingTime = 0
    for index, duration in enumerate(queries):
        queriesLeft = len(queries) - (index + 1)                # because we start at index 0, so we need to add one ot hte index
        totalWaitingTime += duration * queriesLeft              
    
    return totalWaitingTime