"""
----- Caesar Cipher Encryption : Easy -----
------ BRIEF ------
Given a non-empty string of lowercase letters and non-negative integer representing a key, 
write a function that returns a new string obtained by shifting every letter in the input string by k position's in the alphabet,
where k is the key. note that letters should "wrap" around the alphabet; in other words the letter 'z' shifted by one returns the letter 'a'.

------ Hints ------
- Most language have a built-in functions that give you the Unicode value of a character as well as the character corresponding to a Unicode value. 
Consider using such functions to determine which letters the input string's letters should be mapped to.

- Try createing your own mapping of letters to codes, In other words, 
try associating each letter in the alphabet with a specific number - its position in the alphabet, 
for instance - and using that to determine which letters the input string's letters should be mapped to. 

- How do you handle cases where a letter gets shifted to a position that requires wrapping around the alphabet?
What about cases where the key is very large and causes multiple wrappings around the alphabet ?
The modulo operator should be your frined here.

------ Complexity ------ 
Time = O(n) , where n is the length of the string. However, if we are useing an alphabet array approach, it would be O(m) where m is the length of the alphabet.
Space = O(n), 

------ Approach ------

ord(z) 122
ord(1) 97

create an "NLC = ord(letter + key)" , to get the alphabetic wrapp around , we need to use the modulo operator 
if NLC <= 122:
    retutn chr(NLC)
else: 
    return chr(96 + NLC % 122) # this doesnt cover the edge case where the key if for a large number 



Notes
For Solution 2 of this problem, in the video explanation, we update the newLetterCode with the following formula if it's greater than 25:

-1 + newLetterCode % 25

This logic is actually flawed, because if newLetterCode % 25 happens to be equal to 0, 
then we'll be accessing a letter in the alphabet at index -1,
which will throw an error in a lot of languages or simply return an incorrect answer in other languages.

For example, this edge-case issue will occur with these inputs:

string = "z"
key = 25

Instead, we need to use the following formula if the newLetterCode is greater than 25:

newLetterCode % 26

Why isn't this an issue in Solution 1? In Solution 1, our formula is:

96 + newLetterCode % 122

Since we only actually apply this formula if newLetterCode is greater than 122, 
and since the key that's used to initially compute newLetterCode is always less than 26 (because it's modded by 26 at the beginning of the algorithm), 
we know that newLetterCode % 122 will never be equal to 0 (newLetterCode will always be between 123 and 147).

Thus, we'll never compute a character from the char code 96, which would be equivalent to accessing a letter at index -1 in Solution 2. 



"""
###################################################
### First approach
###################################################
def caesarCipherEncryptor(string, key):
    newLetters = []
    newKey = key % 26
    for letter in string:
        newLetters.append(getNewLetter(letter,newKey))
    return "".join(newLetters)

def getNewLetter(letter, key):
    newLetterCode = ord(letter) + key
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)

###################################################
### 2nd approach
###################################################
def caesarCipherEncryptor(string, key):
    newLetters = []
    newKey = key % 26
    alphabet = list('abcdefghijklmnopqrstuvwxyz')                                               # this list and its use is what makes this different from the approach above
    for letter in string:
        newLetters.append(getNewLetter(letter,newKey, alphabet))                                # here
    return "".join(newLetters)

def getNewLetter(letter, key, alphabet):                                                        # here
    newLetterCode = alphabet.index(letter) + key                                                # here
    return alphabet[newLetterCode] if newLetterCode <= 25 else alphabet[newLetterCode % 26]     # here
