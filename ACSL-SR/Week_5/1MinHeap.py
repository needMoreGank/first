"""
Min Heap

Name: Morgan
"""

"""
Min Heap is a data structure that supports the following operations:
    - insert: insert an element into the heap
    - extract_min: extract the minimum element ("topmost" or "foremost") from the heap

This time, the heap is represented as an array. The root of the heap is at index 1.
The left child of the node at index i is at index 2i.
The right child of the node at index i is at index 2i + 1.
The paret of the node at index i is at index 2 // i (floor division)

The heap property is that the value of a node is less than or equal to
the values of its children.
Its children do not have relationships.

For example, the following array represents a min heap:
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

Time Complexity:
    - insert: O(log n)
    - extract_min: O(log n)

Space Complexity:
    - O(n)
"""


class MinHeap:
    """Implements a min heap data structure"""

    def __init__(self):
        """Initialize the heap with a dummy element at index 0, for easier math"""
        self.heap = [0]

    def insert(self, val):
        """
        Insert an element into the heap

        Args:
            val: The value to be inserted
        """
        self.heap.append(val)
        self._heapify_up(len(self.heap)-1)

    def extract_min(self):
        """
        Extract the minimum element from the heap

        Returns:
            The minimum element from the heap. If the heap is empty, returns None.
        """
        
        """
        When "extract_min":
        When taking out the root node,
        must then replace that node with the backmost node
        The node (incorrectly placed) must "heapify down" until the Order Principle is restored
        Every time before swapping down, the children themselves are compared to see which one would be the "best fit" too
        """
        if len(self.heap) == 1:
            #only 0
            return None
        
        return_val = self.heap[1]
        self.heap[1] = self.heap[-1]
        print("\nself.heap[1]:",self.heap[1])
        self.heap.pop(-1)
        print("self.heap:", self.heap)
        #print("\nself.heap[1]:",self.heap[1])
        
        self._heapify_down(1)
        return return_val
        
        

    # Below are helper methods for the MaxHeap class. You do not have to use them, but I recommend doing so to
    # simplify your code. If you choose not to use them, you may delete them.
    def _parent(self, index):
        """Return the index of the parent of the node at index"""
        # TODO: Implement this method
        return index // 2

    def _left_child(self, index):
        """Return the index of the left child of the node at index"""
        # TODO: Implement this method
        return 2*index

    def _right_child(self, index):
        """Return the index of the right child of the node at index"""
        # TODO: Implement this method
        return 2*index + 1

    def _swap(self, i, j):
        """Swap the elements at indices i and j"""
        #i and j are the indices
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        pass

    def _heapify_up(self, index, recursive = False):
        #when inserting
        """
        Bubble up the element at index to its proper place
        When taking out a number

        Args:
            index: The index of the element to bubble up
        """

        print("\nheapify up")
        if recursive != True:
            print("FIRST TIME!")

        print("index:", index)
        print("self.heap:",self.heap)

        node = self.heap[index]
        parent = self.heap[index // 2]

        print("node:", node, "parent:", parent)

        if parent == 0:
            print("parent is DUMMY NODE! LEAVE IT ALONE!")
            return

        if node < parent:
            #print("node is lesser than parent")
            #self.heap[index], self.heap[self.heap.index(parent)] = self.heap[self.heap.index(parent)], self.heap[index]
            self._swap(index, self.heap.index(parent))
            self._heapify_up(self.heap.index(node), True)
        else:
            #if node is actually smaller than the child
            #no equal scenario; no duplicate vals in Heaps
            #print("heapify up recursive is done")
            return

    def _heapify_down(self, index):
        #when extracting
        # TODO: Implement this method
        """
        Bubble down the element at index to its proper place
        
        Args:
            index: The index of the element to bubble down (the incorrectly placed backmost node)
        """
        chosen_child = None
        print("\nheapify down")
        print("index:",index)
        print("self.heap:",self.heap)

        if index > len(self.heap)-1:
            print("initial case. the list's max index is 0.")
            return

        node = self.heap[index]
        print("node:",node)

        if index * 2 <= len(self.heap) - 1:
            print("left child is valid:",self.heap[index * 2])
            chosen_child = self.heap[index * 2]
            print("chosen_child:",chosen_child)
        if index * 2 + 1 <= len(self.heap) - 1:
            print("right child is valid:",self.heap[index * 2 + 1])
            chosen_child = min(chosen_child, self.heap[index * 2 + 1])
            print("chosen_child chosen:", chosen_child)
        

        #chosen_child = max(self.heap[index * 2], self.heap[index * 2 + 1])

        if chosen_child == None:
            print("chosen child is None.")
            #no children = bottomost
            return
        elif node > chosen_child:
            
            print("node is still bigger than chosen_child. commencing swap")
            self._swap(self.heap.index(node), self.heap.index(chosen_child))
            print("self.heap[index]:",self.heap[index], "self.heap[self.heap.index(chosen_child)]", self.heap[self.heap.index(node)])
            #print("self.heap.index(node):",self.heap.index(node))
            #do NOT call node! node is still pointing towards self.heap[index], the old #.]
            #this is because the vals in the list are primitive integers
            #even when I change what node's pointing WITH, node is still pointing to the primitive value
            self._heapify_down(self.heap.index(node))
        else:
            
            #if node is actually smaller than the child
            #no equal scenario; no duplicate vals in Heaps
            print("heapify down recursive is done")
            return
        
        


def test_min_heap_simple():
    print('Testing simple MinHeap...', end='')
    heap = MinHeap()

    # Test inserting elements
    heap.insert(10)
    print(heap.heap)
    assert heap.heap[1] == 10

    heap.insert(20)
    assert heap.heap[1] == 10
    assert heap.heap[2] == 20

    heap.insert(5)
    assert heap.heap[1] == 5
    assert heap.heap[2] == 20
    assert heap.heap[3] == 10

    # Test extracting min element
    #print("heap.extract_min:", heap.extract_min())
    assert heap.extract_min() == 5
    assert heap.heap[1] == 10
    assert heap.heap[2] == 20

    assert heap.extract_min() == 10
    print("self.heap:",heap.heap)
    assert heap.heap[1] == 20

    print("self.heap:", heap.heap)
    assert heap.extract_min() == 20
    assert len(heap.heap) == 1  # Only the dummy element should remain

    # Test extracting from an empty heap
    assert heap.extract_min() is None
    print('Passed!')


def test_min_heap_complex():
    print('Testing complex MinHeap...', end='')
    heap = MinHeap()

    # Test empty heap
    assert heap.extract_min() is None

    # Insert single element
    heap.insert(5)
    assert heap.extract_min() == 5
    assert heap.extract_min() is None

    # Insert multiple elements
    for i in range(10, 0, -1):
        heap.insert(i)

    # Extract elements and verify min order
    for i in range(1, 11):
        print("\ni:",i, "heap.top():", heap.heap[1])
        assert heap.extract_min() == i

    # Test with duplicates
    heap.insert(5)
    heap.insert(5)
    heap.insert(3)
    heap.insert(3)

    assert heap.extract_min() == 3
    assert heap.extract_min() == 3
    assert heap.extract_min() == 5
    assert heap.extract_min() == 5
    assert heap.extract_min() is None

    # Test with negative numbers
    heap.insert(-5)
    heap.insert(-3)
    heap.insert(-7)

    print("\nheap.peek:",heap.heap[0])
    assert heap.extract_min() == -7
    assert heap.extract_min() == -5
    assert heap.extract_min() == -3
    assert heap.extract_min() is None

    # Test with mixed positive and negative numbers
    heap.insert(-5)
    heap.insert(3)
    heap.insert(-7)
    heap.insert(6)

    assert heap.extract_min() == -7
    assert heap.extract_min() == -5
    assert heap.extract_min() == 3
    assert heap.extract_min() == 6
    assert heap.extract_min() is None
    print('Passed!')


if __name__ == '__main__':
    #test_min_heap_simple()
    test_min_heap_complex()