"""
Max Heap

Name: Morgan
"""

"""
Max Heap is a data structure that supports the following operations:
    - insert: insert an element into the heap
    - extract_max: extract the maximum element (only accessible one) from the heap

The heap is represented as an array. The root of the heap is at index 1.
The left child of the node at index i is at index 2i.
The right child of the node at index i is at index 2i + 1.

The heap property is that the value of a node is greater than or equal to
the values of its children.

For example, the following array represents a max heap:
    [0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

The following array does not represent a max heap:
    [0, 10, 9, 8, 7, 6, 5, 4, 3, 2, 11]


Time Complexity:
    - insert: O(log n)
    - extract_max: O(log n)

Space Complexity:
    - O(n)
"""


class MaxHeap:
    """Implements a max heap data structure"""

    def __init__(self):
        """Initialize the heap with a dummy element at index 0"""
        self.heap = [0]

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap)-1)
        print("\ninserted:",val,"self.heap:",self.heap)
    
    def extract_max(self):
        if len(self.heap) == 1:
            #only 0
            return None
        
        return_val = self.heap[1]
        print("\nops to remove",return_val)
        self.heap[1] = self.heap[-1]
        print("new self.heap[1]:",self.heap[1])
        self.heap.pop(-1)
        print("updated self.heap:", self.heap)
        #print("\nself.heap[1]:",self.heap[1])
        
        self._heapify_down(1)
        print("ops to remove",return_val,"are done")
        return return_val

    def _parent(self, index):
        return index // 2

    def _left_child(self, index):
        return 2*index

    def _right_child(self, index):
        return 2*index + 1

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_up(self, index, recursive = True):
        #when inserting:
        #first insert the number at the very end of the list
        #then bubble "up" the tree or "forward" the list
        #this time, bubble up if BIGGER

        print("\nheapify up (when inserting)")
        if recursive != True:
            print("FIRST TIME!")

        print("index:", index)

        node = self.heap[index]
        parent = self.heap[index // 2]

        print("selected (permanent):", node, "parent:", parent)

        if parent == 0:
            print("FIN: parent is DUMMY NODE! LEAVE IT ALONE!")

            return

        if node > parent:
            #print("node is lesser than parent")
            #self.heap[index], self.heap[self.heap.index(parent)] = self.heap[self.heap.index(parent)], self.heap[index]
            self._swap(index, self.heap.index(parent))
            print("FIN")
            self._heapify_up(self.heap.index(node), True)
        else:
            #if node is actually smaller than the child
            #no equal scenario; no duplicate vals in Heaps
            print("FIN: DONE")
            return

    def _heapify_down(self, index):
        #when extracting
        #after the root node is removed,
        #dealing with the "replacing" node that's now in the wrong place.
        chosen_child = None
        print("\nheapify down (when extracting)")
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
            chosen_child = max(chosen_child, self.heap[index * 2 + 1])
            #the more WORTHY one to replace the current node's place.
            print("chosen_child chosen:", chosen_child)
        

        #chosen_child = max(self.heap[index * 2], self.heap[index * 2 + 1])

        if chosen_child == None:
            print("chosen child is None.")
            #no children = bottomost
            return
        elif node < chosen_child:
            
            print("node is still smaller than chosen_child. commencing swap")
            self._swap(self.heap.index(node), self.heap.index(chosen_child))
            print("self.heap[index]:",self.heap[index], "self.heap[self.heap.index(chosen_child)]", self.heap[self.heap.index(node)])
            #print("self.heap.index(node):",self.heap.index(node))
            #do NOT call node! node is still pointing towards self.heap[index], the old #.]
            #this is because the vals in the list are primitive integers
            #even when I change what node's pointing WITH, node is still pointing to the primitive value
            print("\nself.heat.index(node):",self.heap.index(node))
            self._heapify_down(self.heap.index(node))
        else:
            
            #if node is actually smaller than the child
            #no equal scenario; no duplicate vals in Heaps
            print("heapify down recursive is done")
            return


def test_max_heap_simple():
    print('Testing simple Max Heap...', end='')
    heap = MaxHeap()

    # Test inserting elements
    heap.insert(10)
    assert heap.heap[1] == 10

    heap.insert(20)
    assert heap.heap[1] == 20
    assert heap.heap[2] == 10

    heap.insert(15)
    assert heap.heap[1] == 20
    assert heap.heap[2] == 10
    assert heap.heap[3] == 15

    # Test extracting max element
    assert heap.extract_max() == 20
    assert heap.heap[1] == 15
    assert heap.heap[2] == 10

    assert heap.extract_max() == 15
    assert heap.heap[1] == 10

    assert heap.extract_max() == 10
    assert len(heap.heap) == 1  # Only the dummy element should remain

    # Test extracting from an empty heap
    assert heap.extract_max() is None
    print('Passed!')


def test_max_heap_complex():
    print('Testing complex Max Heap...', end='')
    heap = MaxHeap()

    # Test empty heap
    assert heap.extract_max() is None

    # Insert single element
    heap.insert(5)
    assert heap.extract_max() == 5
    assert heap.extract_max() is None

    # Insert multiple elements
    for i in range(1, 11):
        heap.insert(i)

    # Extract elements and verify max order
    for i in range(10, 0, -1):
        assert heap.extract_max() == i

    # Test with duplicates
    heap.insert(5)
    heap.insert(5)
    heap.insert(3)
    heap.insert(3)

    assert heap.extract_max() == 5
    assert heap.extract_max() == 5
    assert heap.extract_max() == 3
    assert heap.extract_max() == 3
    assert heap.extract_max() is None

    # Test with negative numbers
    heap.insert(-5)
    heap.insert(-3)
    heap.insert(-7)

    assert heap.extract_max() == -3
    assert heap.extract_max() == -5
    assert heap.extract_max() == -7
    assert heap.extract_max() is None

    # Test with mixed positive and negative numbers
    heap.insert(-5)
    heap.insert(3)
    heap.insert(-7)
    heap.insert(6)

    assert heap.extract_max() == 6
    assert heap.extract_max() == 3
    assert heap.extract_max() == -5
    assert heap.extract_max() == -7
    assert heap.extract_max() is None
    print('Passed!')


if __name__ == "__main__":
    test_max_heap_simple()
    test_max_heap_complex()