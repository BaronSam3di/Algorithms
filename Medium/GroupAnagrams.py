"""
----- Group Anagrams : Medium -----
Write a function that takes in an array of strings and groups anagrams together.

anagrams are strings made up of exactly the same letters. where order doesn't matter. For example, "cinema" and "iceman" are anagrams; similarly, "foo" and "ofo" are anagrams.

Your unction should return a list of anagram groups in no particular order.


"""

####################################################
## Clunky 1st Solution O(w * n *log*n + n * w * log(w)) | Space: O(wn)
####################################################

def groupAnagrams(words):
    sortedWords = ["".join(sorted(w)) for w in words]       # sort the letters in each wo rd
    indices = [i for i in range(len(words))]                # create an array of indices

    indices.sort(key=lambda x: sortedWords[x])              # sort the indices according to the sorted words, which buckets the indices by anagram

    result = []
    currentAnagramGroup = []
    currentAnagram = sortedWords[indices[0]]


    '''
    because we have bucketed each Anagram next to each other we will keep track of 
    the anagram we are looking at and if we change anagram, we have found all of those anagrams
    '''

    for index in indices:                                   # run through the bucket based indices 
        word = words[index]                                 # current word is based on the index
        sortedWord = sortedWords[index]                     

        if sortedWord == currentAnagram:
            currentAnagramGroup.append(word)                # keep appending the matching word until it is difeeent
            continue

        result.append(currentAnagramGroup)                  # ...else make a new anagram group
        currentAnagram = [word]
        currentAnagram = sortedWord

    result.append(currentAnagramGroup)

    return result



####################################################
## Time: O(w * n *log*n) | Space: O(wn) 
####################################################

def groupAnagrams(words):
    anagrams = {}       
    for word in words:
        sortedWord = "".join(sorted(word))          # whats the sorted version of this word?
        if sortedWord in anagrams:                  
            anagrams[sortedWord].append(word)       # append the word tot he given list that corresponds to the anagram
        else:
            anagrams[sortedWord] = [word]           # otherwise declare a new array of the new word
    return list(anagrams.values())                  # return a list of the values of the dict . This contains the anagrams.
 