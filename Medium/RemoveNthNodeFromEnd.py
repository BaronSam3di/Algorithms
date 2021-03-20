"""
----- NAME: Remove Kth Node from end  -----
----- Category: Linked Lists -----
----- Level : Medium -----
------ BRIEF ------

Write a function that takes in the head of a Singly Linked list and an integer K and removes the Kth node from the end of the list.
The removal should be done in place, meaning that the original data structure should be mutated (no new structure should be created).

Furthermore, the input heads of the link list should remain the heads of the link list after the removal is done, 
even if the head is the need that supposed to be removed. 

In other words, if the head is the nose that supposed to be removed, your function should simply mutate its 'value' and 'next' pointer.

Note that your function doesn't need to return anything.

You can assume that the input Linked List will always have at least two nodes and, more specifically, at least K nodes. 

Each LinkList node has an integer value as well as the next node pointing to the next node in the list or to none/null if it's the tail of the list. 

------ Hints ------

- Since you are given a singly length list, you do not have access to any of the list nodes previous nodes. 
Thus, traversing the entire list and then counting K nodes back isn't an option.
Is there a way for you to traverse the entire list and to know which node is the Kth note from the end by the time 
you reach the final node in the list?

- Can you accomplish the task mentioned in the hint above By traversing the list all the while keeping track of two nodes at time. 
How could this work?

- Initialise two variables pointing to the first night in the list. Traverse K nodes in the list, 
updating the second variable at every night (that is, take K steps with the second variable).

Then, traverse the remainder of the list, this time updating both the second and the first variables 
(that is take as many steps with the first variable as the number of steps between the Kth node from the start and the end of the list).
Once you reach the end of the list, the first variable should point to the Kth from the end.

------ Complexity ------ 
Time: O(n) because you only traverse the length of the list. 
Space: O(1) - only keep track of s few pointers

------ Approach ------
The aimi is to remove the value at the nth index of the Linkedlist.
We initialise two pointers. One called F, for first pointer. One called S, for second pointer.
We then step S forward n indexes.
From here we step both pointers forward until S reaches a null value which will be at the end of the linklist.
We can count backwards from S to F.
We Direct the pointer of the value before F To now point to the value after F.
We can garbage collect the old value for n
Done.

"""

####################################################
## 
####################################################

def removeKthNodeFromEnd(head, k):
    counter = 1                         # initialise at 1 because we deliberately want to get beyond the length of the list
    first = head
    second = head
    while counter <= k:              
        second = second.next            # keep stepping through the node
        counter += 1
    if second is None:
        # edge case where you need to remove the head
        head.value = head.next.value    # Overwrite the value of the head node
        head.next = head.next.next      # Points to 2 values after it 
        return
    while second.next is not None:      # Until the second pointer itself will point to the final value.
        # ... The first pointer will be at the index we want to update 
        second = second.next
        first = first.next
    first.next = first.next.next        

