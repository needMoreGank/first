import sys
inputfilename = "string_manager.txt"
sys.stdin = open(inputfilename)
input = sys.stdin.readline

from collections import deque

global mainstring
isRev = False

def init(mStr: str):
    global mainstring
    mainstring = deque(list(mStr.strip()))

def appendWord(mWord: str):
    global mainstring, isRev
    mWord = mWord.strip()

    if not isRev:
        for c in mWord:
            mainstring.append(c)
    else:
        for c in mWord:
            mainstring.appendleft(c)
        

def cut(k: int):
    global mainstring, isRev
    #k = # of chars to cut from the end
    if not isRev:
        mainstring = mainstring[:len(mainstring)-k]
    else:
        mainstring = mainstring[k:]

def reverse():
    global mainstring, isRev
    isRev = not isRev

def countOccurrence(mWord: str) -> int:
    global mainstring
    tempmainstring = list(mainstring)
    if isRev:
        tempmainstring = tempmainstring[::-1]
    print(tempmainstring)
    #print("mainstring len:",mainstring)
    count = 0
    for c_num in range(len(tempmainstring) - len(mWord)+1):
        #char = mainstring[c_num]
        print("".join(tempmainstring[c_num:c_num+len(mWord)]))
        if "".join(tempmainstring[c_num:c_num+len(mWord)]) == mWord:
            print("AMOGUS!")
            count += 1
    
    #print("count:",count)
    return count




CMD_INIT     = 1
CMD_APPEND   = 2
CMD_CUT      = 3
CMD_REVERSE  = 4
CMD_COUNT    = 5


def run():
    query_cnt = int(input())
    correct = False

    for q in range(query_cnt):
        inputs = iter(input().split())
        cmd = int(next(inputs))

        if cmd == CMD_INIT:
            mStr = next(inputs)
            init(mStr)
            correct = True

        elif cmd == CMD_APPEND:
            mWord = next(inputs)
            if correct:
                appendWord(mWord)

        elif cmd == CMD_CUT:
            k = int(next(inputs))
            if correct:
                cut(k)

        elif cmd == CMD_REVERSE:
            if correct:
                reverse()

        elif cmd == CMD_COUNT:
            mWord = next(inputs)
            print("word to find:",mWord)
            ret = -1
            if correct:
                ret = countOccurrence(mWord)
            
            ans = int(next(inputs))
            if ret != ans:
                print("ret:",ret,"vs ans:",ans)
                correct = False
                exit()

    return correct


def main():
    TC, MARK = map(int, input().split())
    for testcase in range(1, TC + 1):
        score = MARK if run() else 0
        print("#%d %d" % (testcase, score), flush = True)

if __name__ == '__main__':
    main()