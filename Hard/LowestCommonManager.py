
"""
----- NAME: Lowest common manager -----
----- Category: Recursion -----
----- Level : Hard -----
# Has a recursive solution 

------ BRIEF ------
You're given three inputs, all of which are instances of an OrgChart class that
 have a directReports property pointing to their direct reports.

The first input is the top manager in an organisational chart (i.e., the only instance there is an anybody else's direct report),
And the other two inputs are reports in the organisational chart. The two reports are guaranteed to be distinct.

Write a function of return is the lowest common manager to the two reports.

------ Hints ------
- Given a random subtree in the organisational chart, the manager at the root of that subtree is common to any two reports in the subtree.

- The lowest common manager into reports in an organisational chart is the root of the lowest subtree containing those two reports. 
Find that low subtree to find the lowest common manager.

- To find the lowest subtree containing both of the input reports, try recursively traversing the organisational chart and keeping track of
 the number of those reports contained in each subtree as well as the lowest common manager any subtree.
Some subtrees might contain neither of the two reports, some might contain one of them, and others might contain both;
The 1st to contain both should return the lowest common manager for all the subtrees above it that contain it, including the entire organisational chart.

------ Complexity ------ 
Time: O() 
Space: O()

------ Recursive Approach ------

------ Iterative Approach ------

1. Starting at the top of the tree
2. get the info of the subtree and check for the direct reports.
3. keep going down adding the results, add return these up the chain.
"""

####################################################
## Time: O(n) - where n is the number of nodes(people) in the tree
## Space: O(D) - where d is the depth of the tree 
####################################################

def getLowestCommonManager(topManager, reportOne, reportTwo):
    return getOrgInfo(topManager, reportOne, reportTwo).lowestCommonManager

def getOrgInfo(manager, reportOne,reportTwo):                       # helper method that does the heavy lifting

    numImportantReports = 0                                         #  

    for directReport in manager.directReports:
        # recursive call
        orgInfo = getOrgInfo(directReport, reportOne, reportTwo)    # direct report becomes the new manager

        if orgInfo.lowestCommonManager is not None:
            return orgInfo
        numImportantReports += orgInfo.numImportantReports

    if manager == reportOne or manager == reportTwo:                # the manger could be the other report we are looking for.

        # base case of the recursive algorithm
        numImportantReports += 1
    lowestCommonManager = manager if numImportantReports == 2 else None 
    return OrgInfo(lowestCommonManager, numImportantReports)

# This is an input class. Do not edit.
class OrgInfo:                                                      # interface to declare for the Orginfo
    def __init__(self, lowestCommonManager, numImportantReports):
        self.lowestCommonManager = lowestCommonManager
        self.numImportantReports = numImportantReports

# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []