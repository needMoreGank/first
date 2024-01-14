import sys
sys.stdin = open("input_nextbase_jr.txt")
input = sys.stdin.readline


def dec_to_base(num, base):
    og_num = num
    #print("\ndec_to_base ops; base:",base,"num:",num)
    return_num = ""
    exp = 0
    while base**(exp+1) <= num:
        exp += 1
        #print("num:",num,"base**exp:",base**exp)
        #print("updated exp:",exp)

        #return_num += str(base // num)
        #adding a digit
    
    #print("final exp:",exp,"final digit:",base**exp)

    for e in range(exp + 1):
        return_num += str(num // base**(exp-e))
        num = num % (base**(exp-e))
    #print("num:",og_num,"converted_num:",return_num)
    return return_num

def base_to_dec(num, base):
    num = str(num)
    og_num = num
    #print("\nbase_to_dec ops; base:",base,"num:",num)
    return_num = 0
    exp = 0

    #reverse index in base char = exp
    #reverse index = do reverse for loop + 1
    #multiply each digit's value by base**index
    
    for c in range(len(num))[::-1]:
        char = num[c]
        exp = len(num)-c-1
        #print("char:",char,"exp of char:",exp)
        return_num += int(char) * base**exp

    #print("num:",og_num,"converted_num:",return_num)
    return return_num


def next_base(num_to_gen, base, start):
    compiled_digits = ""
    sum = 0
    curr_num = start
    for n in range(num_to_gen):
        #print(dec_to_base(curr_num, base))
        compiled_digits += str(dec_to_base(curr_num + n, base))
        #curr_num += 1
    #print("compiled_digits:",compiled_digits)
    for c in range(len(compiled_digits)):
        char = compiled_digits[c]
        sum += int(char)
    return sum





def main():
    for x in range(5):
        num, base, start = input().split(" ")
        num = int(num)
        base = int(base)
        start = int(start)
        print("\nLINE",x,num,base,start)
        print("final_sum:",str(next_base(num, base, base_to_dec(start, base))))


main()
