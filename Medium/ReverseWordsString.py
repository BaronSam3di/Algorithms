"""
----- Reverse Words In String : Medium -----
------ BRIEF ------
Write a function that takes in a string of words separated by one or more whitespaces 
and returns a string that has these words in reverse order. 

For example, given the string " tim is great", your function should return "great is tim".

For this problems, a word can contain special characters, punctuation, and numbers. the word in the string will be seperated by one or more whitespaces,
and the reversed string must contain the same whitespaces as the original string. For example. given the string "whitespaces 4",
you would be expected to return "4 whitespaces".

Note: you are not allowed to use any built-in split or reverse methids/functions. However, you are allowed to use a built-in `join` method/function.

------ Hints ------
- Maybe consider useing an underscore to replace the white space becasue in a harder problem there could be more that 1 whitespace between whitespace.

------ Complexity ------ 


------ Approach ------

- Another approach is to to read in the strting in reverses, and then for each word in a list, read that in reverse
turning the string around."


I didn't like their solution as much as mine. 

"""

####################################################
## Time and Space: O(n)
####################################################
# Submission 1 
def reverseWordsInString(string):
    # not allowed to use any built-in split or reverse methids/functions.
	# you are allowed to use a built-in `join` method/function.
	wordsList = []
	tmpString = ""
	for item in string:
		if item != " ":
			tmpString += item
		if item == " ":
			wordsList.insert(0,tmpString)
			tmpString = ""
	wordsList.insert(0,tmpString)
    return " ".join(wordsList)


