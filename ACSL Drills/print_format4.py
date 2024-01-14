import sys
sys.stdin = open("print_format4.txt")
input = sys.stdin.readline

def print_format(str,start,length):
    start = int(start)
    length = int(length)
    #print("\nstart:",start,"len:",length)
    start_index = 0
    end_index = 0
    if start >= 0:
        start_index = start
    elif start < 0:
        start_index = len(str) + start
        #so that if len=4 and str=-1, start_index is 3 (last index)
    
    #print("start_index:",start_index)

    if length > 0:
        end_index = start+length-1 #EXclusive
        #start = 2, len = 8 = exclusive index at 10
    elif length < 0:
        end_index = len(str)+length-1 #also EXclusive
    elif length == 0:
        end_index = len(str)
    #print("end_index:",end_index)

    #print("result:",str[start_index:end_index])

    return str[start_index:end_index+1]


def swea(result,c,s):
    return "#"+str(c)+"."+str(s)+" "+result

def main():
    num_cases = int(input())
    for c in range(num_cases):
        str = input().strip()
        num_subs = int(input())
        for s in range(num_subs):
            start, length = input().strip().split(", ")
            result = print_format(str,start,length)
            print(swea(result,c+1,s+1))


main()