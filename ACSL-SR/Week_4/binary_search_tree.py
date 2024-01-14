"""
Binary Search Tree

Name: <your name>
"""

"""
Binary Search Tree (BST) is a binary tree that follows the following conditions:
    - The left subtree of a node contains only nodes with keys lesser than the node's key
    - The right subtree of a node contains only nodes with keys greater than the node's key
    - The left and right subtree each must also be a binary search tree

BST has the following advantages over arrays:
    - Dynamic size
    - Ease of insertion/deletion

BST has the following methods:
    - insert(data): Insert a node with the given data to the BST.
    - delete(data): Delete the first node with the given data from the BST.
    - search(data): Search for the first node with the given data in the BST.

Time Complexity:
    - insert(data): O(log n)
    - delete(data): O(log n)
    - search(data): O(log n)

Space Complexity: O(n)

BST limitations:
    - BST can be unbalanced, which means that the height of the tree can be O(n)
    - BST can be degenerate, which means that the height of the tree can be O(n)

BST vs Linked List:
    - BST is a binary tree, while Linked List is a linear data structure
    - BST is ordered, while Linked List is unordered
    - BST has a search time of O(log n), while Linked List has a search time of O(n) 
"""

# Binary Search Tree implementation

from collections import deque


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
        #self.key is like self.data.


class BinarySearchTree:
    """
    A class representing a Binary Search Tree.

    Attributes:
    root (Node): The root node of the tree.
    """

    #TIP: EVERY ONE OF THESE METHODS WILL USE RECURSION
    #THEREFORE THEY WILL NEED HELPER FUNCTIONS
    #Use resources on the internet. :) concept is easy, but implementation is hard. DON'T FEEL BAD :((((((

    def __init__(self):
        self.root = None
        # a node that is the root node.

    def insert_recursive(self, key, curr_node):
        if curr_node.key == key:
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

    def insert(self, key):
        """
        Inserts a new key in the BST. If the BST is empty, the new key becomes the root.
        If the BST is not empty, the new key is inserted in the correct position.
        If the key already exists in the BST , the key is not inserted.

        Parameters:
        key (int): The key to be inserted.
        """
        # TODO: Write your code here
        
        if self.root == None:
            self.root = Node(key)
        else:
            return self.insert_recursive(key, self.root)

    def delete_find_successor(self, node):
        """Helper method to find the node with the minimum key in a subtree."""
        current = node
        # loop down to find the leftmost leaf
        while current.left is not None:
            current = current.left

        return current

    def delete_recursive(self, node, key):
        '''
        #the way this method works:

        "dive" down the tree until the target node is found
        this will compile a "path": the nodes traversed through to find the target node.

        after the base case (of "finding the node", or key matching the current node),
        then "add" them back via recursion:
        (remember the recursive function is setting the curr_node's left/right (whichever was chosen) as the returned value of the recursive call)


        the recursive calls will now "re"-set

        but the target node gets "forgotten" to be added because it's actually not returned
        - instead, it's "skipped" 
        - its child/successor is instead returned --  the child/successor takes the place of the deleted node
        '''

        if node is None:
        #tree is empty
            return node
        
        if key < node.key:
            node.left = self.delete_recursive(node.left, key)

        elif key > node.key:
            node.right = self.delete_recursive(node.right, key)
        
        elif node.key == key:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                node.key = self.delete_find_successor(node.right).key
                node.right = self.delete_recursive(node.right, node.key)

        return node

    def delete(self, key):
        self.root = self.delete_recursive(self.root, key)
        
    def search_recursive(self, key, node):
        #node is curr_node.
        if node != None:
            #print("node.key:",node.key)
            pass
        if node is None:
            #we are dead...
            return None
        if node.key == key:
            #if the node.data matches key:
            return node
        if type(node.key) == str:
            #print("node.key is dummy str")
            return
        if key > node.key:
            return self.search_recursive(key, node.right)
            #think of it as we must call it again...
            #but we need to store this value?! so we all "return"
            #"that's it"
        elif key < node.key:
            return self.search_recursive(key, node.left)
        return

    def search(self, key):
        """
        Searches for a node with a given key in the BST.

        Parameters:
        key (int): The key to search for.

        Returns:
        Node: The node with the given key if it exists, None otherwise.
        #returns the Node object itself.
        """

        #base case = matching key with node
        return self.search_recursive(key, self.root)
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
        
        return_list.append(curr_node.key)

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
        
    def preorder_traversal_recursive(self, curr_node, return_list, noinf):
        noinf += 1
        if noinf > 20:
            return
        
        #print("curr_node.key selected:",curr_node.key)


        return_list.append(curr_node.key)

        if curr_node.left is not None:
            self.preorder_traversal_recursive(curr_node.left, return_list, noinf)

        if curr_node.right is not None:
            self.preorder_traversal_recursive(curr_node.right, return_list, noinf)
        
        return return_list
                  
    def preorder_traversal(self):
        noinf = 0

        # TODO: Write your code here
        if self.root == None:
            #print("tree doesn't even exist")
            return None
        
        else:
            return_list = []
            return self.preorder_traversal_recursive(self.root, return_list, noinf)
        
    def postorder_traversal_recursive(self, curr_node, return_list):

        if curr_node.left is not None:
            #acts as "holes"
            #once it's snagged, program is forced down a "hole" until the node has no children
            self.postorder_traversal_recursive(curr_node.left, return_list)
            #return_list value carries on to the main function
            #thanks to lists' REFERENCE data type.
            #just like variable assignment
            #instead of the value being copied, return_list's memory address is passed
            #so the list also gets directly edited

            #this is in scope of return_list I guess? lol

        if curr_node.right is not None:
            self.postorder_traversal_recursive(curr_node.right, return_list)
        
        return_list.append(curr_node.key)
        
        return return_list

    def postorder_traversal(self):
        """
        Performs a post-order traversal of the tree and returns a list of visited nodes.
        returns:
        list: A list of visited nodes.
        """
        # TODO: Write your code here
        if self.root == None:
            #print("tree doesn't even exist")
            return None
        
        else:
            return_list = []
            return self.postorder_traversal_recursive(self.root, return_list)

    def get_height_recursive(self, node, depthcount = 0):
        #tree depth = tree height
        '''
        10
       /  \
      5    15
        
        if node != None:
            print("node:",node.key)
        else:
            print("node is None")
        '''
        if node == None:
            #print("dead end")
            #print("depthcount:",depthcount)
            return depthcount
        
        if node != self.root:
            depthcount += 1
        
        left_depth = self.get_height_recursive(node.left, depthcount)
        right_depth = self.get_height_recursive(node.right, depthcount)

        if left_depth > right_depth:
            #print("leftdepth chosen:",left_depth)
            return left_depth
        else:
            #print("rightdepth chosen:",right_depth)
            return right_depth

    def get_height(self):
        """
        Returns:
        int: The height of the tree. (leaf aka no children node is 0)
        """
        # TODO: Write your code here
        
        height = self.get_height_recursive(self.root)
        #print("height:",height)
        return height        

def test_bst():
    print("Testing Binary Search Tree implementation...", end="")
    #, end=""
    # Test Node creation
    node = Node(1)
    assert node.key == 1
    assert node.left is None
    assert node.right is None

    # Test BST initialization
    bst = BinarySearchTree()
    assert bst.root is None

    # Test BST insertion
    bst.insert(50)
    assert bst.root.key == 50
    bst.insert(30)
    assert bst.root.left.key == 30
    bst.insert(70)
    assert bst.root.right.key == 70
    bst.insert(20)
    assert bst.root.left.left.key == 20
    bst.insert(40)
    assert bst.root.left.right.key == 40
    bst.insert(80)
    assert bst.root.right.right.key == 80
    assert bst.inorder_traversal() == [20, 30, 40, 50, 70, 80]
    assert bst.postorder_traversal() == [20, 40, 30, 80, 70, 50]
    '''
    Here is visual representation of the tree:
            50 height 2 (total height)
           /  \
          30    70 height 1
        /  \      \
      20    40     80 height 0
    '''

    #me adding on code
    """
    bst.insert(45)
    bst.insert(35)
    bst.insert(43)
    bst.insert(44)
    """

    '''
    Here is visual representation of the tree:
            50 height 2 (total height)
           /  \
          30    70 height 1
        /  \      \
      20    40     80 height 0
           /   \
         35    45
              /
            43
              \
              44
             
            
    '''

    #bst.delete(35)
    #print("bst.root.left.right.left:",bst.root.left.right.left)
    #assert bst.search(35) == None
    #assert bst.root.left.right.left == None
    #bst.root.left.right.left
    #bst.delete(40)
    #assert bst.search(40) == None
    #print("bst.root.left.right.key:",bst.root.left.right.key)
    #assert bst.root.left.right.key == 43
    #print("bst.root.left.right.right.left.key:",bst.root.left.right.right.left.key)
    #assert bst.root.left.right.right.left.key == 44

    '''
    New updated tree
    Here is visual representation of the tree:
            50 height 2 (total height)
           /  \
          30    70 height 1
        /  \      \
      20    43     80 height 0
           /  \
         35    45
              /
            44
              
              
    '''
    
    
    # Test BST search
    assert bst.search(50) == bst.root
    assert bst.search(30) == bst.root.left
    assert bst.search(70) == bst.root.right
    assert bst.search(20) == bst.root.left.left
    assert bst.search(40) == bst.root.left.right
    assert bst.search(80) == bst.root.right.right
    assert bst.search(100) is None
    assert bst.search(10) is None

    # Test BST inorder traversal
    #print("bst.preorder_traversal():",bst.preorder_traversal())
    assert bst.preorder_traversal() == [50, 30, 20, 40, 70, 80]
    assert bst.inorder_traversal() == [20, 30, 40, 50, 70, 80]
    assert bst.postorder_traversal() == [20, 40, 30, 80, 70, 50]

    # Test BST deletion
    bst.delete(80)  # Remove leaf node
    assert bst.root.right.right is None

    bst.insert(80)  # Add leaf node back
    bst.delete(70)  # Remove node with one child
    assert bst.root.right.key == 80

    bst.delete(30)  # Remove node with two children
    assert bst.root.left.key == 40
    assert bst.root.left.left.key == 20

    '''
    Here is visual representation of the tree:
            50
           /  \
          40    80
         /  
       20
    '''
    assert (bst.preorder_traversal() == [50, 40, 20, 80])
    assert (bst.inorder_traversal() == [20, 40, 50, 80])
    assert (bst.postorder_traversal() == [20, 40, 80, 50])

    # Test BST height
    assert (bst.get_height() == 2)
    

    """
    Test Larger BST ------------------------------------------------------------------------
    """
    # Test BST initialization
    bst = BinarySearchTree()
    assert bst.root is None

    # Test BST insertion
    bst.insert(50)
    assert bst.root.key == 50
    bst.insert(30)
    assert bst.root.left.key == 30
    bst.insert(70)
    assert bst.root.right.key == 70
    bst.insert(20)
    assert bst.root.left.left.key == 20
    bst.insert(40)
    assert bst.root.left.right.key == 40
    bst.insert(80)
    assert bst.root.right.right.key == 80
    bst.insert(10)
    assert bst.root.left.left.left.key == 10
    bst.insert(25)
    assert bst.root.left.left.right.key == 25
    bst.insert(35)
    assert bst.root.left.right.left.key == 35

    # Test BST search
    assert bst.search(50) == bst.root
    assert bst.search(30) == bst.root.left
    assert bst.search(70) == bst.root.right
    assert bst.search(20) == bst.root.left.left
    assert bst.search(40) == bst.root.left.right
    assert bst.search(80) == bst.root.right.right
    assert bst.search(25) == bst.root.left.left.right
    assert bst.search(100) is None
    assert bst.search(5) is None
    assert bst.search(45) is None
    assert bst.search(60) is None

    # Test BST inorder traversal
    assert bst.preorder_traversal() == [50, 30, 20, 10, 25, 40, 35, 70, 80]
    #print("\nbst.inorder_traversal():",bst.inorder_traversal())
    assert bst.inorder_traversal() == [10, 20, 25, 30, 35, 40, 50, 70, 80]
    assert bst.postorder_traversal() == [10, 25, 20, 35, 40, 30, 80, 70, 50]
    #works fine until here

    # Test BST deletion
    bst.delete(80)  # Remove leaf node
    #not the problem: parent_node ain't the root
    #print("bst.root.right.right:",bst.root.right.right)
    assert bst.root.right.right is None

    bst.insert(80)  # Add leaf node back
    #print("\nbst.root.right.right.key:",bst.root.right.right.key)
    #print(bst.search(80).right)
    #works fine until here

    #print("good preorder_traversal:",bst.preorder_traversal())
    
    bst.delete(70)  # Remove node with one child

    #print("bst.search(10):",bst.search(10))
    #print("inorder_traversal:",bst.preorder_traversal())


    #where it went wrong
    #print("bst.root.right.key:",bst.root.right.key)
    #assert bst.search(80) != None
    assert bst.root.right.key == 80

    bst.delete(30)  # Remove node with two children
    assert bst.root.left.key == 35
    assert bst.root.left.right.key == 40

    '''
    Here is visual representation of the tree:
            50
           /  \
         30   80
        /  \
       20  35
      /  \   \
    10    25  40
    '''

    assert (bst.preorder_traversal() == [50, 35, 20, 10, 25, 40, 80])
    assert (bst.inorder_traversal() == [10, 20, 25, 35, 40, 50, 80])
    assert (bst.postorder_traversal() == [10, 25, 20, 40, 35, 80, 50])

    bst.insert(70)
    bst.insert(75)
    assert (bst.inorder_traversal() == [10, 20, 25, 35, 40, 50, 70, 75, 80])
    '''
    Here is visual representation of the tree:
            50
           /  \
         35    80
        /  \   /
       20  40 70
      /  \      \
    10    25    75
    '''

    bst.delete(50)
    assert bst.root.key == 70
    assert bst.root.right.key == 80
    assert bst.root.right.left.key == 75

    '''
    Here is visual representation of the tree:
            70
           /  \
         35    80
        /  \   /
       20  40 75
      /  \
    10    25
    '''

    assert (bst.preorder_traversal() == [70, 35, 20, 10, 25, 40, 80, 75])
    assert (bst.inorder_traversal() == [10, 20, 25, 35, 40, 70, 75, 80])
    assert (bst.postorder_traversal() == [10, 25, 20, 40, 35, 75, 80, 70])

    # Test BST height
    assert (bst.get_height() == 3)
    print("Passed all tests!")

if __name__ == "__main__":
    test_bst()