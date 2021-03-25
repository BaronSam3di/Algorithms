"""
----- Product Sum : Easy -----

# Has a recursive solution 

------ BRIEF ------

-- A classic recursion question--
Write a function tht takes in a "special" array and returns tis product sum.
A "special" array is a non-empty array that contains either integers o other "special" arrays. 
The product of a "special array is the sum of its elements, where "special" arrays inside it are 
summed themselves and then multiplied by their level of depth.

The depth of a special array is how far nested it is. For instance, the depth if []  is 1; 
the depth of the innter array in [[]] is 2; the depth of the innermost array in [[[]]] is 3.
therefore, the product sum of [x,y] is x + y; the product sum of [x,[y,z]] is 'x + 2 * (y + z)';
 the product of [x,[y, [z]]] is 'x+2 * (y + 3z)'.

------ Hints ------
- if a "special" array can contain "special" arrays, this is recursive. Try using recursion to solve the problem.

- Initialize the product Sum of the "special arrrya to 0. 
Then , iterate through hall of the array's elements; if you come across a number, add it ot the product sum; 
if you come accross another "special" array, recursively call the productSum function on it and add the return value to the product sum. 
How will you handle multiplying the product sums at a given level of depth. 

------ Approach ------ 
Initialize the Sum to 0
step through the array from left to right, and start adding the items. 
IF you have a number you add it to the sum which is initialised to zero at the beginning of the recursive call. 
IF you come to a special arrya, you call the function on that array and add 1 to the multiplier that you pass and use your current multiplier plus 1. 
Add the sum you get from that call to the sum and return it multiplied by the multiplier.

When you get to a special array " if our element is an array, add to the su the product sum of the special array" 
WE would alsos need to initialise a multiplier to represent he depth we are in.

To summerise: 
------ Recursive Formula ------
Time: O(N) - where N is the total number of elements on all arrays , so if you have arrays in arrays, you count the arrays and the element in them. 
Space: O(D) - where D is the highest depth of the sub arrays.

------ Iterative Approach ------

"""

def productSum(array, multiplier = 1):
    sum = 0
    for element in array:
        if type(element) is list: #
            sum += productSum(element, multiplier + 1)
        else:
            sum += element
    return sum * multiplier

