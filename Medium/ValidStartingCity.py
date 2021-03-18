"""
----- NAME: Valid Starting City -----
----- Category: Greedy Algorthms -----
----- Level : Medium -----
------ BRIEF ------

Imagine you have a set of cities are laid out in a circle, connected by a circular road that runs clockwise.
Each city has a gas station that provides gallons of fuel, and each city is some distance away from the next city.

Do you have a car that can drive some number of miles per gallon of fuel, and your goal is to pick 
a starting city such that you can fill up your car with that city's fuel, drive to the next city, re-fill up your car with that city's fuel, and 
so on and so forth until you return back to the starting city with 0 or more gallons of fuel left.

The city is called a valid starting city, and its guarantee that there will always be exactly one valid starting city.

For the actual problem, you'll be given 
- an array of distances such that city i is distance[i] away from city [i + 1].
- an array of fuel we can collect at each city ( this will be the same length as the distances)
- and an mpg value for your car


Since the cities are connected via a circular Road, the last city is connected to the first city. In other words, 
the last distance in the distances array is equal to the distance from the last city to the first city. 
You'll also be given an array of fuel available at each city, where fuel[i] is equal to the fuel available city i. 
The total amount of fuel available (from all cities combined) is exactly enough to travel to all cities. 

Your fuel tank always starts out empty, and you're given a positive integer value for the number of miles that your car
can travel per gallon of fuel (mile per gallon, or mpg). You can assume that you will always be given at least two cities.

Right to function returns the index of the valid starting city.

Note: the fuel will always match the distances.

------ Hints ------
 

------ Complexity ------ 


------ Recursive Formula ------

------ Iterative Approach ------

"""

####################################################
## Optimal Approach: O(n) time | O(1) space - where n is the number of cities
####################################################

def validStartingCity(distances, fuel, mpg):
    numberOfCities = len(distances)
    milesRemaining = 0

    indexOfStartingCityCandidate = 0
    milesRemainingAtStartingCityCandidate = 0

    for cityIdx in range(1, numberOfCities):
        distanceFromPreviousCity = distances[cityIdx - 1]
        fuelFromPreviousCity = fuel[cityIdx - 1]
        milesRemaining += fuelFromPreviousCity * mpg - distanceFromPreviousCity

        if milesRemaining < milesRemainingAtStartingCityCandidate:
            milesRemainingAtStartingCityCandidate = milesRemaining
            indexOfStartingCityCandidate = cityIdx

    return indexOfStartingCityCandidate


####################################################
## Brute force Approach: O(n^2) time | O(1) space - where n is the number of cities
####################################################

def validStartingCity(distances, fuel, mpg):
    numberOfCities = len(distances)

    # pick a starting city
    for startCityIdx in range(numberOfCities):
        milesRemaining = 0

        # iterate through remianing cities    
        for currentCityIdx in range(startCityIdx, startCityIdx + numberOfCities):
            if milesRemaining < 0:
                continue                                                            # if we have run out of fuel, skip

            currentCityIdx = currentCityIdx % numberOfCities    

            fuelFromCurrentCity = fuel[currentCityIdx]                              # 
            distanceToNextCity = distances[currentCityIdx]
            milesRemaining += fuelFromCurrentCity * mpg - distanceToNextCity        #

        if milesRemaining >= 0:
            return startCityIdx

    # This line should never be reached if the inputs are correct.
    return -1