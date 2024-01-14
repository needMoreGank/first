char_dict = {
    "(":")",
    ")":"("
}


def validstr(string):
    #front includes middle in odds
    front = []
    back = []
    mid = (len(string)-1)/2+1
    front = string[0:mid+1]
    back = string[mid+1:len(string)]


    print("front:",front,"back:",back)
    
    
        




def main():
    string = input()
    print(validstr(string))

main()