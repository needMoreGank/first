import sys
sys.stdin = open("input_scrabble_jr.txt")
input = sys.stdin.readline

letters_dict = {
    "A" : 1, "E": 1, "D":2, "R":2, "B":3, "M":3, "V":4, "Y":4, "J":8, "X":8
}

def calc_points(word, start_square_num):
    points = 0
    letters = word.split(", ")
    #print("letters:",letters)
    double_word = False
    triple_word = False

    for l in range(len(letters)):
        square_num = start_square_num + l
        #print("square_num:",square_num)
        letter = letters[l].strip()
        #print("letter:",letter)
        point = letters_dict[letter]
        if (square_num+3) % 6 == 0:
            #print("Double Letter qualified")
            point *= 2
        elif square_num % 5 == 0:
            #print("Triple letter qualified")
            point *= 3
        elif square_num % 7 == 0:
            #print("Double word qualified")
            double_word = True
        elif square_num % 8 == 0:
            #print("Triple word qualified")
            triple_word = True
        points += point
        #print("points update:",points)
    
    if double_word == True:
        points *= 2
    elif triple_word == True:
        points *= 3
    return points


def main():
    word = input().split(". ")[1]
    for x in range(5):
        start_square = int((input()).split(". ")[1])
        #print("\nstart_square:",start_square)
        print(str(x+1)+". "+str(calc_points(word, start_square)))

main()