"""
Sorting Algorithms

Name: <your name>
"""


"""
Linear Search is a searching algorithm that searches for an item in a list by going through each item in the list
starting from the first item until the item is found or the end of the list is reached.

Linear Search has the following steps:
    1. Start from the first item in the list.
    2. Compare the item with the item we are searching for.
    3. If the item is found, return the index of the item.
    4. If the item is not found, move to the next item in the list.
    5. Repeat steps 2-4 until the item is found or the end of the list is reached.
    6. If the item is not found, return -1.

Linear Search has a time complexity of O(n) where n is the number of items in the list.
Linear Search has a space complexity of O(1) because it does not use any additional space.

Complete the 'linear_search' function below.
"""
def linear_search(lst, target):
    """
    Perform a linear search on a list.

    This function iteratively checks each element of the list to see if it is equal to the target value.
    If a match is found, the index of the matching element is returned. If no match is found, -1 is returned.

    Parameters:
    lst (list): The list to be searched.
    target (any): The value to be searched for.

    Returns:
    int: The index of the target value if it exists in the list, else -1.
    """
    #literally the most basic for loop search algorithm.
    # TODO: Write your code here
    for item in lst:
        if item == target:
            return lst.index(target)
    else:
        return -1


def triangle_number(n):
    """
    Compute the nth triangular number.

    This function uses a recursive approach to compute the nth triangular number.
    A triangular number counts the objects that can form an equilateral triangle.
    The nth triangular number is the number of dots composing a triangle with n dots on a side,
    and it represents the sum of the n natural numbers from 1 to n.
    Visualize Triangle Number: https://www.mathsisfun.com/algebra/triangular-numbers.html

    Parameters:
    n (int): The number to compute the triangular number of.

    Returns:
    int: The nth triangular number.
    """
    # TODO: Write your code here
    # just copypasted from triangle_number.py
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + triangle_number(n-1)


"""
Binary Search is a searching algorithm that searches for an item in a sorted list by repeatedly dividing the list in half
and searching for the item in the half where the item might be located.

Binary Search has the following steps:
    1. Start from the middle item in the list.
    2. Compare the item with the item we are searching for.
    3. If the item is found, return the index of the item.
    4. If the item is not found, check if the item is less than or greater than the middle item.
    5. If the item is less than the middle item, repeat steps 1-4 with the left half of the list.
    6. If the item is greater than the middle item, repeat steps 1-4 with the right half of the list.
    7. Repeat steps 1-6 until the item is found or the end of the list is reached.
    8. If the item is not found, return -1.

Binary Search has a time complexity of O(log n) where n is the number of items in the list.
Binary Search (iterative) has a space complexity of O(1) because it does not use any additional space.
Binary Search (recursive) has a space complexity of O(log n) because it uses additional space for the recursive calls.

Complete the 'binary_search_iterative' function below.
"""
def binary_search_iterative(lst, target):
    """
    Perform an iterative binary search on a sorted list.

    This function repeatedly divides the search space in half until the target value is found or the search space is exhausted.
    If a match is found, the index of the matching element is returned. If no match is found, -1 is returned.

    Parameters:
    lst (list): The SORTED list to be searched.
    target (any): The value to be searched for.

    Returns:
    int: The index of the target value if it exists in the list, else -1.
    """
    # TODO: Implement the binary search algorithm iteratively here


    #get low and high vals (conveniently the lowest and highest both indexes and values)
    #calculate the midpoint index
    #check the midpoint index value
    #depending on what it is midpoint value is new LOW/HIGH

    low = 0
    high = len(lst)-1
    if target not in lst:
        return -1
    
    while True:
        #print('inifite?')
        #forgot to make a breakout case.
        #if using while loop and nothing happens, it might be an infinite case
        #add print debugs to find out
        midpoint_index = (low + high) // 2
        midpoint_val = lst[midpoint_index]
        if midpoint_val == target:
            return lst.index(midpoint_val)
        elif midpoint_val < target:
            #target is bigger than midpoint therefore on the right side
            low = midpoint_index + 1 #we already checked midpoint_index so take it out
            continue
        elif target < midpoint_val:
            high = midpoint_index - 1
            continue



def binary_search_recursive(lst, target, low=0, high=None):
    #print("List:",lst)
    """
    Perform a binary search on a sorted list.

    This function recursively divides the list in half until the target value is found or the search space is exhausted.
    If a match is found, the index of the matching element is returned. If no match is found, -1 is returned.

    Parameters:
    lst (list): The sorted list to be searched.
    target (any): The value to be searched for.
    low (int, optional): The lower bound of the search space. Defaults to 0.
    high (int, optional): The upper bound of the search space. Defaults to the length of the list minus 1.

    Returns:
    int: The index of the target value if it exists in the list, else -1.
    """
    # TODO: Implement the binary search algorithm recursively here
    if high == None:
        high = len(lst) - 1
    
    if target not in lst:
        return -1
    
    midpoint_index = (low + high + 1) // 2
    #print("Midpoint_index:",midpoint_index)
    midpoint_val = lst[midpoint_index]
    if midpoint_val == target:
        #print("works!")
        return midpoint_index
        #this returns midpiont val to the underneath parent (among nested)
        #but never gets the actual function (the ultimate parent one) to RETURN
    elif midpoint_val < target:
        #target is bigger than midpoint therefore on the right side
        low = midpoint_index + 1 #we already checked midpoint_index so take it out
        #print("Target is bigger. New low:",low)
        return binary_search_recursive(lst, target, low, high)
    elif target < midpoint_val:
        high = midpoint_index - 1
        #print("Target is smaller. New high:",low)
        return binary_search_recursive(lst, target, low, high)
    
    #return midpoint_index
    #this just returns the 1st run's midpoint_index (which is 7)
    #return return_val

"""
Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order.
Bubble sort has the following steps:
    1. Start from the first element in the list.
    2. Compare the current element with the next element.
    3. If the current element is greater than the next element, swap them.
    4. If the current element is less than or equal to the next element, move to the next element.
    5. Repeat steps 2-4 until the end of the list is reached.
    6. Repeat steps 1-5 until the list is sorted.

Bubble sort has a time complexity of O(n^2) where n is the number of elements in the list.
Bubble sort has a space complexity of O(1) because it does not use any additional space.

Complete the 'bubble_sort' function below.
"""
def bubble_sort(lst):
    #print("List:",lst)
    """
    Perform the bubble sort algorithm on a list.

    :param lst: List of unordered elements
    :return: Sorted list of elements

    Bubble sort is a simple sorting algorithm that repeatedly steps through the list,
    compares adjacent elements and swaps them if they are in the wrong order.
    The pass through the list is repeated until the list is sorted.
    """
    # TODO: Write your code here
    #curr_index = 0
    done = 0
    #write exceptions for list len = 0 or 1 to save time

    for count in range(len(lst)):
        curr_index = 0
        while True:
            if curr_index == len(lst)-1 - done:
                done += 1
                #print("number",done,"DONE!")
                break
            #print("Curr_index:",curr_index,"Curr_val:",lst[curr_index])
            #print("curr_index:", curr_index)
            #print("curr_index+1 :",curr_index+1,"for",lst)
            if lst[curr_index] > lst[curr_index+1]:
                #print("Curr_index is bigger than latter")
                savedval = lst[curr_index]
                lst[curr_index] = lst[curr_index+1]
                lst[curr_index+1] = savedval
                #print("savedval:",savedval)
                #curr_index = lst.index(savedval)
                continue
            else:
                #moving onto the right one (curr_index + 1) if curr_index fails to be bigger
                curr_index = curr_index + 1
                continue
    return lst

#print(bubble_sort([3, 2, 1]))
#[1, 2, 3]


"""
Selection sort is a simple sorting algorithm that repeatedly finds the minimum element from the unsorted part of the list and puts it at the beginning.
Selection sort has the following steps:
    1. Find the minimum element in the unsorted part of the list.
    2. Swap the minimum element with the first element of the unsorted part of the list.
    3. the swapped element is now SORTED. that index will subsequently be IGNORED.
    4. Repeat steps 1-2 until the list is sorted.

Selection sort has a time complexity of O(n^2) where n is the number of elements in the list.
Selection sort has a space complexity of O(1) because it does not use any additional space.

Complete the 'selection_sort' function below.
"""
def selection_sort(lst):
    """
    Perform the selection sort algorithm on a list.

    :param lst: List of unordered elements
    :return: Sorted list of elements

    Selection sort is a simple comparison-based algorithm. It seeks out the smallest element in the list and
    swaps it with the first element. It then finds the smallest element in the rest of the list and swaps
    it with the second element, and so on. In other words, after the i-th pass, the i smallest items are in place.

    This sort is noted for its simplicity and also has performance advantages over more complicated
    algorithms in certain situations, particularly where auxiliary memory is limited.
    """
    # TODO: Write your code here
    # cycle through list listlen amount of times
    # for each cycle, hold onto the SMALLEST value
    # after reaching the end, take the smallest value and swap its place with the 0th index
    # and so forth...
    #print("STARTING:",lst)
    for chosen_index in range(len(lst)):
        #print("\nCHOSEN_INDEX:",chosen_index, "lst:", lst)
        #print("chosen_index val:", lst[chosen_index])
        #for how many items are in list
        smallest_index = chosen_index
        #if smallest_index = 0, literally cannot ever change since 0 is the smallest
        for todo_index in range(len(lst)-1-chosen_index): #the leftover after chosen_index, -1 is added because chosen_index itself should be counted
            #for every cycle, continue until satisfied
            #print("smallest_index:",smallest_index)
            todo_index += chosen_index + 1
            #print("todo_index:",todo_index)
            if lst[smallest_index] > lst[todo_index]:
                smallest_index = todo_index
                #print("swap happened. new smallest index:",smallest_index)
                #must come in first because in case of a 2 item list
                #once todo_index reaches 1, it gets all over. still needs a chance to SWAP at the last todo
            if todo_index == len(lst)-1:
                #print("time to actually swap")
                savedval = lst[smallest_index]
                lst[smallest_index] = lst[chosen_index]
                lst[chosen_index] = savedval
                #print("index number",chosen_index,"DONE!")
                #Pythonic way to swap elements: lst[smallest index], lst[chosen_index] = lst[chosen_index], lst[smallest_index]
                break
            else:
                continue
    #print("FINAL:",lst)
    return lst


#print(selection_sort([1, 2, 3, 4, 5]))
#[1, 2, 3, 4, 5]



"""
Insertion sort is a simple sorting algorithm that builds the final sorted list one item at a time.
Insertion sort has the following steps:
    1. Start from the second element in the list.
    2. Compare the current element with the previous element.
    3. If the current element is less than the previous element, swap them.
    4. If the current element is greater than or equal to the previous element, move to the next element.
    5. Repeat steps 2-4 until the beginning of the list is reached.
    6. Repeat steps 1-5 until the list is sorted.

Insertion sort has a time complexity of O(n^2) where n is the number of elements in the list.
Insertion sort has a space complexity of O(1) because it does not use any additional space.

Complete the 'insertion_sort' function below.
"""
def insertion_sort(lst):
    """
    Perform the insertion sort algorithm on a list.

    :param lst: List of unordered elements
    :return: Sorted list of elements

    Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time.
    It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.
    However, insertion sort provides several advantages:
    - Simple implementation
    - Efficient for (quite) small data sets, much like other quadratic sorting algorithms
    - More efficient in practice than most other simple quadratic (i.e., O(n^2)) algorithms such as selection sort or bubble sort
    - Adaptive, i.e., efficient for data sets that are already substantially sorted

    - basically like selection_sort in compiling smallest values
    - but NOT digit-based
    - instead more like bubble-sort -- smallest, then 2nd smallest piling to the right
    - "biggest/smallest based"
    - bubble sort but backwards actually
    """
    # TODO: Write your code here

    done = 0
    for start_index in range(len(lst)):
        # for each smallest number...
        #print("\nSTART_INDEX:",start_index)
        if start_index == 0:
            #print("SKIPPING 0")
            continue
        curr_index = start_index
    #write exceptions for list len = 0 or 1 to save time
        while True:
            #print("curr_index:",curr_index,"for",start_index-1,"smallest num")
            if curr_index <= 0:
                #print("At the very front")
                break
            #we can check at the beginning I guess? LMFAO
            if lst[curr_index] < lst[curr_index-1]:
                #print("Curr_index-1:",curr_index-1)
                #we swap now
                #print("Curr_index is smaller than in front")
                savedval = lst[curr_index]
                lst[curr_index] = lst[curr_index-1]
                lst[curr_index-1] = savedval
                curr_index = curr_index-1
                #print("New curr_index:",curr_index)
                #curr_index = lst.index(savedval) this is just redundant
                continue
            #print("Curr_index:",curr_index,"Curr_val:",lst[curr_index])
            #print("curr_index:", curr_index)
            #print("curr_index+1 :",curr_index+1,"for",lst)
            else:
                #moving onto the right one (curr_index + 1) if curr_index fails to be bigger
                break
            #to make this more efficient I could've just done a normal while loop though :(
    return lst

#print(insertion_sort([3, 2, 1]))
#[1, 2, 3]

def merge(left_list, right_list):
    """
    Merge two lists in a sorted manner.

    :param left_list: Sorted list of elements
    :param right_list: Sorted list of elements
    :return: Single sorted list combined from left_list and right_list

    This function assumes that `left_list` and `right_list` are sorted and merges them
    into a single sorted list in linear time.
    #different lens are OK :)
    """
    return_list = []
    # TODO: Implement merge
    while len(left_list) > 0 and len(right_list) > 0:
        left_item = left_list[0]
        right_item = right_list[0]
        if left_item > right_item:
            return_list.append(right_item)
            right_list.pop(0)
            #same thing as left_list.remove(item)
        elif left_item < right_item:
            return_list.append(left_item)
            left_list.pop(0)
        else:
            return_list.append(left_item)
            return_list.append(right_item)
            left_list.pop(0)
            right_list.pop(0)
    return_list.extend(left_list)
    return_list.extend(right_list)
    #one will be blank anyway
    return return_list


#print(merge([4],[1,3,7]))
#[1, 2, 3, 4, 5]


"""
Merge sort is a sorting algorithm that uses the divide and conquer approach.
Merge sort has the following steps:
    1. Divide the list into two halves.
    2. Sort each half recursively.
    3. Merge the two sorted halves.

Merge sort has a time complexity of O(n log n) where n is the number of elements in the list.
Merge sort has a space complexity of O(n) because it uses additional space to store the two halves of the list.

Complete the 'merge_sort' function below.
"""
def merge_sort(lst):
    """
    Perform the merge sort algorithm on a list.

    :param lst: List of unordered elements
    :return: Sorted list of elements

    Merge sort is a divide-and-conquer algorithm that works by recursively breaking down
    a problem into two or more sub-problems of the same or related type, until these become simple enough to be solved directly.
    The solutions to the sub-problems are then combined to give a solution to the original problem.
    """
    # TODO: Implement merge sort
    #RECURSIVE program
    #base case: len(chunk) = 1
    #recursive case: else, apply merge to each pair of same length

    if len(lst) <= 1:
        return lst

    while True:
        if len(lst) == 1:
            #print("single item list:",lst)
            return lst
        else:
            left_list = []
            right_list = []
            for item_index in range(len(lst)):
                #the one time I used "for item in lst". it failed
                #because lst.index(item) just looks for the FIRST instance of the same value
                #ok then
                item = lst[item_index]
                if item_index < len(lst)/2:
                #if list len = 5
                #list items = 0, 1, 2, 3, 4
                #5/2 = 2.5; 4/2 = 2
                #if list len = 7
                #list items = 0, 1, 2, 3, 4, 5, 6
                #7/2 = 3.5 (includes middle item 3); 6/2 = 3
                #I guess I'll do left big chomp
                    left_list.append(item)
                else:
                    right_list.append(item)
            #print("left_list:",left_list,"right_list:",right_list)
            #print("Merged val:", left_list,right_list)
            return merge(merge_sort(left_list), merge_sort(right_list))


#print(merge_sort([5, 4, 3, 2, 1]))
#should be [1, 2, 3, 4, 5]


"""
Test Cases ----------------------------------------------------------------------
"""
def test_linear_search():
    print('Testing linear_search()...', end='')
    numbers = [1, 2, 3, 4, 5]
    assert linear_search(numbers, 3) == 2
    assert linear_search(numbers, 6) == -1
    assert linear_search(numbers, 1) == 0
    assert linear_search(numbers, 5) == 4
    assert linear_search(numbers, 2) == 1
    assert linear_search(numbers, 4) == 3
    numbers2 = [34, 6, 8, 2, 4, 45, 78, 3, 86, 7]
    assert linear_search(numbers2, 45) == 5
    assert linear_search(numbers2, 86) == 8
    assert linear_search(numbers2, 7) == 9
    assert linear_search(numbers2, -23) == -1
    assert linear_search(numbers2, 1000) == -1
    print('Passed.')


def test_binary_search_iterative():
    print('Testing binary_search_iterative()...', end='')
    numbers = [1, 2, 3, 4, 5]
    assert binary_search_iterative(numbers, 3) == 2
    assert binary_search_iterative(numbers, 6) == -1
    numbers2 = [3, 6, 9, 12, 15, 47, 57, 68, 72, 84, 89, 91, 95, 99]
    assert binary_search_iterative(numbers2, 95) == 12
    assert binary_search_iterative(numbers2, 100) == -1
    assert binary_search_iterative(numbers2, 3) == 0
    assert binary_search_iterative(numbers2, 99) == 13
    assert binary_search_iterative(numbers2, 47) == 5
    assert binary_search_iterative(numbers2, 0) == -1
    print('Passed!')


def test_binary_search_recursive():
    print('Testing binary_search_recursive()...', end='')
    numbers = [1, 2, 3, 4, 5]
    assert binary_search_recursive(numbers, 3) == 2
    assert binary_search_recursive(numbers, 6) == -1
    numbers2 = [3, 6, 9, 12, 15, 47, 57, 68, 72, 84, 89, 91, 95, 99]
    assert binary_search_recursive(numbers2, 95) == 12
    assert binary_search_recursive(numbers2, 100) == -1
    assert binary_search_recursive(numbers2, 3) == 0
    assert binary_search_recursive(numbers2, 99) == 13
    assert binary_search_recursive(numbers2, 47) == 5
    assert binary_search_recursive(numbers2, 0) == -1
    print('Passed!')


def test_triangle_number():
    print('Testing triangle_number()...', end='')
    assert triangle_number(1) == 1
    assert triangle_number(2) == 3
    assert triangle_number(3) == 6
    assert triangle_number(4) == 10
    assert triangle_number(5) == 15
    assert triangle_number(6) == 21
    assert triangle_number(7) == 28
    assert triangle_number(8) == 36
    assert triangle_number(9) == 45
    assert triangle_number(10) == 55
    assert triangle_number(11) == 66
    assert triangle_number(12) == 78
    assert triangle_number(13) == 91
    assert triangle_number(14) == 105
    assert triangle_number(15) == 120
    assert triangle_number(16) == 136
    assert triangle_number(17) == 153
    assert triangle_number(18) == 171
    assert triangle_number(19) == 190
    assert triangle_number(20) == 210
    assert triangle_number(21) == 231
    assert triangle_number(22) == 253
    assert triangle_number(23) == 276
    assert triangle_number(24) == 300
    assert triangle_number(25) == 325
    assert triangle_number(26) == 351
    assert triangle_number(27) == 378
    assert triangle_number(28) == 406
    assert triangle_number(29) == 435
    assert triangle_number(30) == 465
    assert triangle_number(31) == 496
    assert triangle_number(32) == 528
    assert triangle_number(33) == 561
    assert triangle_number(34) == 595
    assert triangle_number(35) == 630
    assert triangle_number(36) == 666
    assert triangle_number(37) == 703
    assert triangle_number(38) == 741
    assert triangle_number(39) == 780
    assert triangle_number(40) == 820
    assert triangle_number(41) == 861
    assert triangle_number(42) == 903
    assert triangle_number(43) == 946
    assert triangle_number(44) == 990
    print("All test cases passed!")


def test_bubble_sort():
    print('Testing bubble_sort()...', end='')
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]
    assert bubble_sort([1, 2]) == [1, 2]
    assert bubble_sort([2, 1]) == [1, 2]
    assert bubble_sort([3, 2, 1]) == [1, 2, 3]
    assert bubble_sort([1, 3, 2]) == [1, 2, 3]
    assert bubble_sort([1, 2, 3]) == [1, 2, 3]
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert bubble_sort([3, 5, 8, 2, 9, 3, 0]) == [0, 2, 3, 3, 5, 8, 9]
    assert bubble_sort([3, 5, 8, -30, 2, 9, 3, 0, 1, -3, -2, -5]) == [-30, -5, -3, -2, 0, 1, 2, 3, 3, 5, 8, 9]
    print('Passed.')


def test_selection_sort():
    print('Testing selection_sort()...', end='')
    assert selection_sort([]) == []
    assert selection_sort([1]) == [1]
    assert selection_sort([1, 2]) == [1, 2]
    assert selection_sort([2, 1]) == [1, 2]
    assert selection_sort([3, 2, 1]) == [1, 2, 3]
    assert selection_sort([1, 3, 2]) == [1, 2, 3]
    assert selection_sort([1, 2, 3]) == [1, 2, 3]
    assert selection_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert selection_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert selection_sort([3, 5, 8, 2, 9, 3, 0]) == [0, 2, 3, 3, 5, 8, 9]
    assert selection_sort([3, 5, 8, -30, 2, 9, 3, 0, 1, -3, -2, -5]) == [-30, -5, -3, -2, 0, 1, 2, 3, 3, 5, 8, 9]
    print('Passed.')


def test_insertion_sort():
    print('Testing insertion_sort()...', end='')
    assert insertion_sort([]) == []
    assert insertion_sort([1]) == [1]
    assert insertion_sort([1, 2]) == [1, 2]
    assert insertion_sort([2, 1]) == [1, 2]
    assert insertion_sort([3, 2, 1]) == [1, 2, 3]
    assert insertion_sort([1, 3, 2]) == [1, 2, 3]
    assert insertion_sort([1, 2, 3]) == [1, 2, 3]
    assert insertion_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert insertion_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert insertion_sort([3, 5, 8, 2, 9, 3, 0]) == [0, 2, 3, 3, 5, 8, 9]
    assert insertion_sort([3, 5, 8, -30, 2, 9, 3, 0, 1, -3, -2, -5]) == [-30, -5, -3, -2, 0, 1, 2, 3, 3, 5, 8, 9]
    print('Passed.')


def test_merge_sort():
    print('Testing merge_sort()...', end='')
    assert merge_sort([]) == []
    assert merge_sort([1]) == [1]
    assert merge_sort([1, 2]) == [1, 2]
    assert merge_sort([2, 1]) == [1, 2]
    assert merge_sort([3, 2, 1]) == [1, 2, 3]
    assert merge_sort([1, 3, 2]) == [1, 2, 3]
    assert merge_sort([1, 2, 3]) == [1, 2, 3]
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert merge_sort([3, 5, 8, 2, 9, 3, 0]) == [0, 2, 3, 3, 5, 8, 9]
    assert merge_sort([3, 5, 8, -30, 2, 9, 3, 0, 1, -3, -2, -5]) == [-30, -5, -3, -2, 0, 1, 2, 3, 3, 5, 8, 9]
    print('Passed.')


def test_all():
    test_linear_search()
    test_triangle_number()
    test_binary_search_iterative()
    test_binary_search_recursive()
    test_bubble_sort()
    test_selection_sort()
    test_insertion_sort()
    test_merge_sort()
    print("SLAY ALL DAY")


if __name__ == '__main__':
    test_all()


#numbers = [1, 2, 3, 4, 5]
# print(binary_search_iterative(numbers, 3) == 2)
#print(binary_search_iterative(numbers, 6) == -1)