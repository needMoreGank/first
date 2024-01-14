import math
def main():
    string = input()
    print(canPalindrome(string))



"""
isPalindrome after deleting 0 or 1 letters?

To-do
Case 1: is already Palindrome
- make a palindrome function
Case 2: is not yet Palindrome
- create case for every 1 char deleted. input the new word into the palindrome
- if still after that not isPalindrome, return false
"""

"""
a b a
0 1 2

word len: 3
2 / 2 = 1 (if len is 3)
3 / 2 = 1.5 (if len is 4)
"""

def isPalindrome(string):
    lastindex = len(string)-1
    #print("last index number of input:",lastindex)
    for c in range(math.ceil(lastindex / 2)):
        curr_char = string[c]
        mirror_char = string[-1*(c+1)]
        #print("curr_char:",curr_char,"mirror_char:",mirror_char)
        if curr_char == mirror_char:
            #print("continue")
            continue
        else:
            #print("fail")
            return False
    else:
        return True


def canPalindrome(string):
    if isPalindrome(string):
        #print("SLAY!")
        return True
    else:
        for c in range(len(string)):
            new_word = string[0:c] + string[c+1:len(string)]
            if isPalindrome(new_word):
                return True
            else:
                continue
        else:
            return False

main()