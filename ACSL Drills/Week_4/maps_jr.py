import sys
sys.stdin = open("input_maps_jr.txt")
input = sys.stdin.readline

cities_dist = {
    "A":0, "B": 450, "C": 590, "D": 710, "E": 1030, "F": 1280, "G": 1360
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
    milesPerGal, pricePerGal, milesPerHour = map(float, input().split(" "))
    print("milesPerGal:",milesPerGal,"pricePerGal:",pricePerGal,"milesPerHour:",milesPerHour, "\n")
    for case in range(5):
        start, end = input().strip().split(" ")
        print("input:",start,end)
        miles = cities_dist[end] - cities_dist[start]
        print("miles:",miles)
        time = calc_time(miles, milesPerHour)
        print("time:",time)
        gal = miles / milesPerGal
        cost = "$" + str(calc_cost(gal, pricePerGal))
        print("cost:",cost)
        print("\n")

main()

    