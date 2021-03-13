"""
----- NAME: Phone Number Mnemonics -----
----- Category: Recursion -----
----- Level : Medium -----
------ BRIEF ------

Your phone keypad will likely look like this.

-------------------------
|       |  ABC  |  DEF  |
|   1   |   2   |   3   |
-------------------------
|  GHI  |  JKL  |  MNO  |
|   4   |   5   |   6   |
-------------------------
| PQRS  |  TUV  | WXYZ  |
|   7   |   8   |   9   |
-------------------------
|       |       |       |
|   *   |   0   |   #   |
-------------------------

Almost every every digit is associated with some letters in the alphabet;
this allows certain phone numbers to spell out actual words.
For example, the phone number `2686463` can be written as antoine or as `ant6463`.

It's important to note that a phone number doesn't represent a single sequence of letters, 
but rather multiple combinations of letters, For instance, the digit 2 can represent three different letters (a,b and c).

A mnemonic is defined as a pattern of letters, ideas, or associations that assist in remembering something.
Companies often times use a mnemonic for their phone number to make it easier to remember. 

Given a stringified phone number of any non-zero length, write a function that returns all valid mnemonics for this phone number,in any order.
So given "1905" come up with a list based on all the combination of mnemonics that could be generated.

Notes: 1 or 0 will remain as 1 or 0.

For this problem, a valid mnemonic may only contain letters and the digits 0 and 1. In other words, if a digit is able t obe represented by a letter, then it must be. 
Digits 0 and 1 are the only two digits that don't have letter representations on the keypad.

Note that you should rely on the keypad illustrated above for digit-letter associations. 

------ Hints ------


------ Complexity ------ 
Time: O(4^n * n) - worst case is a a number full of 4 char numbers (9,7).

------ Approach ------

Define a dictionary with key values eg 2 : [a,b,c].
Define a list of hte Mnemonic results.

recursivepickchar(idx) 

"""

####################################################
# O(4^n * n) time | O(4^n * n) Space
def phoneNumberMnemonics(phoneNumber):
    currentMnemonic = ['0'] * len(phoneNumber)
    mnemonicsFound = []

    phoneNumberMnemonicsHelper( 0, phoneNumber, currentMnemonic, mnemonicsFound)
    return mnemonicsFound

def phoneNumberMnemonicsHelper( idx, phoneNumber, currentMnemonic, mnemonicsFound): 
    if idx == len(phoneNumber):  
        # base case                                        # we are at the end of the phonenumber
        mnemonic = ''.join(currentMnemonic) 				# O(n) time
        mnemonicsFound.append(mnemonic)
    else:
        # not the base case 
        digit = phoneNumber[idx]                                       # get the current digit
        letters = DIGIT_LETTERS[digit]                              # gives us all the chars that represent the digit
        for letter in letters:
            currentMnemonic[idx] = letter                           # the choice made at this step
            phoneNumberMnemonicsHelper( idx + 1, phoneNumber, currentMnemonic, mnemonicsFound)    # recursive call at the next index 

DIGIT_LETTERS = {
    "0":["0"],
    "1":["1"],
    "2":["a","b","c"],
    "3":["d","e","f"],
    "4":["g","h","i"],
    "5":["j","k","l"],
    "6":["m","n","o"],
    "7":["p","q","r","s"],
    "8":["t","u","v"],
    "9":["w","x","y","z"],
}
