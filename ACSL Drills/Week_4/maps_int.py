import sys
sys.stdin = open("input_maps_int.txt")
input = sys.stdin.readline

cities_dist = {
    "A":0, "B": 450, "C": 590, "D": 710, "E": 1030, "F": 1280, "G": 1360
}

road_dict = {
    #tells mph
    "I": 65, "H": 60, "M": 55, "S": 45
}

car_dict = {
    #tells gpm
    "C": 28, "M": 25, "F": 22, "V": 20
}

def calc_time(miles, mph):
    time = miles / mph
    #gives hours in decimals; ex: 2.5
    floatTime = time % 1
    #gives decimal part
    minTime = str(round(floatTime * 60)).zfill(2)
    hourTime = str(int(time // 1)).zfill(2)
    return hourTime + ":" + minTime
    
def calc_cost(gal, pricePerGal):
    return round(gal * pricePerGal, 2)

def main():
    for case in range(10):
        start, end, car, road, pricePerGal = input().strip().split(" ")
        pricePerGal = float(pricePerGal)
        print("input:",start,end,car,road,pricePerGal)
        #milesPerGal, pricePerGal, milesPerHour
        milesPerGal = car_dict[car]
        milesPerHour = road_dict[road]
        print("milesPerGal:",milesPerGal,"pricePerGal:",pricePerGal,"milesPerHour:",milesPerHour, "\n")
        miles = cities_dist[end] - cities_dist[start]
        print("miles:",miles)
        time = calc_time(miles, milesPerHour)
        print("time:",time)
        gal = miles / milesPerGal
        cost = "$" + str(calc_cost(gal, pricePerGal))
        print("cost:",cost,"\n")
        #print("\n")

main()

    