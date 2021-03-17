"""
----- NAME: Task Assignment -----
----- Category: Greedy Algorithms -----
----- Level : Medium -----
------ BRIEF ------
You are given an integer k representing a number of workers and an array of positive integers representing
durations of tasks that must be completed by the workers.

Specifically, each worker must compete two unique tasks and can only work on one task at a time.

The number of tasks will always be equal to 2k such that each worker always has exactly two tasks to complete. 
All task are independent of one another and can be competer in any order.

Workers will complete their assigned tasks in parallel, and the time taken to complete all tasks will be 
equal to the time taken to complete the longest pair of tasks will be equal to the time taken to 
complete the longest pair of tasks (see the sample output for an explanation).


Write a function that returns the optimal assignment of tasks to each worker such that the tasks are completed as fast as possible. 

Your function should return a list of pairs, where each pair stores the INDICIES of the tasks that should be completed by one worker.

The pair should be in the following format: [task1, task2], Where are the order of task one and task two doesn't matter. 
Your function can return the pairs in any order. Paragraph if multiple optimal assignments exist, any correct answer will be accepted.

Note: you'll always be given at least one worker (i.e , k Will always be greater than 0)

k = 3           # number of workers
tasks = [1,3,5,3,1,4]
INDICIES 0 1 2 3 4 5
[
[0,2] # tasks[0] = 1, tasks[2] = 5 | 1 + 5 = 6
[4,5] # tasks[4] = 1, tasks[5] = 4 | 1 + 4 = 5
[1,3] # tasks[1] = 3, tasks[3] = 3 | 3 + 3 = 6
]

# Greedy, because you take the optimal solution in that instance.

------ Hints ------

- Start by considering which pairs of tasks will lead to the longest possible time to complete all tasks.

- The amount of time it will take to complete all tasks will be dictated by the pairs of tasks that has the longest total duration. 
This means that you want to avoid pairing long tasks together

- Since the pair of tasks with the longest total duration is the time it takes for us to finish all tasks, we want to minimise this past duration. 
To do this we can simply pay the shortest duration task with the longest duration task and repeat the process with all other tasks.

- Start by sorting the tasks array in ascending order. Then, Pay the shortest-duration task with the longest-duration task, and add that pair to some out parade.
Repeat this process until you've paid all tasks. 
This will lead to an optimal pairing, because your pair of tasks with the longest duration will have the shortest duration that it could possibly have.

------ Complexity ------ 


------ Recursive Formula ------

------ Iterative Approach ------

"""

####################################################
## Time O(n(log(n))) |
####################################################

def taskAssignment(k, tasks):
    pairedTasks = []
    taskDurrationsToIndices = getTaskDurationsToIndices(tasks)

    sortedTasks = sorted(tasks)                                                 # new array

    for idx in range(k):
        task1Duration = sortedTasks[idx]
        indicesWithTask1Duration = taskDurrationsToIndices[task1Duration]
        task1Index = indicesWithTask1Duration.pop()

        task2SortedIndex = len(tasks) - 1 - idx
        task2Duration = sortedTasks[task2SortedIndex]
        indicesWithTask2Duration = taskDurrationsToIndices[task2Duration]
        task2Index = indicesWithTask2Duration.pop()

        pairedTasks.append([task1Index,task2Index])

    return pairedTasks

# Helper functon
def getTaskDurationsToIndices(tasks):
    taskDurationsToIndices = {}                                 # mapping durations to indices

    for idx, taskDuration in enumerate(tasks):
        if taskDuration in taskDurationsToIndices:
            taskDurationsToIndices[taskDuration].append(idx)
        else:
            taskDurationsToIndices[taskDuration] = [idx]        # creates new value for indices
    return taskDurationsToIndices