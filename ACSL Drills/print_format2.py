import sys
sys.stdin = open("print_format2.txt")
input = sys.stdin.readline

def print_format(format, val):

    if "." in val:
        front = 
        #use .find!

def main():
    num_cases = int(input().strip())
    for c in range(num_cases):
        format, val = input().strip().split(" ")
        print("result:",print_format(format,val))