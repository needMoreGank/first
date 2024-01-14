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
        curr_dig = num // base **(exp-e)
        #current CONVERTED TO DEC digit
        if curr_dig <= 9:
            curr_dig = str(curr_dig)
        else:
            if curr_dig == 10:
                curr_dig = "A"
            elif curr_dig == 11:
                curr_dig = "B"
            elif curr_dig == 12:
                curr_dig = "C"
            elif curr_dig == 13:
                curr_dig = "D"
            elif curr_dig == 14:
                curr_dig = "E"
            elif curr_dig == 15:
                curr_dig = "F"

        return_num += curr_dig
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
        #print("char:",char)
        #print("num:"+num+"ok")

        if char.isnumeric():
            char = int(char)
        else:
            if char == "A":
                char = 10
            elif char == "B":
                char = 11
            elif char == "C":
                char = 12
            elif char == "D":
                char = 13
            elif char == "E":
                char = 14
            elif char == "F":
                char = 15
        #print("dec_char:",char)
        return_num += char * base**exp


    #print("num:",og_num,"converted_num:",return_num)
    return return_num


def next_base(num_to_gen, base, start):
    compiled_digits = ""
    sum = 0
    curr_num = start
    for n in range(num_to_gen):
        #print(dec_to_base(curr_num, base))
        compiled_digits += str(dec_to_base(curr_num + n, base))
        #compiled_digits += "\\"
        #curr_num += 1
    #print("compiled_digits:",compiled_digits)

    
    occ_dict = {}
    
    for n in range(base):
        if n <= 9:
            n = str(n)  
        else:
            if n == 10:
                n = "A"
            elif n == 11:
                n = "B"
            elif n == 12:
                n = "C"
            elif n == 13:
                n = "D"
            elif n == 14:
                n = "E"
            elif n == 15:
                n = "F"
        
        occ_dict[n] = 0

    
    for char in compiled_digits:
        occ_dict[char] += 1

    #print("occ_dict:",occ_dict)
    
    num_max = max(occ_dict, key = occ_dict.get)
    

    return occ_dict.get(num_max)
    #"""





def main():
    for x in range(5):
        num, base, start = input().strip().split(" ")
        num = int(num)
        base = int(base)
        print("\nLINE",x,num,base,start)
        print("num_occs:",str(next_base(num, base, base_to_dec(start, base))))


main()
