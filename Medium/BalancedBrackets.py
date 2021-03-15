"""
----- NAME: Balanced Brackets -----
----- Category: stacks -----
----- Level : Medium -----
------ BRIEF ------
Write a function that takes in a string made up of brackets ( (,{,[,},],) and }) and other optional characters.
The function should return a boolean representing weather the string is balanced with regard to brackets. 

A string is said to be balanced if it has as many opening brackets of a certian type as it has closing brackets for that type 
and if no bracket is unmatched. 

Note that 
- an opening bracket can't match a corresponding closing bracket that comes before it.
- a closing bracket can't match a corresponding opening bracket that comes after it.
- brackets can't overlap each other as [(]).


------ Hints ------
You want ot use a stack, LIFO style,

------ Complexity ------ 


------ Recursive Formula ------

------ Iterative Approach ------

"""

####################################################
##
####################################################

def balancedBrackets(string):
    openingBrackets = "({["
    closingBrackets = ")}]"
    matchingBrackets = {")":"(","]":"[","}":"{"}
    stack = []
    for char in string:
        if char in openingBrackets:                 
            stack.append(char)                      # we juts need to store the complimentary opening brackets
        elif char in closingBrackets:                
            if len(stack) == 0:                     # there are no opening brackets so False
                return False
            if stack[-1] == matchingBrackets[char]: # does the last value of the stack match with a closeing bracket in matchingBrackets 
                stack.pop()                         # garbage collect the the last value
            else:
                return False
    return len(stack) == 0                          # last check to make sure the stack is empty and no half pairs of brackets are left.
