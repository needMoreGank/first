"""
Queue

Name: <your name>
"""

"""
Queue is a data structure that is similar to a list, but with a few differences.
Basically manually downgrading a list to implement this abstract content
Queue follows the FIFO (First In First Out) principle.
Queue is used in many applications such as:
    - Breadth First Search (BFS) WHAT IS THIS?
    - Implementing cache "an auxiliary memory from which high-speed retrieval is possible."
    - I guess it's about RAM? because the 1st thing the user requests is the 1st thing the RAM retrieves
    - and the 1st that gets out
    - Implementing a printer queue
    - queues need to be in order
    - etc.
    
Queue operations:
    - enqueue(item) - adds an item to the end of the queue
    - IN QUEUE
    - dequeue() - removes the first item (bottom) from the queue
    - DE QUEUE
    - unlike Stack, in which pop() removes the LAST item (top)
    - peek() - returns the first item from the queue without removing it
    - umlike Stack, which peek() returns the top/LAST item
    - is_empty() - returns True if the queue is empty, False otherwise
    - size() - returns the number of items in the queue
    
Queue implementation:
    - Using a list
    - Using a linked list
    
Queue applications:
    - Breadth First Search (BFS)
    - Implementing cache
    - Implementing a printer queue
    - etc.
    
Queue complexity:
    - same with stack
    - enqueue(item) - O(1)
    - dequeue() - O(1)
    - peek() - O(1)
    - is_empty() - O(1)
    - size() - O(1)
    
Queue limitations:
    - Queue size is fixed (depends on the implementation)
    - Queue can overflow (depends on the implementation)
    - Queue can underflow (depends on the implementation)
    
Queue vs Stack:
    - Queue follows the FIFO (First In First Out) principle
    - Stack follows the LIFO (Last In First Out) principle
"""

# Queue can be implemented using a list, but it is not efficient because deleting at the beginning of a list is O(n)
# since all the elements have to be shifted by one. 
# Instead, we can use a collections.deque which is a double-ended queue
# supports efficient addition and removal of elements from both sides.
# basically a list without the shifting and additional mechanics

# Queue implementation using a deque

from stack import Stack
from collections import deque


class Queue:
    """
    A simple implementation of a Queue data structure.
    This Queue provides FIFO functionality using Python's built-in deque.
    """

    def __init__(self):
        """Initialize an empty Queue via deque"""
        # TODO: Implement this method.
        self.queue = deque()


    def enqueue(self, item):
        """
        Add an element to the end of the Queue.

        Parameters:
        item (any): The item to add to the Queue.
        """
        self.queue.append(item)


    def dequeue(self):
        """
        Remove an element from the front of the Queue.

        Returns:
        The item removed from the Queue. If the Queue is empty, returns None.
        """
        if len(self.queue) != 0:
            val = self.queue[0]
            self.queue.popleft() #pop() by default is removing the last item.
            return val
        else:
            return None

    def peek(self):
        """
        Return the element at the front/first (bottom) of the Queue without removing it.

        Returns:
        The item at the front of the Queue. If the Queue is empty, returns None.
        """
        # TODO: Implement this method.
        return self.queue[0]


    def is_empty(self):
        """
        Check if the Queue is empty.

        Returns:
        True if the Queue is empty, False otherwise.
        """
        if len(self.queue) == 0:
            return True
        else:
            return False

    def size(self):
        """
        Get the number of items in the Queue.

        Returns:
        The number of items in the Queue.
        """
        # TODO: Implement this method.
        return len(self.queue)

    def display(self):
        """
        Display the content of the Queue.

        Returns:
        A list representation of the Queue.
        """
        # TODO: Implement this method.
        return list(self.queue)


def is_palindrome(s):
    """
    Check if a string is a palindrome using a Queue.
    You can also use other data structures such as a Stack.
    Assume that the string only contains lowercase letters and no spaces.

    Parameters:
    s (str): The string to check.

    Returns:
    True if the string is a palindrome, False otherwise.
    """
    # TODO: Implement this method.
    s_stack = Stack()
    s_queue = Queue()
    #first half goes to stack
    #last half goes to queue
    #after sorting everything, things get pulled out
    # r a c e c a r
    #stack: rac -> peeking everything is c a r
    #queue: car -> peeking everything is c a r

    # 5 chars:
    # 0, 1, 2, 3, 4
    # 4/2 = 2.0
    # 6 chars:
    # 0, 1, 2, 3, 4, 5
    # 5/2 = 2.5
    midpoint = (len(s)-1)/2
    for char_index in range(len(s)):
        char = s[char_index]
        #print("char_index:",char_index)
        if char_index < midpoint:
            s_stack.push(char)
        elif char_index > midpoint:
            s_queue.enqueue(char)
        elif char_index == midpoint:
            #this happens if char count is odd and there's a middle number
            pass
            #ignore
    
    #print("s_stack:",s_stack.get_stack())
    #print("s_queue:",s_queue.display())
    
    #print("len match:",len(s_stack.get_stack()) == len(s_queue.display()))
    for item_index in range(len(s_stack.get_stack())):
        if s_stack.pop() == s_queue.dequeue():
            pass
        else:
            return False
    else:
        return True

#print(is_palindrome("racecar")) 
#True


"""
Test cases for Queue implementation. ----------------------------
"""


def test_queue():
    print("Testing Queue implementation...", end="")
    queue = Queue()
    assert queue.is_empty() is True
    assert queue.size() == 0
    queue.enqueue("Apple")
    #print(queue.display())
    assert queue.display() == ["Apple"]
    queue.enqueue("Banana")
    assert queue.display() == ["Apple", "Banana"]
    assert queue.peek() == "Apple"
    assert queue.dequeue() == "Apple"
    assert queue.display() == ["Banana"]
    assert queue.is_empty() is False
    assert queue.size() == 1
    print("Passed!")


def test_is_palindrome():
    print("Testing is_palindrome()...", end="")
    assert is_palindrome("racecar") is True
    assert is_palindrome("apple") is False
    assert is_palindrome("a") is True
    assert is_palindrome("") is True
    assert is_palindrome("ab") is False
    assert is_palindrome("abc") is False
    assert is_palindrome("abcd") is False
    assert is_palindrome("abcde") is False
    assert is_palindrome('kayak') is True
    assert is_palindrome('rotor') is True
    assert is_palindrome('우영우') is True
    assert is_palindrome('역삼역') is True
    assert is_palindrome('기러기') is True
    assert is_palindrome('대한민국') is False
    print("Passed!")

def test_all():
    # Comment out the tests you do not wish to run!
    test_queue()
    test_is_palindrome()
    #pass


if __name__ == '__main__':
    test_all()