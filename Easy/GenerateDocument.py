"""
----- NAME : Level -----
------ BRIEF ------


You are given a string if available characters and a string representing a document that you need to generate. 
Write a function that determins if you can generate the document using the available characters. 
If you cna generate the document, your function should return `true`; otherwise return `false`.

You are only able to generate the document if
- the frequency of unique characters in the characters string is greater than or
equal to the frequency of unique characters in the document string. 

For example, if you're given `characters = "abcabc"` and document = "aabbccc"
you cannot genreate the document because you're missing one "c". 
The document that you need to create may contain any characters, including special characters, capital letters, numbers, and spaces.

BAsically, are the characters a jumbled up version of the string. 


------ Hints ------


------ Complexity ------ 

3 approaches

Non-optimal ()

Loop through the characters string.
Count how many times the char occurs in thedocument string.
Then count how many times it occurs in the chars string.
and see if the counts are greater than or equal to the amount of document characters. 

Approach 2 same as before but we make a set called counted . Once we count a char we add it to our set. 

Solution 3  - Time:O(M+n), Space: O(c), Where m in doc length, n is chars string.

Loop through count every char. Use a chache to store the counts of the values. In python a dict.
Then loop through the document and subtract each value from the cache. IF we don't have enough , we cannot make the string and will return False. 

------ Recursive Formula ------

------ Iterative Approach ------

"""
## Solution 1 - Least optimal Time:O(m(n*m)), Space: O(1)
def generateDocument(characters, document):
    for character in document:
        documentFrequency = countCharacterFrequency(character, document)
        charactersFrequency = countCharacterFrequency(character,characters)
        if documentFrequency > charactersFrequency:
            return False
    return True

def countCharacterFrequency(character, target):
    '''
    In python we could also use 'document.count(character)' but this is still O(n) time.
    This function counts the frequency of chars in a string
    '''
    frequency = 0
    for char in target:
        if char == character:
            frequency += 1
    return frequency



##----------------------
## Solution 2 - Time:O(c(n*m)), Space: O(c) - c= unique chars in the document.
def generateDocument(characters, document):
    alreadycounted = set()
    for character in document:
        if character in alreadycounted:
            continue                    # save time, don't cunt and move on to the next character.

        documentFrequency = countCharacterFrequency(character, document)
        charactersFrequency = countCharacterFrequency(character,characters)
        if documentFrequency > charactersFrequency:
            return False
        alreadycounted.add(character)

    return True

def countCharacterFrequency(character, target):
    '''
   helper func as above
    '''
    frequency = 0
    for char in target:
        if char == character:
            frequency += 1
    return frequency


## Solution 2 - Optimal - Time:O(n + m), Space: O(c) - c= unique chars in the characters.
def generateDocument(characters, document):
    characterCounts = {}                        # this will be our cache

    for character in characters:
        if character not in characterCounts:
            characterCounts[character] = 0      # pythonic way to initialise defult values in a dictionary
        
        characterCounts[character] += 1         # if it exists , add another one.

    for character in document:
        if character not in characterCounts or characterCounts[character] == 0:
            return False
	    
        characterCounts[character] -= 1
		
	return True