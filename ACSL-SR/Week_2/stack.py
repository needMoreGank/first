"""
Stack

Name: <your name>
We are making our own data type of "Stack" by downgrading a list
"""

"""
Stack ADT (Abstract Data Type) is a data structure that follows the LIFO (Last In First Out) principle.
ADT = not an actual data type, this idea is implemented through actual data types (as created by different languages)

Stacks are used in many applications such as:
    - Function calls
    - Undo/Redo
    - Backtracking
    - Expression evaluation and syntax parsing
    - Memory management
    - etc.
    
Stack methods:
    - push(item) - adds an item to the top of the stack
    - pop() - removes the top item from the stack
    - peek() - returns the top (last) item from the stack without removing it
    - is_empty() - returns True if the stack is empty, False otherwise
    - size() - returns the number of items in the stack
    
Stack implementation by using actual data types:
    - Using a list
    - Using a linked list
    *keep in mind that Python list isn't an actual stack or queue.
    *its abstract data category is an ARRAY
    *both Python list and Java ArrayList is an ARRAY
    
Stack applications:
    - Reversing a string
    - Balancing parentheses
    - Infix, prefix, postfix expressions
    - Implementing undo/redo
    - Implementing backtracking
    - Implementing call stack
    - Implementing memory stack
    - etc.
    
Stack complexity:
    Time complexity = CONSTANT (always a certain amount of number)
    Big O notation: 1 inside means that no matter how many, it ALWAYS takes 1 second
    "n" inside Param signifies the length of list -- in this case, it doesn't matter
    - push(item) - O(1)
    - pop() - O(1)
    - peek() - O(1)
    - is_empty() - O(1)
    - size() - O(1)
    
Stack limitations:
    - Stack size is fixed (depends on the implementation of the programmer)
    - Stack can overflow (depends on the implementation)
    - Stack can underflow (depends on the implementation)
"""

# Stack implementation using a list
# Not as an actual parent function tho...,
# REMINDER: list itself isn't a stack, it's an array.
# we're using Python's built-in list to PRETEND to make a Stack for practice!

class Stack:
    def __init__(self):
        self.stack = []
        pass

    # Method to add data to the stack
    # Adds to the end of the list
    # end = "top" of the stack and first out btw

    # aka discount append
    def push(self, data):
        self.stack.append(data)
        pass

    # Method to remove data from the stack
    # Removes from the top/end of the list
    # Returns None if stack is empty
    # Returns the popped item otherwise

    # aka discount pop
    def pop(self):
        if len(self.stack) != 0:
            return_val = self.stack[len(self.stack)-1]
            self.stack.pop(len(self.stack)-1)
            return return_val
        else:
            return None
        

    # Method to check if stack is empty
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
        

    # Method to view the top/end element of the stack
    # Returns None if stack is empty
    # Returns the top element otherwise

    # aka discount list[len(list)-1]
    def peek(self):
        if self.is_empty() == True:
            return None
        else:
            return self.stack[len(self.stack)-1]
        

    # Method to view all elements of the stack
    # Returns the stack
    def get_stack(self):
        return self.stack
        #so that the list element can be returned.
"""       
stacky = Stack()
n = 0
for s in range(5):
    stacky.push(n)
    n += 1
print(stacky.peek()) #returns 4 as it's the last item in aka the "top" of the stack
print("HI!")
print("STACKY:",stacky.get_stack())
"""

# Use the Stack class you implemented above to solve the following problems


# Function to reverse a string using a stack
# s: string
# return: reversed string
def reverse_string(s):
    #use last in first out mechanism
    #maybe I should implement stacks.
    s_stack = Stack()
    return_val = Stack()
    for char in s:
        s_stack.push(char)
    #print("s_stack:",s_stack.get_stack())

    for item in range(len(s_stack.get_stack())):
        #if I do raw item in stack, it'll get only done once? since it's dynamic?
        #since after I remove 1 item from 2 lists, it only takes care of 1
        #I guess after the first run, there's only 1 item left in s_stack
        #so it counts itself as having been done 1 out of 1 after the subtraction
        #print("item no",item)
        return_val.push(s_stack.peek())
        s_stack.pop()
        #print("s_stack now:",s_stack.get_stack())
        #print("char pushed to return_val:",char)
        #print("list now:",return_val.get_stack())

    #print("return_val raw:",return_val.get_stack())

    return "".join(return_val.get_stack())

#print(reverse_string("abc"))
#should be "cba"


# Function to check if parentheses are balanced
# You can assume that the string only contains braces and no other characters.
# The braces consist of (), [], and {}. You can also assume that empty string is balanced.
# s: string
# return: True if balanced, False otherwise
def is_balanced(s):
    # your code here
    s_stack = Stack()
    open_brackets = ["}","]",")"]
    open_stack = Stack()
    for char in s:
        s_stack.push(char)
    
    for count in range(len(s_stack.get_stack())):
        item = s_stack.peek()
        #print("\ncurrent item:",item)
        if item in open_brackets:
            if item in open_brackets:
                open_stack.push(item)
                #print("item pushed:",item)
        else:
            #print("current top of stack:",s_stack.peek())
            if item == "[":
                if open_stack.peek() != "]":
                    return False
            elif item == "{":
                if open_stack.peek() != "}":
                    return False
            elif item == "(":
                if open_stack.peek() != ")":
                    return False
            open_stack.pop()
        #print("current stack:",s_stack.get_stack())
        #print("current open_stack:",open_stack.get_stack())
        s_stack.pop()
    else:
        if len(open_stack.get_stack()) != 0:
            return False
        else:
            return True
            


#print(is_balanced('[()]{}'))
#True


"""
Test Cases-----------------------------------------------------------------------
"""


# Testing the Stack class
# Testing the Stack class
def test_stack():
    print('Testing Stack class...', end='')
    # Instantiate the Stack class
    s = Stack()

    # Test if new stack is empty
    assert s.is_empty() == True

    # Test push method
    s.push(1)
    s.push(2)
    s.push(3)
    assert s.get_stack() == [1, 2, 3]

    # Test peek method
    assert s.peek() == 3

    # Test pop method
    assert s.pop() == 3
    assert s.get_stack() == [1, 2]

    # Test is_empty method
    assert s.is_empty() == False

    # Test pop method
    assert s.pop() == 2

    # Test peek method
    assert s.peek() == 1

    # Test pop method
    assert s.pop() == 1
    assert s.pop() == None

    # Test peek method
    assert s.peek() == None
    print('Passed!')



def test_reverse_string():
    print('Testing reverse_string()...', end='')
    assert reverse_string('') == ''
    assert reverse_string('a') == 'a'
    assert reverse_string('ab') == 'ba'
    assert reverse_string('abc') == 'cba'
    assert reverse_string('abcd') == 'dcba'
    assert reverse_string('abcde') == 'edcba'
    assert reverse_string('Hello, World!') == '!dlroW ,olleH'
    print('Passed!')


def test_is_balanced():
    print('Testing is_balanced()...', end='')
    assert is_balanced('') == True
    assert is_balanced('[]') == True
    assert is_balanced('()') == True
    assert is_balanced('{}') == True
    assert is_balanced('[](){}') == True
    assert is_balanced('[()]{}') == True
    assert is_balanced('[([]{})]') == True
    assert is_balanced('[([]{})]((())){}') == True
    assert is_balanced('[([]{})]()[{}]') == True
    assert is_balanced('[([]{})][(){}]') == True
    assert is_balanced('[') == False
    assert is_balanced(']') == False
    assert is_balanced('][') == False
    assert is_balanced('[][') == False
    assert is_balanced('[(]}') == False
    assert is_balanced('[(]{})') == False
    assert is_balanced('[([]{})](){}]') == False
    assert is_balanced('()[][([]{})](){}(') == False
    assert is_balanced('{{{{{{{{{') == False
    assert is_balanced('}}}}}}}}') == False
    assert is_balanced('(}') == False
    assert is_balanced('[(])') == False
    print('Passed!')


def test_all():
    # comment out the tests you do not wish to run!
    test_stack()
    test_reverse_string()
    test_is_balanced()


if __name__ == '__main__':
    test_all()
