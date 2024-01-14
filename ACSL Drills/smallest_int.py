import sys
"""
Given num (as string) and k (as int),

Give smallest possible int after removing k consecutive digits from num.

To-do
1. for loop to remove k-len sections (as string) from num
2. convert created num to int
3. compare created num to current smallest_int (w/ max())
4. return final smallest_int
"""

def smallest_int(num, d):
    d = int(d)
    min_num = sys.maxsize
    #if d=1, proceed as normal (delete 0)
    #if d=2, skip 1 last one (delete 1)
    #delete (d-1)
    for c_num in range(len(num)-(d-1)):
        curr_num = num[0:c_num] + num[c_num+d:len(num)]
        #print("curr_num:",curr_num)
        if curr_num == "":
            curr_num = 0
        else:
            curr_num = int(curr_num)
        min_num = min(min_num, curr_num)
    return min_num




def main():
    num, k = input().split(" ")
    print(smallest_int(num, k))

main()