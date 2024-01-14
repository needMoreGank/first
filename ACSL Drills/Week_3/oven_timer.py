def my_oct2bin(oct):
    print("oct:",oct)
    bin = ""
    bin += str(oct//4)
    oct = oct % 4
    bin += str(oct //2)
    oct = oct%2
    bin += str(oct//1)
    print("curr_bin:",bin)
    return bin

def oct2bin(oct):
    ret = []
    for n in range(3):
        #working backwards.
        ret.append(oct%2)
        oct = oct // 2
        #remove the appended val.
    ret = map(str, ret[::-1])
    #map = apply the function (1st param) into every item of the iterable (2nd param)
    ret = "".join(ret)
    return ret

def bin_to_oct(bin):
    bin = str(bin)
    while len(bin) % 3 != 0:
        bin = "0" + bin
    else:
        print("padding done")
    bin = int(bin)
    for n in range(0, len(bin), 3):
        sliced = bin[n:n+3]
        #print(bin2oct(sliced))

def oktalni2(oct):
    oct = str(oct)
    returnval = ""
    for digit_num in range(len(oct)):
        digit = oct[digit_num]
        returnval += oct2bin(int(digit))
    returnval = returnval.lstrip("0")
    print(returnval)


oktalni2(314)
