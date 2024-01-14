import sys
sys.stdin = open("input_bases.txt")
input = sys.stdin.readline

def alpha_to_num(alpha):
    if alpha.isnumeric():
        return int(alpha)
    if alpha == "A":
        return 10
    elif alpha == "B":
        return 11
    elif alpha == "C":
        return 12
    elif alpha == "D":
        return 13
    elif alpha == "E":
        return 14
    elif alpha == "F":
        return 15
    #else:
        #print(alpha)
        
    
def num_to_alpha(num):
    if num < 10:
        return num
    
    if num == 10:
        return "A"
    elif num == 11:
        return "B"
    elif num == 12:
        return "C"
    elif num == 13:
        return "D"
    elif num == 14:
        return "E"
    elif num == 15:
        return "F"
    

def bases(num, base, round_place):
    #identify digit "right" to the round_digit (just do +1 on index)
    #find place of actual round_digit by num.index(".") + round_digit
    #divide rightdigit by base
    #if quotient >= 0.5: round_digit +=1
    #else: round_digit += 0 (remain the same)

    num = str(num)

    round_digit_index = num.index(".") + round_place
    right_num = alpha_to_num(num[round_digit_index + 1])
    #handle alphabet right_num; convert to number

    #print("right_num:",right_num)
    quotient = right_num / base

    num = list(num)
    #print("num_list:",num)
    
    if quotient >= 0.5:

        new_round_digit = alpha_to_num(num[round_digit_index]) + 1
        #alpha_to_num is fancy int
        
        #print("new target digit val",new_round_digit)
        curr_index = round_digit_index

        while new_round_digit >= base:
            #trigger rounding up mechanism
            #print("rounding up to next digit.")
            num[curr_index] = "0"

            curr_index -= 1
            if num[curr_index].isalnum() != True:
                curr_index -= 1

            new_round_digit = alpha_to_num(num[curr_index]) + 1
            #print("".join(num))

        new_round_digit = str(num_to_alpha(new_round_digit))
        #print("new_round_digit:",new_round_digit)

        newindex = (len(num)-round_digit_index) * -1

        if curr_index < 0:
            num.insert(0, "1")
        else:
            num[curr_index] = new_round_digit
            #print("curr_index",curr_index)

        #back = num[round_digit_index+1:]
        #you discard the back!
        num = "".join(num)[:newindex + 1]
    
    else:
        #do nothing with new_round_digit!
        num = num[:round_digit_index+1]
        num = "".join(num)
    #print("ANSWER:")
    return num



def main():
    for l in range(10):
        number, base, round_place = input().split(", ")
        #print("\ninput:",number, base, round_place, end ="")
        number = number.replace(" ","")
        base = int(base)
        round_place = int(round_place)
        
        print(bases(number, base, round_place))

main()