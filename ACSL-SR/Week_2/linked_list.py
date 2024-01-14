"""
Linked List

Name: <your name>
"""

"""
Linked List is a data structure that stores a collection of items.
Each item is connected to the next item through a link.
the "link" is actually just a pointer to the data location.
since this is a "reference type" Class

Linked List has two types of nodes:
    1. Head Node: The first node in the list
    2. Tail Node: The last node in the list
    
Each node contains two items:
    1. Data: The data that we want to store
    - The actual data included
    2. Next: The reference (pointer) to the next node in the list
    - It's literally just setting it as node.next = Node()
    - this works since Node is a Reference class. Reference class just stores a POINTER to the original
    - so self.next would be a NODE. it doesn't have an actual name, just data. it shows as "object at <memory address>"
    - but that isn't legible. so we would implement a function to show self.next's DATA
    
Linked List is a dynamic data structure, which means that it can grow and shrink at runtime by allocating and deallocating memory.
It means that we don't need to give the size of the linked list at the beginning.

Linked List is a linear data structure, which means that it can be traversed in one direction.
at least for singly linked lists (like this one)

Linked List has the following advantages over arrays:
    1. Dynamic size
    2. Ease of insertion/deletion
    
Linked List has the following methods:
    1. append(data): Add a node with the given data to the end of the linked list.
    2. insert(data, position): Insert a node with the given data at the given position.
    3. delete(data): Delete the first node with the given data.
    4. display(): Display the linked list.
    
Time Complexity:
    1. append(data): O(n)
    2. insert(data, position): O(n)
    3. delete(data): O(n)
    4. display(): O(n)
    
Space Complexity: O(n)
"""

#TODO:
#investigate why while True loop failed? (probably because of failed self.head transfer or smth)


class Node:
    """Class representing a node in a singly linked list."""
    # Already done by teacher!

    def __init__(self, data=None):
        """
        Initialize a node.

        Args:
            data: Data to be stored in the node. Defaults to None.
        """
        self.data = data
        self.next = None


class LinkedList:
    """Class representing a singly linked list."""

    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None
        #we make our own definition

    def append(self, data):
        """
        Add a node with the given data to the end of the linked list.

        Args:
            data: Data to be stored in the new node.
        """
        # hints
        # 1. create a new node with the data
        # 2. IF: the linked list is empty, set the head to the new node
        # 3. ELSE: traverse through the linked list until the last node
        # 4. set the next of the last node to the new (just added) node
        # Step 4 happens for every single appended item so it automatically overrides Node's initial None "next"
        # TODO: Write your code here

        new_node = Node(data)
        #so we have a temporary new name? I guess.

        if self.head is None:
            self.head = new_node
            #this just makes "self.head" reference to new_node
            #now self.head and new_node share a memory address. they are 2 references for the same memory address

        else:
            current_node = self.head #again, since Node is a reference data type, current_node will just POINT to self.head NOT make a copy
            # asked ChatGPT: it said that for reference types, multiple variables just have the same pointer to the SAME SHARED memory address.
            # in that memory address an object stored. in that object actually is the value.
            while current_node.next !=  None:
                current_node = current_node.next
            
            current_node.next = new_node

            #current_node just SHARES the SAME data memory spot with actual end
            #so setting current_node.next as new_node CHANGES the actual node too
            

    def insert(self, data, position):
        """
        Insert a node with the given data at the given position.

        Args:
            data: Data to be stored in the new node.
            position: Index where the new node should be inserted.
                      If position is out of range, the node is appended at the end.
        """
        # TODO: Write your code here
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            # in this case new_node.next's pointer is now pointing towards self.head's memory address
            self.head = new_node
            # now, the title of self.head is being transferred to new_node. self.head will now POINT towards new_node's memory address
        else:
            current_node = self.head
            before_node = self.head
            for index in range(position):
                #remember that position is 0-based too
                #so if position = 0, this for loop would NOT have happened. oh well

                #len of linked_list = 4. valid index vals: 0, 1, 2, 3, NONE
                #ex: position = 5. index vals: 0, 1, 2, 3, 4
                #ex: position = 2. index vals: 0, 1, 2. replace 2 then? and push 2 back
                if current_node.next == None:
                    #list index out of range failsafe
                    # so that current_node doesn't get assigned to "None"
                    # and it would stop at "3" and just run append
                    self.append(data)
                    return
                
                current_node = current_node.next
                #current_node ends as the node about to get replaced?

            for index in range(position-1):
                before_node = before_node.next
            new_node.next = current_node
            before_node.next = new_node
            


    def delete(self, data):
        """
        Delete the first node with the given data.

        Args:
            data: Data to be deleted from the linked list.
        """
        # TODO: Write your code here
        current_node = self.head
        before_node = self.head

        while current_node != None and current_node.data != data:
            #again, for 0-based and data 0-based MATCH!
            #print("does not match")
            print("current_node.data:",current_node.data)
            if current_node != self.head:
                #activates 1 turn after current_node
                #doesn't activate at all if current_node == self.head and returns
                print("before_node working")
                before_node = before_node.next
            current_node = current_node.next
            #print("updated current_node.next:",current_node.next.data)

        if current_node == None:
            return None
        
        if current_node.data == data:
            print("match")
            if current_node == self.head:
                print("current_node == self.head")
                self.head = current_node.next
                #current_node.next = self.head
                #I'm supposed to assign the dummy node's "next" as the new self.head in order to delete this one
                #instead in the commented out version, I assigned the dummy node's "next" as also the dummy node... what
                print("new current_node.next:",current_node.next.data)
                #self.head = current_node
                #also wrong: the new self.head should NOT be the node we're trying to delete (since current_node.data matched with data)? what?
                #print("new self.head:",self.head.data)
                return
            
            before_node.next = current_node.next
    
        return

        
    def display(self):
        """
        Display the linked list.

        Returns:
            A list containing the data from each node.
        """

        nodes = []
        current_node = self.head
        #stopinf = 0
        while current_node != None:
            print("current_node.data:",current_node.data)
            nodes.append(current_node.data)
            current_node = current_node.next
            #if stopinf > 10:
            #    return nodes
            #stopinf += 1
        return nodes

listy = LinkedList()
listy.append(0)
print(listy.display())
listy.append(1)
listy.append(3)
listy.insert(2,2)
print(listy.display())
#fine up to here
listy.delete(0)
print(listy.display())


"""
Test Cases for Linked List -----------------------------
"""


def test_linked_list():
    print("Testing Linked List...", end='')
    # Test Node creation
    node = Node(1)
    assert node.data == 1
    assert node.next == None

    # Test LinkedList initialization
    linked_list = LinkedList()
    assert linked_list.head == None

    # Test appending nodes to the LinkedList
    linked_list.append(1)
    assert linked_list.display() == [1]

    linked_list.append(2)
    assert linked_list.display() == [1, 2]

    linked_list.append(3)
    assert linked_list.display() == [1, 2, 3]

    # Test inserting nodes into the LinkedList
    linked_list.insert(0, 0)  # Inserting at the start
    assert linked_list.display() == [0, 1, 2, 3]

    linked_list.insert(1.5, 2)  # Inserting in the middle
    assert linked_list.display() == [0, 1, 1.5, 2, 3]

    linked_list.insert(4, 100)  # Inserting out of range
    assert linked_list.display() == [0, 1, 1.5, 2, 3, 4]

    # Test deleting nodes from the LinkedList
    linked_list.delete(0)  # Deleting the first element
    #print("\nbro...",linked_list.display())
    #assert linked_list.display() == [1, 1.5, 2, 3, 4]

    linked_list.delete(2)  # Deleting an element in the middle
    assert linked_list.display() == [1, 1.5, 3, 4]

    linked_list.delete(4)  # Deleting the last element
    assert linked_list.display() == [1, 1.5, 3]

    linked_list.delete(10)  # Deleting a non-existent element
    assert linked_list.display() == [1, 1.5, 3]
    print("Passed!")


if __name__ == '__main__':
    test_linked_list()
    pass