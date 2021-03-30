"""
----- NAME: Generate Div Tags -----
----- Category: Recursion -----
----- Level : Hard -----
# Has a recursive solution 
------ BRIEF ------

Write a function that takes in positive integer numberOfTags and returns a list of all the valid strings that 
you can generate with that number of matched "<div></div>" tags.

A string is valid and contains matched <div></div> tags if for every opening tag <div>, there is a closing tag <div> that
comes after the opening tag and that isn't used as a closing tag for another opening tag.

Each output string should contain exactly numberOfTags opening tags and numberOfTags closeing tags. 

For example, given numberOfTags = 2, valid strings to return would be:
["<div></div><div></div>","<div></div><div></div>"].

Note the the output strings don't need to be in any particular order.

------ Hints ------
- The brute force approach to solve this problem is to generate every single possible string it contains a numberOfTags tags and to then check all of those strange to see if they are valid. 
Can you think of a better solution?

- To solve this problem optimally, you'll have to incremental E build valid strings by adding <div> and </div> tags tp already valid partial strings.
While doing this, you can avoid creating strings that will never lead to a valid final string by following two rules:
1. If a string has fewer opening tags the numberOfTags, it's valid to add an opening tag to the end of it.
2. If a string has fewer closing tags than opening tags, it's valid to add a closing tax to the end of it.

- Using the roles defined above, write a recursive algorithm to generate all possible value strings, 
you'll need to keep track of how many opening and closing tags each string has available (at recursive call),
and you'll simply follow the rules outlined above. Once a string has no more opening and closing tax available,
You can add it to your final list of strings. The first called to the function will start with an empty string as the partial string and
 with a numberOfTags as the number of opening and closing tags available.
 For example, after you had an opening tag to a partial string, your recursively cool the function.

"""

####################################################
## Time: O((2n)!/(n!((n+1)!)))) this is an approximate , catalan formula
## Space: O((2n)!/(n!((n+1)!)))) 
####################################################

def generateDivTags(numberOfTags):
    matchedDivTags = []
    generateDivTagsFromPrefix(
        numberOfTags, numberOfTags, "", matchedDivTags)
    return matchedDivTags

def generateDivTagsFromPrefix(openingTagsNeeded, closeingTagsNeeded, prefix, result):
    if openingTagsNeeded > 0:
        newPrefix = prefix + "<div>"
        generateDivTagsFromPrefix(openingTagsNeeded - 1, closeingTagsNeeded, newPrefix, result)
    
    if openingTagsNeeded < closeingTagsNeeded:
        newPrefix = prefix + "</div>"
        generateDivTagsFromPrefix(openingTagsNeeded, closeingTagsNeeded  - 1, newPrefix, result)

    if closeingTagsNeeded == 0:
        result.append(prefix)