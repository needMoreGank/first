import sys
import string
sys.stdin = open("mocktest_2_2.txt")
input = sys.stdin.readline

val_to_alphabet_list = []
for i in range(26):
    val_to_alphabet_list.append(string.ascii_uppercase[i])

def val_to_alphabet(val):
    global val_to_alphabet_list
    index = val-10
    #because A=10, A's index is 0.
    return val_to_alphabet_list[index]


def dec_to_base(num, base):
    base_num = ""

    max_exp = 0
    max_digit_val = base**max_exp
    #print("max_digit_val:",max_digit_val)

    while base**(max_exp+1) <= num:
        max_exp += 1
        max_digit_val = base**max_exp
    #print("final max_exp:", max_exp, "final max_digit_val:",max_digit_val)

    for exp in range(max_exp+1)[::-1]:
        digit_val = base**exp
        base_num_currdigit_val = num // digit_val
        if base_num_currdigit_val < 10:
            base_num_currdigit_val = str(base_num_currdigit_val)
        elif base_num_currdigit_val >= 10:
            base_num_currdigit_val = val_to_alphabet(base_num_currdigit_val)

        base_num += base_num_currdigit_val


        num = num%digit_val #the remainder to operate on.
    
    #print("final base_num:",base_num)
    return base_num






def main():
    for x in range(5):
        number, base = input().split(" ")
        number = int(number)
        base = int(base)

        print(dec_to_base(number, base))

main()