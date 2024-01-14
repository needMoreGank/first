import sys
sys.stdin = open("acslletters.txt")
input = sys.stdin.readline

def main():
    #first just do 1

    sentence = input().strip()
    print("cleaned_sentence:",sentence)
    sentence_list = []

     

main()