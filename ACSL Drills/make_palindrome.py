import math

"""
Given s (as string)

Can add chars in FRONT of s.

Return shortest palindrome possible via above method.
"""

"""
input: abcecbaa
output: aaacecaaa

input: abcd
output: dcbabcd

input: dedcba
output: abcdedcba

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

def isSym(start_l, start_r, last_index, string):
    #left of center and right of center
    curr_l = start_l
    curr_r = start_r

    while curr_l > 0:
        curr_l -= 1
        curr_r += 1
        #print(string[curr_l],string[curr_r])
        if string[curr_l] == string[curr_r]:
            continue
        else:
            return False 
    else:
        #print("last curr_r (NOT rejected):",string[curr_r])
        missing_phrase = string[curr_r+1:last_index+1]
        #print("missing_phrase:",missing_phrase)
        return missing_phrase[::-1]

    


def brute_make_Palindrome(string):
    return_string = string
    noFirst = True
    for c in string:
        if noFirst == False:
            return_string = c+return_string
        else:
            noFirst = False
    return return_string

def canPalindrome(string):
    """
    find the "center" of symmetry (may have 1 in between or none)
    start spreading out to see if they continue to match
    as soon as one can't, hard exit and hard duplicate
    if all pass but runs out of words (at left), add as needed

    repeat this until all possible "centers" are exhausted
    """
    last_index = len(string)-1

    for c in range(len(string)-2):
        #print("string[c]:",string[c],"string[c+1]",string[c+1],"string[c+2]:",string[c+2])
        if string[c] == string[c+1]:

            missing_phrase = isSym(c, c+1, last_index, string)
            #print("missing_phrase:",missing_phrase)
            if missing_phrase == False:
                #print("BRUH.")
                continue
            else:
                #print("SLAY")
                return missing_phrase + string
        elif string[c] == string[c+2]:
            missing_phrase = isSym(c, c+2, last_index, string)
            #print("missing_phrase:",missing_phrase)
            if missing_phrase == False:
                #print("BRUH.")
                continue
            else:
                #print("SLAY")
                return missing_phrase + string
    else:
        #print("no center in sight")
        return brute_make_Palindrome(string)
        

    


def main():
    s = input()
    print(canPalindrome(s))

main()