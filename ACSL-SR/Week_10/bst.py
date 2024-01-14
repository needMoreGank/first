"""
Name: Morgan K
"""

class Node:
    """
    A Node class that will be used as the basic structure in our Binary Search Tree.

    Attributes:
    key (int): The key value of the node.
    left (Node): The left child node.
    right (Node): The right child node.
    """

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.count = 1
        #self.key is like self.data.

class BST:
    def __init__(self):
        self.root = None

    def insert_recursive(self, key, curr_node):
        if curr_node.key == key:
            #when overlaps! IMPORTANT.
            #print("overlap!")
            curr_node.count += 1
            #print(curr_node.key, "count update:",curr_node.count)
            return
        else:
            if key < curr_node.key:
                if curr_node.left is None:
                    curr_node.left = Node(key)
                    return
                curr_node = curr_node.left
            elif key > curr_node.key:
                if curr_node.right is None:
                    curr_node.right = Node(key)
                    return
                curr_node = curr_node.right
            return self.insert_recursive(key, curr_node)
            #just goes into hole
            #actually returns: nothing

    def insert(self, key):
        if self.root == None:
            self.root = Node(key)
        else:
            return self.insert_recursive(key, self.root)
        """
        Searches for a node with a given key in the BST.

        Parameters:
        key (int): The key to search for.

        Returns:
        Node: The node with the given key if it exists, None otherwise.
        #returns the Node object itself.
        """

        #base case = matching key with node
        #return self.search_recursive(key, self.root)
        #this is needed BECAUSE search_recursive cannot be called by itself.

    def inorder_traversal_recursive(self, curr_node, return_list):
        #left parent right
        #base case: node has no children; return node itself
        #recursive case: node has children; call recursive function on LEFT child.

        """
        TREE
                5
              /   \
             2     7
           /  \
          1    3
        """

        #ex case: [20, 30, 40, 50, 70, 80]

        '''
        Here is visual representation of the tree:

             50 height 2 (total height)
            /  \
           30    70 height 1
          /  \     \
        20    40    80 height 0
        '''
        
        if curr_node.left is not None:
            #print("left child available. moving on now:",curr_node.left.key)
            self.inorder_traversal_recursive(curr_node.left, return_list)
            #return_list value carries on to the main function
            #thanks to lists' REFERENCE data type.
            #just like variable assignment
            #instead of the value being copied, return_list's memory address is passed
            #so the list also gets directly edited

            #this is in scope of return_list I guess? lol
        
        if curr_node.left is not None and curr_node.right is None:
            return_list.append(curr_node)

        if curr_node.left is None and curr_node.right is not None:
            return_list.append(curr_node)

        if curr_node.right is not None:
            self.inorder_traversal_recursive(curr_node.right, return_list)
        
        return return_list
     #btw even though this technically gets printed out every time, it's sort of a "trashed value"

    def inorder_traversal(self):

        """
        Performs an in-order traversal of the tree and returns a list of visited nodes in order.
        returns:
        list: A list of visited nodes.
        """
        # TODO: Write your code here
        
        if self.root == None:
            return None
        
        else:
            return_list = []
            return self.inorder_traversal_recursive(self.root, return_list)

def process_string(s):
    """
    Process the input string, build a binary search tree, and calculate the desired output.

    Args:
    - s (str): The input string.

    Returns:
    - int: The sum of counts for nodes with a single child in the constructed tree.
    """
    # TODO: Implement this function
    bst = BST()
    str = []
    return_sum = 0

    for c in range(len(s)):
        if s[c].isalnum():
            str.append(s[c].upper())
    #print(str)

    for item_num in range(len(str)):
        #print("current letter:", str[item_num],"unicode #:",ord(str[item_num]))
        bst.insert(ord(str[item_num]))
    
    values_list = bst.inorder_traversal()

    for item_num in range(len(values_list)):
        return_sum += values_list[item_num].count

    #print(return_sum)
    return return_sum
    #now make it only accept single children. the filtering algorithm.



process_string("how much wood could a woodchuck chuck if a woodchuck could chuck wood")

def test1():
    test_strings = [
        "abracadabracabob",
        "American Computer Science League",
        "Python and Java are programming languages",
        "Python and Java and java and python",
        "the quick brown fox jumped over the lazy river"
    ]

    expected_outputs = [15, 9, 23, 18, 9]

    print('Running a first test set...')
    for idx, (test_str, expected) in enumerate(zip(test_strings, expected_outputs), 1):
        result = process_string(test_str)
        assert result == expected, f"Test {idx} failed. Expected {expected}, but got {result}."
        print(f"Test {idx} passed!")
    print('All tests passed!')


def test2():
    print('Running a second test set...')
    test_strings = [
        "simple simon",
        "simple simon simply said something slowly",
        "peter piper picked a peck of pickles",
        "peter piper picked a peck of pickled peppers",
        "how much wood could a woodchuck chuck if a woodchuck could chuck wood"
    ]

    expected_outputs = [4, 10, 7, 8, 18]

    for idx, (test_str, expected) in enumerate(zip(test_strings, expected_outputs), 1):
        result = process_string(test_str)
        assert result == expected, f"Test {idx} failed. Expected {expected}, but got {result}."
        print(f"Test {idx} passed!")
    print('All tests passed!')


if __name__ == "__main__":
    test1()
    print()
    test2()