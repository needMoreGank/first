"""
import sys
sys.stdin = open("park_job.txt")
input = sys.stdin.readline
"""

def hex_to_dec(hex):
    #print("hex:",hex)
    if hex.isnumeric():
        return int(hex)
    else:
        #print('not numeric.')
        if hex == "A":
            return 10
        elif hex == "B":
            return 11
        elif hex == "C":
            return 12
        elif hex == "D":
            return 13
        elif hex == "E":
            return 14
        elif hex == "F":
            return 15
        elif hex == "G":
            return 16
        elif hex == "H":
            return 17


def park_job(loc, start, end):
    loc = int(loc)
    start = hex_to_dec(start)
    end = hex_to_dec(end)
    #print("start:",start,"end:",end)

    hours = (end-start)/2

    if 1 <= loc <= 9:
        return 10 * hours
    elif 10 <= loc <= 19:
        if hours <= 4:
            return hours * 8
        else:
            #hours > 4
            return 4 * 8 + (hours-4) * 12
    elif 20 <= loc <= 29:
        if hours <= 4:
            return hours * 12
        else:
            return 4 * 12 + (hours-4) * 24






def main():
    num_test_cases = int(input())
    for i in range(num_test_cases):
        l, s, e = input().strip().split(" ")
        
        print("$"+str(park_job(l,s,e)))

main()