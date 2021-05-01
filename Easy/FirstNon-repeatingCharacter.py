"""
----- NAME: First non-repeating character -----
----- Category: Strings -----
----- Level : East  -----
------ BRIEF ------

Write a function that takes in a string of lowercase English alphabet letters and
returns the index of the strings first non-repeating character.

The first nonrepeating character is the first character in the string that occurs only once.

If the input string doesn't have any non-repeating characters, your function should return -1.


------ Hints ------

- How can you determine if the character only appears once in the entire input string?
What would be the brute force approach to solve this problem?

- One way to solve this problem is with nested traverse use of the string: you start by traversing the string, and for each character that you traverse,
 you traverse through the entire stream again to see if the character appears anywhere else. 
The first index which you find a character that doesn't appear anywhere else in the string is the index that you return. 
This approach works, but it is not optimal. Are there any data structures that you can use to improve the time complexity of this approach?

- Hash tables are very commonly used to keep track of frequencies.
Build a hash table, where every key is a character in the string and every value is the corresponding characters frequency in the input string.
You can reverse the entire string wants to fill the hash table and then with a second reversal through the string (not a nested reversal), 
you can use the hashtag was constant time lookups to find the first character with a frequency of 1.

------ Complexity ------ 
Time: O() 
Space: O()

------ Approach ------

"""

####################################################
## OPTIMAL
## Time: O(n) - Its 2n because we iterate twice ( 2 for loops)
## Space: O(26) - 26 for lower alphabet so constant time
####################################################

def firstNonRepeatingCharacter(string):
    characterFrequencies = {}

    for character in string:
        # build the hash map. Default char to 0 if never seen else, + 1
        characterFrequencies[character] = characterFrequencies.get(character, 0) + 1

    for idx in range(len(string)):
        character = string[idx]
        if characterFrequencies[character] == 1:            # As soon as we find a char that only has one instance
            return idx
        
    return -1

####################################################
## BRUTE FORCE
## Time: O(n^2) - slow; where n is 
## Space: O(1) - no extra space needed
####################################################

def firstNonRepeatingCharacter(string):
    
    # find the first non-repeating char
    for idx in range(len(string)):
        foundDuplicate = False

        # inner traversal to find a duplicate
        for idx2 in range(len(string)):
            if string[idx] == string[idx2] and idx != idx2:
                foundDuplicate = True
            
        if not foundDuplicate:
            return idx
        
    return -1


