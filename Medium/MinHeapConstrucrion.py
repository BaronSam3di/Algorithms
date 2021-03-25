"""
----- NAME: Min Heap Construction  -----
----- Category: Heaps -----
----- Level : Medium -----
------ BRIEF ------
Implement a Minheap class that supports :
    - Building a Min HEap from an unsorted input array of integers.              
    - inserting integers in the heap.
    - removing the heap's minimum / root value.
    - peeking the heap's minimum / root value.
    - sifting integers up and down the heap, which is to be used when intersin and removeing.

Note that the heap should be represented in the form of an array.

A Heap/binary heap is a Binary tree with the added properties of:
    - "Completness" - each level should be full, apart from the last which you fill up from the left.
    - The heap property: every nodes value in the heap will be smaller than its children's nodes value.

------ NOTES ------
Important to note that heap is in no way sorted. Infact the smallest value in he heap will be at the root, hence the name - MinHeap. 
A MaxHeap would have the highest value in the root.

With a representation of heap in an array, to find the position two children  of a given node; you take the index of the given node (i). 
You take the first child node you do 2i+1. To get the 2nd child node you do 2i+2.

Parent nodes can be found by floor(i-1/2).


The core methods of the heap will be 
- Build heap - takes an unsorted array and builds a heap - Time: O(n) - 
- Sift up - move a value up to its correct position - Time: O(log(n)) because we always eliminate half the tree each time
- Sift down - move a value down to its correct position. Bit more involved than sift up. - Time: O(log(n)) because we always eliminate half the tree each time
- Insert - add a node(value) in the heap
- remove - del a node(value) in the heap . The easiest value you can remove is the root.  
- peek - return the value of the root


"""

####################################################

class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2                                          # this is -2 because you want the final index( in python -1) and then - 1 again
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    def siftDown(self, currentIdx, endIdx, heap ):
        childOneIDx = currentIdx * 2 + 1
        # switching "<" to ">" on L63 & L67 will make a MaxHeap 
        while childOneIDx <= endIdx:                                                     # we only want to sift on nodes that are not leaves
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else - 1
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIDx]:              # if we have a 2nd child node thats not -1 AND the value of child is the smallest 
                idxToSwap = childTwoIdx                                                  # the child we need to swap is 
            else:
                idxToSwap = childOneIDx
            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIDx = currentIdx * 2 + 1                                         # update for the while loops
            else:
                return


    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1 ) // 2
        # switching below "<" to ">" will make a MaxHeap 
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:    # while we are not at the top of the heap AND current node is smaller than its parent ( out of position for a miniHeap)
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx                                      # now the node we want to sift up is in the parentIDx
            parentIdx = (currentIdx -1 ) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        self.swap(0, len(self.heap) -1, self.heap)                # swap the root with the last value 
        valueToRemove = self.heap.pop()                     # pop the new end value (old root value)
        self.siftDown(0,len(self.heap) -1 , self.heap)
        return valueToRemove                                

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) -1 , self.heap)

    def swap(self, i, j, heap):
        heap[i] , heap[j] = heap[j], heap[i]