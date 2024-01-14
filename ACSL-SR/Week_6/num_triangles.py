'''
Numeral Triangle

Name: <your name>
'''
#
# Complete the 'sumOfLastRow' function below.
#
# The function is expected to return a CHARACTER.
# The function accepts following parameters:
#  1. STRING s: starting #
#  2. STRING d: delta (increase amount)
#  3. INTEGER r: number of rows
#sumOfLastRow("A","9",5)
# # of items in last row (focus) = also the # of rows

def sumOfLastRow(starting, delta, rows):
    #triangle_num = 0
    last_row = []
    return_sum = 0
    noinf = 0

    starting = hex_to_dec(starting)
    delta = hex_to_dec(delta)

    above_items = int(rows * (rows + 1)/2) - rows
    #print("# of total items:",total_items)

    #triangle_num += starting
    formula_build_triangle(starting,delta, above_items, last_row, rows)
    
    #for item in triangle[:-rows-1:-1]:
    #    last_row.append(dec_to_hex(item))

    #print("last_row:",last_row)

    for item_num in range(len(last_row)):
        item = last_row[item_num]
        #print("\n\nitem:",item)
        current_sum = truncate_hex_sum(str(item))
        #print("current_sum:",current_sum)
        return_sum += current_sum
        #print("return_sum dec:",return_sum)

    return_sum = dec_to_hex(return_sum)
    #print("return_sum hex:",return_sum)

    #print("return_sum:",return_sum,"return_sum length:",type(return_sum))

    while len(return_sum) > 1:
        if noinf > 20:
            print("INFINITY")
            return
        #print("len(num):",len(return_sum))
        return_sum = truncate_hex_sum(return_sum)
        #print("return_sum dec:",return_sum)   
        return_sum = dec_to_hex(return_sum)       
        #print('return_sum_hex:',return_sum)                     

        noinf += 1

    return return_sum

def formula_build_triangle(starting, delta, above_items, last_rows, rows):
    #get the sum of all the numbers preceding
    #so that the "starting num" is the 1st item of the last row

    first_num = above_items * delta + starting

    for i in range(rows):
        #print("first_num to be appended:",first_num)
        #print("hex rep:",dec_to_hex(first_num))
        last_rows.append(dec_to_hex(first_num))
        first_num += delta

def iterative_build_triangle(delta, total_items, triangle_num, last_row, rows):
    for order in range(total_items)[-1]:
        #total_items = 0 ~ last_index + 1
        #0-based total_items and the 1st item is already done

        #rows = 4
        # 1 2 3 4
        #ex: 1~10 (1-based)
        #10 is total_items
        #counted:0~9 (0-based)
        #6,7,8,9
        triangle_num += delta
        if order > total_items-1 - rows:
            last_row.append(dec_to_hex(triangle_num))
            #print("last_row update:",last_row)
        
    #print("iterative build triangle done.")

def recursive_build_triangle(delta, total_items, triangle):
    if len(triangle) == total_items:
        #both is final_index + 1
        #print("the last item has been processed")
        return triangle

    #print("# to append:",triangle[-1]+delta)

    triangle.append(triangle[-1] + delta)
    #print("current triangle:",triangle)
    recursive_build_triangle(delta, total_items, triangle)

def dec_to_hex(dec):
    #print("dec_to_hex ops")
    #print("dec:",dec)
    hex = ""
    exp = 0
    while 16 ** (exp+1) <= dec:
        exp += 1
        #print("updated exp:",exp)
        #will cut off once the larger amount is detected

    #ex num:20
    #exp:1

    for i in range(exp+1)[::-1]:
        #print("dividing",dec,"by",16 ** i)
        digit = dec // 16 ** i
        #print("digit:",digit)
        dec -= digit * 16 ** i
        if digit == 10:
            digit = "A"
        elif digit == 11:
            digit = "B"
        elif digit == 12:
            digit = "C"
        elif digit == 13:
            digit = "D"
        elif digit == 14:
            digit = "E"
        elif digit == 15:
            digit = "F"
        else:
            digit = str(digit)
        if digit == "0":
            #str adding literally adds 0 too
            pass
        else:
            hex += digit
        #print("updated hex:",hex)
        #print("updated dec:",dec)
    return hex

def hex_to_dec(hex):
    #hex is str
    #print("hex_to_dec ops")
    hex = str(hex)
    #print("hex:",hex)
    dec = 0
    for char in range(len(hex))[::-1]:
        #print("char num:",char)
        digit = hex[char]
        #print("digit:",digit)
        
        if digit == "A":
            digit = 10
        elif digit == "B":
            digit = 11
        elif digit == "C":
            digit = 12
        elif digit == "D":
            digit = 13
        elif digit == "E":
            digit = 14
        elif digit == "F":
            digit = 15
        else:
            digit = int(digit)
        
        #print("current digit:",digit)
        #print("16 power:",char,"16 as exponent:",16 ** char)
        dec += digit * 16 ** char
        #print("dec now:",dec)
        #ex: 0 index digit will have 16 ** 0 (1) multiplied. mwahaha
    #print("HEX_TO_DEC DONE")
    return dec
    
def truncate_hex_sum(sum):
    truncated_sum = 0
    #print("sum about to be truncated:",sum)
    for char_num in range(len(sum))[::-1]:
        char = sum[char_num]
        #print("\nraw char:",char)
        char = hex_to_dec(char)
        #print("char:",char)
        truncated_sum += char
    #print("truncated_sum of",sum,":",truncated_sum)
    
    return truncated_sum

print(sumOfLastRow("A", "9", 5))


if __name__ == '__main__':
    '''
    Read test cases from stdin.
    To test your solution, make 'triangle_numeral_sample_data.txt'
    in the same directory as this file,
    paste the sample data from the question in that file,
    and run this code.
    (Sample data is also available below)
    '''
    import sys
    sys.stdin = open('triangle_numeral_sample_data.txt', 'r')

    for i in range(10):
        data = input().split()
        s = data[0]
        d = data[1]
        r = int(data[2])

        print("\n TEST CASE:",s,d,r)
        result = sumOfLastRow(s, d, r)

        print('Test Case #{}: {}'.format(i + 1, result))

    '''
    Your output on console should be:
    Test Case #1: 5
    Test Case #2: C
    Test Case #3: A
    Test Case #4: F
    Test Case #5: 5
    Test Case #6: 5
    Test Case #7: F
    Test Case #8: 3
    Test Case #9: A
    Test Case #10: E
    '''


# Sample data:
# Copy and paste this in 'triangle_numeral_sample_data.txt' without the triple quotes
'''
A 9 5
ABC F 4
BAD 50 10
FED ABC 25
184 231 35
ABE CAB 40
31415 92653 60
DEAF BED 72
BAD DAD 100
704 1776 244
'''





