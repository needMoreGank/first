import sys
sys.stdin = open("input_num_trans_jr.txt")
input = sys.stdin.readline
#read line of the opened input file

def digit_trans_small(digit, num, trans, pos):
    sum = str(digit + trans)
    num[-1 * pos] = sum[-1]
    

def digit_trans_big(digit, num, trans, pos):
    pass

def main():
    for case in range(6):
        num, pos, trans = input().split(" ")
        num = list(num)
        pos = int(pos)
        trans = int(trans)
        print("num:",num,"pos:",pos,"trans:",trans)
        digit = num[-1 * pos]
        print("digit:",digit)

        if 0 <= digit <= 4:
            digit_trans_small(digit, num, trans, pos)
        elif 5 <= digit <= 9:
            digit_trans_big(digit, num, trans, pos)

main()