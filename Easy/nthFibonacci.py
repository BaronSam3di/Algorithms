"""
----- Nth Fibonacci : Easy -----
------ BRIEF ------
The Fibonacci sequence is defined as follows:
The first number of the sequence is 0, the second number is 1, and the nth number is the sum of (n-1)th and (n-2)th numbers.

IT is a static sequence 

Write a function tha takes in an integer n and returns the nth Fibonacci number. 

Important note: the Fibonacci sequence is often defined with its first two numbers as F0 = and F1 = 1. 
For the purpose of this question , the first Fibonacci number is F0; therefore, getNthFib(1) is equal to F0, 
getNthFib(2) is equal to F1. etc.

------ Hints ------

The formula to generat the nth Fibonacci number can be written as follows: F(n) = F(n -1) + F(n -2). think if the case(s) foe which 
this formula doesn't apply (the base case(s)) and try to implement a simple recursive algorithm to find the nth Fibonacci number with this formula.

What ar the runtime implications of solving this problem as is described in the Hint above. ? Can you use memorization ( cacheing) to 
improve the performance of your algorithm?

Realise tha to calculate any single Fibonacci number you only need to have the two previous Fibonacci numbers. KNowing this, can you implement and iterative
algorithm to solve this question, storing only the last two Fibonacci numbers at any given time?

------ Complexity ------ 


------ Recursive Formula ------

------ Iterative Approach ------

"""


## Naive recursive method 
'''
Time: O(2^n) - Not the best time complexity because we are doing a lot of unnecessary calculations. 
If we call fib(5) , this will call (fib(4) and fib(3). fib(4) will also call fib(3). A lot of duplication.
Space O(n) - because of the all the recursive calls
'''
def getNthFib(n):
    # 2 base Cases
    if n == 2:
        return 1
    elif n == 1:
        return 0
    # Recursive case
    else :
        return getNthFib(n-1) + getNthFib(n-2)

## Better Recursive method which is faster due t othe cashine
""" 
Time O(n) - because We are only calculateing each Fib number once and storeing it in a Hash table for later access.
"""

def getNthFib(n, hashTable = {1: 0, 2: 1}):
    if n in hashTable:
        return hashTable[n]
    else: 
        hashTable[n] = getNthFib(n -1, hashTable ) + getNthFib(n-2 , hashTable)
        return hashTable[n]



## Iterative approach (the best approach)
## O(n) time | O(1) Space
"""
here we use an array of the last 2 fibonacci number and a counter to keep the fibonacci number. 
"""
def getNthFib(n):
    lastTwo = [0,1]                             # initial values
    counter = 3                                 # base fibonacci
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]  # python ternary operator format
