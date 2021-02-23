"""
----- Run-Length Encoding : Easy -----
------ BRIEF ------
Write a function that takes in a non-empty string and returns its run-length encodeing. 


Wikipedia defines RLE as - "a form of lossless data compression in which runs of data (sequences in which the same data value occurs in many consecutive data elements)
are stored as a single data value and count, rather than as the original run."
For this problem , a run of data is any sequence of consecutive, identical characters. So the run "AAA" would be run-length-encoded as "3A".

This is lossless because we can get back the same data back as we put in. 

To make things more complicated , however, the input string can contain all sorts of special characters, includeing numbers.
Since encoded data must be decodable, this means tha we can't naively run-length-encode long runs. For example, the run "AAAAAAAAAAAA" (112 A's), 
can't naively be encoded as "12A", since this string can be decoded as either "AAAAAAAAAAAA" or "1AA". 
Thus, Long runs (runs of 10 or more characters) should be encoded in a split fashion; the aforementioned run should be encoded as "9A3A".
------ Hints ------


------ Complexity ------ 


------ Recursive Formula ------

------ Iterative Approach ------

"""
## O(n) Time \ O(n) space
def runLineEncoding(string):
    encodedStringCharacters = []                                                # this will store the chars for the encoded OP string
    currentRunLength = 1

    for i in range(1, len(string)):                                             # starting at 1 so we can count back by 1 at the start
        currentCharacter = string [i]                                           
        previousCharacter = string[i-1]                                         # because we start at index 1, in a zero indexed language.    

        if currentCharacter != previousCharacter or currentRunLength == 9:      #     
            encodedStringCharacters.append(str(currentRunLength))
            encodedStringCharacters.append(previousCharacter)                   # this is the end of the rn we have just found
            currentRunLength = 0                                                # reset the run length to zero because whatever happens , we will be adding 1 to the run length.

        currentRunLength +=1                                                    # either resetting or adding one, this does that actual counting of same chars

    encodedStringCharacters.append(str(currentRunLength))
    encodedStringCharacters.append(string[len(string) - 1])

    return "".join(encodedStringCharacters)