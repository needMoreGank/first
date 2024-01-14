import sys
sys.stdin = open("wordcolumn.txt")
input = sys.stdin.readline

def wordcolumn(string):
    string_list = string.split(" ")
    column_list = []
    max_len = 0

    for word in string_list:
        max_len = max(max_len, len(word))
    #print("max_len:",max_len)

    for i in range(max_len):
        column_list.append("")

    #print(string_list)
    #print(column_list)

    for word in string_list:
        for c in range(len(word)):
            char = word[c]
            column_list[c] += char
            #print(column_list)
        for diff in range(max_len - len(word)):
            insert = diff + len(word)
            column_list[insert] += " "
    #print(column_list)
    
    for w in range(len(column_list)):
        column_list[w] = column_list[w].rstrip()

    #print(column_list)

    return column_list





def main():
    for i in range(3):
        s = input().strip()
        print(wordcolumn(s))

main()