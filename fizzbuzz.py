'''
for number in range(51):
    if number % 2 == 0 and number % 5 == 0 and number % 5 == 0:
        print("CodilityTestCoders")
        continue
    elif number % 3 == 0:
        print("Test")
        continue
    elif number % 3 == 0:
        print("Test")
        continue
    elif number % 5 == 0:
        print("Coders")
        continue
    print(number)
'''

'''
result = checkDivisibility(number)
if result is not "":
    print result
else:
    print number
'''

N = 1000




def checkDivisibility(number):
    result = ""
    if number % 2 == 0:
        result += "Codility"
    if number % 3 == 0:
        result += "Test"
    if number % 5 == 0:
        result += "Coders"
    return result

for CandidateNumber in range(1, N+1):
    result = checkDivisibility(CandidateNumber)
    if result != "":
        print(result)
    else:
        print(number)

        