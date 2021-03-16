"""
----- NAME: Dijkstra's Algorithm -----
----- Category: Famous Algorithms -----
----- Level : Hard -----

------ BRIEF ------

Dijkstra's Algorithm - A path finding Algorithm. How to find the "cheapest" route to a "destination" . 
It can be used on directed, undirected, weighted, unweighted graphs. Negative weights will change the problem allot.





You're given an integer "start" and a list "edges" of pairs of integers. 

This list is what's called an adjacency list, and it represents a graph. 
The number of vertices in the graph is equal to the length of edges, where each i in edges contains vertex i's outbound edges, 
in no particular order. 
Each individual edge is represented by a pair of two numbers, [destination, distance] where the destination is a positive integers denoting the destination 
vertex and the distance is a positive integer representing the length of the edge (the distance from vertex i to vertex "destination"). 
Note that these edges are directed, meaning that you can only travel from a particular vertex to its destination - not the 
other way around (unless the destination vertex itself has an outbound edge to the original vertex).

Write a function that computes the lengths of the shortest paths between "start" and all of the other vertices in the graph using Dijkstra's Algorithm and returns them in an array.
Each index i in the output array should represent the length of the shortest path between "start" and vertex"i". 
If no path is found from "start" ot vertex i, then output[i] should -1.

Note that the graph represented by edges won't contain any self-loops (vertices that have an outbound edge to themselves) and will only have positively weighed edges (ie, no negative distances).





------ Hints ------


------ Complexity ------ 


------ Approach ------

Use an "adjacency ;ist" which will list all the nodes that can be reached from a certain node.
Dijkstra's Algorithm will keep track of what it has already seen, making it much more efficient. Start by looking at the nodes that have the shortest distance and add this into your cache.  

"""

####################################################
## Non-optimal approach useing a list
## Time: O(v^2 + e) | Space: O(v)
##  where v is the number of vertices and e is the number of edges
####################################################

def dijkstrasAlgorithm(start, edges):
    numberOfVertices = len(edges)
    minDistances =  [float('inf') for _ in range(numberOfVertices)]
    minDistances[start] = 0

    visited = set()
    while len(visited) != numberOfVertices:
        vertex, currentMinDistance = getVertexWithMinDistance(minDistances, visited)
        if currentMinDistance == float('inf'):
            break

        visited.add(vertex)

        for edge in edges[vertex]:
            destination, distanceToDestination = edge

            if destination in visited:
                continue

            newPathDistance = currentMinDistance + distanceToDestination
            currentDestinationDistance = minDistances[destination]
            if newPathDistance < currentDestinationDistance:
                minDistances[destination] = newPathDistance
    
    return list(map(lambda x: -1 if x == float('inf') else x, minDistances ))

def getVertexWithMinDistance(distances, visited):
    currentMinDistance = float('inf')
    vertex = None 

    for vertexIdx, distance in enumerate(distances):
        if vertexIdx in visited:
            continue
        if distance <= currentMinDistance:
            vertex = vertexIdx
            currentMinDistance = distance
    
    return vertex, currentMinDistance

####################################################
## approach useing a heap - see Min-Heap Construction - https://www.algoexpert.io/questions/Min%20Heap%20Construction
## Time: O(v^2 + e) | Space: O(v)
##  where v is the number of vertices and e is the number of edges
## Note: requires heap implimentation to work - : MinHeap
####################################################

def dijkstrasAlgorithm(start, edges):
    numberOfVertices = len(edges)
    minDistances =  [float('inf') for _ in range(numberOfVertices)]
    minDistances[start] = 0
    
    minDistancesHeap = MinHeap([(idx, fliat('inf') for idx in range(numberOfVertices))])
    minDistancesHeap.update(start,0)

    visited = set()
    while len(visited) != numberOfVertices:                    # v time
        vertex, currentMinDistance = minDistancesHeap.remove() # Log(v) time
        
        if vertex in visited:
            continue

        if currentMinDistance == float('inf'):
            break

        visited.add(vertex)

        for edge in edges[vertex]:
            destination, distanceToDestination = edge

            if destination in visited:
                continue

            newPathDistance = currentMinDistance + distanceToDestination
            currentDestinationDistance = minDistances[destination]
            if newPathDistance < currentDestinationDistance:
                minDistances[destination] = newPathDistance
                minDistancesHeap.update(destination, newPathDistance)
    
    return list(map(lambda x: -1 if x == float('inf') else x, minDistances ))

def getVertexWithMinDistance(distances, visited):
    currentMinDistance = float('inf')
    vertex = None 

    for vertexIdx, distance in enumerate(distances):
        if vertexIdx in visited:
            continue
        if distance <= currentMinDistance:
            vertex = vertexIdx
            currentMinDistance = distance
    
    return vertex, currentMinDistance


####################################################
## 
####################################################
