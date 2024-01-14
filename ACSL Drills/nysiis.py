import sys
sys.stdin = open("nysiis.txt")
input = sys.stdin.readline

rule_1_dict = {
    "MAC":"MC",
    "KN":"N",
    "K":"C",
    "PH":"F",
    "PF":"F",
    "SCH":"S"
}

rule_2_dict = {
    
}


def rule_processor(name, rule_dict):
    for counter_n in range(len(name)-1):
        print(len(name))
        print(counter_n)
        c_n = counter_n

        char = name[c_n]
        if char in rule_dict:
            name = name.replace(char, rule_dict[char])
            print("damn")
        if c_n < len(name)-1 and (char+name[c_n+1]) in rule_dict:
            #print("AMOGUS!!!")
            print(char+name[c_n+1])
            counter_n += len(char+name[c_n+1]) - len(rule_dict[char+name[c_n+1]])
            print("amog:",name)
            name = name.replace(char+name[c_n+1],rule_dict[char+name[c_n+1]])
            
        if c_n < len(name)-2 and char+name[c_n+1]+char+name[c_n+2] in rule_dict:
            counter_n += len(char+name[c_n+1]+char+name[c_n+2]) - len(rule_dict[char+name[c_n+1]+char+name[c_n+2]])
            name = name.replace(char+name[c_n+1]+char+name[c_n+2],rule_dict[char+name[c_n+1]+char+name[c_n+2]])
            
        print("current name:",name)
    return name
    

def nysiis(name):
    #og_name = name
    name = rule_processor(name, rule_1_dict)
    name = rule_processor(name, rule_2_dict)

    print("final name:",name)
            

    
def main():
    for x in range(5):
        nysiis(input().strip())
        
main()