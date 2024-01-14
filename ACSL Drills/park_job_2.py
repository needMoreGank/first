import sys
sys.stdin = open("park_job_2.txt")
input = sys.stdin.readline


def hex_to_dec(hex):
    #print("hex:",hex)
    if hex.isnumeric():
        return int(hex)
    else:
        #print('not numeric.')
        if hex == "A":
            return 10
        elif hex == "B":
            return 11
        elif hex == "C":
            return 12
        elif hex == "D":
            return 13
        elif hex == "E":
            return 14
        elif hex == "F":
            return 15
        elif hex == "G":
            return 16
        elif hex == "H":
            return 17


def park_job(loc, day, start, end):
    loc = int(loc)
    start = hex_to_dec(start)
    end = hex_to_dec(end)
    pay = 0
    #print("start:",start,"end:",end)

    hours = (end-start)/2
    

    if 100 <= loc <= 199:
        pay = 10 * min(hours, 5) + 5 * max(hours-5, 0)
    elif 200 <= loc <= 299:
        pay = 7.5 * min(hours, 6) + 15 * max(hours-6, 0)
    elif 300 <= loc <= 399:
        pay = 9.25 * min(hours, 4) + 10.5 * max(hours-4,0)
    elif 400 <= loc <= 499:
        if day == 1 or day == 7:
            pay = 13.5 * hours
        else:
            pay = 6.75 * hours
    elif 500 <= loc <= 599:
        pay = 8 * min(hours, 6) + 12 * max(hours-6,0)
        
    #hours = str(hours)
    print(pay)
    #hours = hours.rjust(5,"0")
    return pay






def main():
    num_test_cases = int(input())
    for i in range(num_test_cases):
        input_list = input().strip().split(" ")
        total_pay = 0
        days_list = []

        mid_index = int(len(input_list) / 2)
        
        days_list.append(input_list[0:mid_index])
        days_list.append(input_list[mid_index : len(input_list)])

        for d in days_list:
            day_pay = park_job(d[0],d[1],d[2],d[3])
            print("day_pay:",day_pay)
            total_pay += day_pay
        

        print("raw total_pay:",total_pay)
        total_pay = str(total_pay).ljust(5,"0")
        print("formatted total_pay:",total_pay)
        
        
        #print("#"+str(i+1)+" " + "$" + total_pay)

main()