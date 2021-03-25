"""
----- Class Photos : easy -----
------ BRIEF ------
It's photo day at the local school, and you're the photographer assigned to take class photoes. 

The class that you'll be photographing has an even number of students, and all these students are wearing red or blue shirts. 
In fact, exactly half of the class is wearing red shirts and the other half is wearing blue shirts.
You're responsible for arraigning the students in two rows before taking the photo. 

Each row should contain the same number of students and should adhere to the following guidelines:
    - All Students wearing red shirts must be in the same row.
    - All Students wearing blue shirts must be in the same row.
    - Each student in the back row must be strictly taller than the student directly in front of them in the front row.

You're given two input arrays: 
- one containing the heights of all the students wth redshirts
- one contianing the heights of all the students with blue shirts. 

These arrays will always have the same length, and each height will be a positive integer. 
Write a function that returns weather or not a class photo that follows the stated guidelines can be taken.

Note: You can assume that each class has at least 2 students.
Reduce the problem: Start with a class of 4 people , 2 in the red shirt. two in the blue shirt. 
The tallest student of either row (and so their entire row) will need to be in the back row. 

------ Hints ------


------ Complexity ------ 
 Time: O(n log(n)) - need to sort both arrays 
 Space: O(1) - everything is done in place. Assumeing You can modify the input arrays

"""

def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse=True)             # reverse = True will sort in desending order, Tallest first
    blueShirtHeights.sort(reverse=True) 

    shirtColorInFrontRow = 'RED' if redShirtHeights[0] < blueShirtHeights[0] else 'BLUE'        # compare the tallest red vs blue to decide the front row
    for idx in range(len(redShirtHeights)):
        redShirtHeight = redShirtHeights[idx]
        blueShirtHeight = blueShirtHeights[idx]

        if shirtColorInFrontRow == 'RED':
            if redShirtHeight >= blueShirtHeight:
                return False
        else:
            if blueShirtHeight >= redShirtHeight:
                return False
    return True