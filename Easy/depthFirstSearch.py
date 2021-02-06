"""
----- Depth First Search : Easy -----

------ BRIEF ------

Depth First search is the sibling of Breadth first search.

The graph will be a tre like DS with a bunch of nodes having a name(value)and maybe some children nodes.  

You are given a Node class that has a name and an array of optional children nodes.
When put together , nodes form a acyclic tree-like structure. (See: https://mathworld.wolfram.com/AcyclicGraph.html)

Implement the depthfirstSearch method on the Node class, which 
- takes in an empty array, 
- traverses the tree using the depth-first Search approach (specifically navigateing te tree from let to right), 
- stores all of the nodes' names in the input array,
- returns the array.

How does it work? 

As the name suggests , we go deep first, so we explore all the way down before we move laterally.
We can call the function recursively at each node. 
When were are at a given node, we will add that nodes name to the final array, then for every child in tis children node, 
we will call the depth first search function and pass in the final array.

------ Hints ------
The Depth first algorithm works by traverseing a graph branch by banach . 
In orther words, before traverseing any Node's sibling Nodes, Its children nodes must be traversed. 
How can you simply and effectively keep track of Nodes' siblings Nodes as you traverses them, 
all the while retaining the order in which you must traverse them?

Start at the root Node and try simply calling the depthFirstSearch method on all of its children Nodes. 
Then, call the depthFirstSearch method on all children Nodes of each child node. 
Keep applying this logic until the entire graph has been traversed.
Don't forget to add the current node's name to the input array at every ca of depthFirstSearch.

------ Complexity ------ 
Space: O(v) :we are storeing an array of each node, but also Think about adding the frames to call a stack when we call this function.
We could be running DFS in a complete linear way on as many nodes as there are on the graph because it could be a line of nodes. eg: each node only has 1 child. 
The function will not resolve until its last child node has returned,


Time: O(v + e)  where v is the number of vertices (nodes) of the input graph and e is the number of edges (connections) of the input graph.

------ Recursive Formula ------

------ Iterative Approach ------


"""

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)       # for every child we call the DFS function and pass in the final array.
        return array
        