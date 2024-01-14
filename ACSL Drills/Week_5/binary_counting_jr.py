import sys
sys.stdin = open("input_binary_counting_jr.txt")
input = sys.stdin.readline

def char_to_bin(value):
    all_bins = ""
    for n in range(len(value)):
        char = value[n]
        ord_char = ord(char)
        #print("ord_char:",ord_char)
        bin_char = bin(ord_char)[2:].zfill(8)
        #print("bin_char:",bin_char)
        all_bins += bin_char
        #print("all_bins update:",all_bins)
    return all_bins

def bin_conv(dec):
    #print(str(bin(int(dec))))
    return str(bin(int(dec)))[2:]
        
def find_bound(all_bins):
    dec_curr = "0"
    #print(bin_conv(dec_curr))
    while all_bins.find(bin_conv(dec_curr)) != -1:
        #print("BABA")
        #print("dec:",dec_curr,"bin:",bin_conv(dec_curr), "can be found! Advancing.")
        dec_curr = str(int(dec_curr)+1)
    else:
        #print("dec:",dec_curr,bin_conv(dec_curr),"could not be found. bound found")
        return str(int(dec_curr)-1)


def main():
    for n in range(5):
        print("\n",find_bound(char_to_bin(input())))

main()