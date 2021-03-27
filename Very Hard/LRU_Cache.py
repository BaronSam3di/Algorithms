"""
----- NAME: LRU Cache -----
----- Category: Linked List -----
----- Level : very hard -----
------ BRIEF ------


Implement and LRUCache class for at least recently used cache. The class should support:
 - Inserting key-value pairs with the `insertKeyValuePair` method.
 - Retrieving a key is value with the `getValueFromKey` method
 - Retrieving the most recently used (the most recently inserted or retrieved) 
   key with the get most recent key method.

Each of the message should run in constant time.

Additionally, the LRUCache class should store a maxSize Property set to the size of the cache, 
which is passed in as an argument during instantiation. 
This size represents the maximum number of key-value pairs the cash can store at once.
If a key-value pair is inserted in the cash when it has reached maximum capacity, the least recently used key-value pair should be evicted from the cash and no longer retrievable;
 the newly added cache in value they should effectively replace it.

Note that inserting a key-value pair with an already existing key should simply replace the key's value in the cache with the new value and shouldn't evict a key-value pair if the cash is full. 

------ Hints ------

- What data structure can allow you into insert, retrieve, and if it's resources as fast as possible, 
all the while keeping track of the least recently accessed resource - essentially keeping track of the order of the resources?
A hash table would allow you to insert and retrieve resources fast, but it wouldn't allow you to keep track of their order. 
An array would let you keep track of their order, but it wouldn't let you access elements fast; 
It's also wouldn't allow you to move an element from one position to another in constant time, 
which he would need to do to make a newly-access to key/value per the most recent one upon retrieval of the key's value.
A linked list would allow you to keep track of elements order and to move them seriously (if you knew their position), 
but it wouldn't allow you to access them easily without knowing their position beforehand. 
Could I heap help? What about a BST ir tree? With any other data structures work.

- Could use multiple data structures to make your LRUCaches functionality fast and efficient?
Could you store keys in one data structure, for instance, and values in an auxiliary data structure?
What should these data structures be in order for all of the L are you caches methods to run in constant time? 

- Try storing keys in a hash table and mapping them to nodes in a doubly link to list containing the keys corresponding values (perhaps the notes would also have to store the keys themselves). 
With these two data structures, you could access any key/value pair very easily via the hash table, 
and you could also effortlessly move nodes in the linked list so as to keep track of the most recent and least recent key / value pairs.
The link list would also allow you to keep track of the entire order of the key/value pairs, that's allowing you to actually update the least recent key/value pairs after evictions.

Notes: 
- Combine data structures
- every method in the class will be generally moving pointers around
------ Complexity ------ 
Time: O() 
Space: O()

------ Recursive Approach ------

------ Iterative Approach ------

"""

####################################################
## Time: O(1) - where n is 
## Space: O(1) - 
####################################################

class LRUCache:
    def __init__(self, maxSize):
        self.cache = {}
        self.maxSize = maxSize or 1
        self.currentSize = 0
        self.listOfMostRecent = DoublyLinkedList()


    def insertKeyValuePair(self, key, value):
        if key not in self.cache:
            if self.currentSize == self.maxSize:
                    self.evictLeastResent()
            else:
                    self.currentSize += 1
            self.cache[key] = DoublyLinkedListNode(key, value)
        else:
                self.replaceKey(key,value)
        self.updateMostRecent(self.cache[key])


    def getValueFromKey(self, key):
        if key not in self.cache:
              return None
        self.updateMostRecent(self.cache[key])
        return self.cache[key].value


    def getMostRecentKey(self):
        if self.listOfMostRecent.head is None:
            return None
        return self.listOfMostRecent.head.key 
    
    def evictLeastResent(self):
        keyToRemove = self.listOfMostRecent.tail.key
        self.listOfMostRecent.removeTail()
        del self.cache[keyToRemove]
    
    def updateMostRecent(self, node):
          self.listOfMostRecent.setHeadTo(node)

    def replaceKey(self, key, value):
        if key not in self.cache:
              raise Exception("The Provided key is not in the cache")
        self.cache[key].value = value
		
		
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # O(1) Time | O(1) space
    def setHeadTo(self, node):
        if self.head == node:
            return
        elif self.head is None:
            self.head = node
            self.tail = node
        elif self.head is self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail
        else:
            if self.tail == node:
                self.removeTail()
            node.removeBindings()
            self.head.prev = node
            node.next = self.head
            self.head = node
            
    def removeTail(self):
        if self.tail is None:
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None
    
    # O(1) Time | O(1) space
    def setTail(self, node):
        if self.tail is None:
            self.setHeadTo(node)
            return
        self.insertAfter(self.tail, node)

    # O(1) Time | O(1) space
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev                       # needs setting before it is overwrittern
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    # O(1) Time | O(1) space
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node                       # needs setting before it is overwrittern
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert
    
    # O(p) Time | O(1) space - where p is the position value
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHeadTo(nodeToInsert)
            return
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)
    
    # O(n) Time | O(1) space
    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)
 
    
    # O(1) Time | O(1) space
    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removeNodeBindings(node)
        
    # O(n) Time | O(1) space
    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None

    # helper method
    def removeNodeBindings(self, node):
        # the order of these function is important
        if node.prev is not None:
            # Needs to happen first to update the previous nodes next before we loose node.prev
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

class DoublyLinkedListNode:
    def __init__(self,key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def removeBindings(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
        self.prev = None
        self.next = None