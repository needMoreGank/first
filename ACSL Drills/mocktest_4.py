import sys
sys.stdin = open("mocktest_4.txt")
input = sys.stdin.readline

def main():
    for x in range(4):
        whites_locs = []
        blacks_locs = []
        inputval = input().split(" ")
        num_whites = int(inputval[0])
        for i in range(num_whites)[1:]:
            print(i)
            whites_locs.append(int(inputval[i]))

        num_blacks = int(inputval[num_whites+1])
        for i in range(num_blacks)[num_whites+2:]:
            blacks_locs.append(int(inputval[i]))
        print("num_whites:",num_whites,"whites_locs:",whites_locs,"num_blacks:",num_blacks,"blacks_locs:",blacks_locs)





main()

