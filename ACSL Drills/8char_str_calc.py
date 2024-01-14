import sys
sys.stdin = open("8char_str_calc.txt")
input = sys.stdin.readline

def str_calc(op, str):
    #print("\nop:",op,"str:",str)
    if op == "DIVIDE":
        mid_index = int(len(str) / 2)
        front = str[0:mid_index]
        back = str[mid_index:len(str)]
        return front + front + " and " + back + back
    elif op[0:3] == "ADD":
        n = int(op[3])
        first = str[0:n]
        str = first + first + str[n:]
        #print("not cut off str:",str)
        return str[0:8]
    elif op[0:8] == "SUBTRACT":
        n = int(op[8])
        str = str[n:]
        print("not rep'd str:",str)
        if len(str) >= n:
            str = str + str[len(str)-n:]
        elif len(str) < n:
            str = str+str
       
        print("not cut off str:",str)
        return str[0:8]
    elif op == "UNION":
        front,back = str.split(" ")
        #print("raw front:",front,"back:",back)
        front = front[4:8]
        back = back[0:4]
        
        return front+back
    elif op == "INTERSECT":
        front,back = str.split(" ")
        #print("raw front:",front,"back:",back)
        front = front[0:2] + front[6:8]

        back = back[0:2] + back[6:8]
        return front+back

def swea(result,q_num):
    return "#"+str(q_num)+" "+result

def main():
    num_cases = int(input())
    for n in range(num_cases):
        input_str = input()
        operation, string = input_str.strip().split(" ",1)
        result = str_calc(operation, string)
        print(swea(result,n+1))

main()


