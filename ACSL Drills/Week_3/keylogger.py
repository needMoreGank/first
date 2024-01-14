import sys
sys.stdin = open("keyloggerin.txt")
input = sys.stdin.readline

from collections import deque

N = int(input())
# of test cases
for n in range(N):
    string = input().strip()
    left = list()
    right = deque([])
    #popleft, appendleft
    #for n in range(len(string)):
        #left.append(string[n])

    for c in string:
        if c == "<":
            if len(left) > 0:
                right.appendleft(left.pop())
        elif c == ">":
            if len(right) > 0:
                left.append(right.popleft())
        elif c == "-":
            if len(left) > 0:
                left.pop()
        else:
            left.append(c)
        #print("left:",left)
        #print("right:",right)
    ans = ""
    for item in left:
        ans += item
    for item in right:
        ans += item
    print(ans)
            