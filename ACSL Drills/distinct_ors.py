from itertools import combinations

distincts = []
subarrays = []

def distinct_ors(vals):
    global distincts
    global subarrays
    for itemnum in range(len(vals)+1)[1::]:
        print("Num:",itemnum)
        curr_subarrays = combinations(vals,itemnum)
        for i in curr_subarrays:
            subarrays.append(i)
    
        print(subarrays)
    
    for num in range(len(subarrays)):
        curr_val = 0
        item = subarrays[num]
        print("item:",item)
        for c_num in range(len(item)):
            curr_val = (curr_val|item[c_num])

        distincts.append(curr_val)
        print("curr_val:",curr_val)
        print("distincts:",distincts)
    distincts = set(distincts)
    return len(distincts)



def main():
    vals = input().replace("[","").replace("]","")
    vals = vals.split(",")
    print(vals)
    for i in range(len(vals)):
        vals[i] = int(vals[i])
    
    print(distinct_ors(vals))
        

main()