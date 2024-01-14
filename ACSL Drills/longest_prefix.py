import sys
sys.stdin = open("longest_prefix.txt")
input = sys.stdin.readline

def longest_prefix(string):
    total_score = 0
    for c in range(len(string))[::-1]:
        curr_word = ""
        curr_score = 0
        #just does counting in reverse, not neg index
        char = string[c]
        curr_word += char
        #print("char:",char)
        for behind_c in range(len(string))[c+1:len(string):1]:
            behind_char = string[behind_c]
            #print("behind_char:",behind_char)
            curr_word += behind_char
        #print("\ncurr_word:",curr_word)

        for prefix_c in range(len(curr_word)):
            #print("prefix_c:",prefix_c)
            if curr_word[prefix_c] == string[prefix_c]:
                #print("prefix match.")
                curr_score += 1
            else:
                break
        
        #print("curr_score:",curr_score)
        total_score += curr_score
    #print("\ntotal_score:",total_score)
    return total_score
    



def main():
    for i in range(2):
        s = input().strip()
        print(longest_prefix(s))

main()