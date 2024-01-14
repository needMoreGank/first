import sys
sys.stdin = open("input_print_formatting_jr.txt")
# setting sys.stdin (variable-like aspect) to the file.
input = sys.stdin.readline

#we are redefining the function (Python knows input as a function)
#function of "input" gets changed to function of "sys.stdin.readline"
#so henceforth, every time we call "input", sys.stdin.readline instead gets executed.

def fillIn(format, val):
    return_val = ""
    for x in range(format.count("&") - (len(val)-val.count("-"))):
        #while val_len is too short than format_len:
        return_val += "*"
    return return_val


def fillStars(format, val):
    print("format:", format, "value:", val)
    init_val = val

    do_fillins = True

    #only look at left int side first

    #should come last
    
    if "$" in format:
        if "*" in format:
            val = fillIn(format, val) + "$" + val
        else:
            val = "$" + val
        
    else:
        val = fillIn(format, val) + val

    if "," in format:
        #strings are immutable though
        format_counter = 0
        for c in range(len(init_val)):
            c = (c + 1) * -1
            print("val is",val)
            if c % 3 == 0 and c != 0:
                print("c is",c)
                c -= format_counter
                print("updated c is",c)
                print("val[:c]:",val[:c],"val[c:]",val[c:])
                val = val[:c] + "," + val[c:]
                format_counter += 1

    if "-" in format:
        if "-" in val:
            val = val.replace("-", "")
            print("val:",val)
            val = val + "-"
        else:
            val = val + "*"


    return val
            
def main():
    for case in range(5): # 5 inputs total
        format, value = input().split(" ")
        print(str(fillStars(format, value.strip()))+ "\n")

main()