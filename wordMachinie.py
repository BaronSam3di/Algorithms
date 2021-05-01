'''


Stack of integetrs
Stack is empty
operations are given by a string
    X >> int from 0 to 2^20 -1
    POP >> 
    DUP
    +
    -
Example test:   '4 5 6 - 7 +'
Example test:   '13 DUP 4 POP 5 DUP + DUP + -'
Example test:   '5 6 + -'
Example test:   '3 DUP 5 - -'


REQs
- If the stack is empty it reports an error
- And underflow or overflow in addition or subtraction causes an error.


1. clean the input
2. step through the input
3. process the input
4. apply the input to the Output stack


Example1 = '4 5 6 - 7 +'
Example2 = '13 DUP 4 POP 5 DUP + DUP + -'
Example3 = '5 6 + -'
Example4 = '3 DUP 5 - -'

'''
def cleanInput(commands):
    validatedInput = []
    inputData = commands.split()
    for value in inputData:
        if value == '-' or value == '+' or value == 'DUP' or value == 'POP':
            validatedInput.append(value)
        else:
            validatedInput.append(int(value))
    return validatedInput
            
 
def solution(commands):
    print("commands: ",commands)
    stack = []
    if isEmpty(commands):
        print("Error Code 1: Stack is empty")

    for i in commands:
        if isinstance(i, int):
            stack.append(i)
            print("Appending :", i)
        if i == '-':
            temp = stack[-2] - stack[-1]
            stack.pop(-2)
            stack.pop(-1)
            stack.append(temp)
        if i == 'POP':
            stack.pop(-1)
        if i == 'DUP':
            newDup = stack[-1]
            stack.append(newDup)
    return stack
        

def isEmpty(stack):
    if len(stack) == 0:
        return True


def updateStack():
    pass

def returnTheTop():
    pass


commandData = cleanInput(Example2)
print(commandData)
result = solution(commandData)
print(result[-1])
