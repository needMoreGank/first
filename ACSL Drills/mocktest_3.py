import sys
sys.stdin = open("mocktest_3.txt")
input = sys.stdin.readline

def binclock(hours, mins, secs):
    bin_hours = bin(hours)[2:].rjust(6, "0")
    print("bin_hours:",bin_hours)
    bin_mins = bin(mins)[2:].rjust(6, "0")
    bin_secs = bin(secs)[2:].rjust(6, "0")

    hor_clock = bin_hours+bin_mins+bin_secs
    ver_clock = ""

    for i in range(6):
        #print(i)
        ver_clock += bin_hours[i]
        ver_clock += bin_mins[i]
        ver_clock += bin_secs[i]
        print("ver_clock:",ver_clock)

    return ver_clock + " " + hor_clock

def main():
    for x in range(2):
        dec_hours, dec_mins, dec_secs = input().split(":")
        dec_hours = int(dec_hours)
        dec_mins = int(dec_mins)
        dec_secs = int(dec_secs)

        print(binclock(dec_hours, dec_mins, dec_secs))

main()
"""
011001100010100011 001010100101110001
000000000000000001 000000000000000001

011001100010100011 001010100101110001
000000000000000001 000000000000000001
"""