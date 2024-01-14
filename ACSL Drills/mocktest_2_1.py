import sys
import string
sys.stdin = open("mocktest_2_1.txt")
input = sys.stdin.readline

alphabet_to_val_dict = dict.fromkeys(string.ascii_uppercase, 0)

count = 10
for alphabet in alphabet_to_val_dict:
    alphabet_to_val_dict[alphabet] = count
    count += 1

#print(alphabet_to_val_dict)

def alphabet_to_val(val):
    global alphabet_to_val_dict
    return alphabet_to_val_dict[val]


def base_to_dec(num, base):
    dec_num = 0
    for digit_place in range(len(num)):
        #reverse manually: first char is index len(num)-1
        val = num[len(num) - 1 - digit_place] # if c_num is 0, char is len(num) - 1

        if val.isnumeric():
            val = int(val)
        elif val.isalpha():
            val = alphabet_to_val(val)

        digit_val = base ** digit_place
        dec_num += val * digit_val

    #print("Final dec_num:",dec_num)
    return dec_num

"""
def convert(num, base):
    #num can have alphabets and numbers
    return base_to_dec(num, base)
"""

def main():
    for x in range(5):
        number, base = input().split(" ")
        base = int(base)
        #print("number:",number,"base:",base)
        print(base_to_dec(number, base))

main()