import sys
sys.stdin = open("string_formatting.txt")
input = sys.stdin.readline


def string_formatting(format, val):
    


def main():
    num_test_cases = int(input())
    for i in range(3):
        format, val = input().strip().split(" ")
        print(string_formatting(format, val))