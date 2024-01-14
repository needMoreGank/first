import sys
sys.stdin = open("input_acslball.txt")
input = sys.stdin.readline

player_val = {}

player_points = {}

points_list = []

x_points_list = []
y_points_list = []

x_player_goals = {}
x_player_attempts = {}
y_player_goals = {}
y_player_attempts = {}

zone2_points_list = []
zone1_points_list = []

zone2_points_dict = {}
zone1_points_dict = {}

def list_to_output_string(list):
    return_str = ""
    for p in range(len(list)):
        player = list[p]
        return_str += player
        if p != len(list)-1:
            return_str += ", "
    return return_str

def calc_points(val):
    total_points = 0
    for mult in range(4):
        mult += 1
        #to accurately do zone points
        total_points += int(val[mult-1]) * mult
        print("points:",val[mult-1],"zone mult:",mult, "total_points:",total_points)
    return total_points

def calc_attempts(val):
    raw_attempts = val[4]
    dec_attempts = int(raw_attempts, 16)
    print("hex_attempts:",raw_attempts, "dec_attempts:",dec_attempts)
    return dec_attempts


def calc_total_points_mean(player_points):
    total_points = 0
    for p in player_points:
        total_points += player_points.get(p)
    
    #print("final total_points:",total_points)
    return total_points / 10

def calc_total_points_median(points_list):
    #print("sorted points_list:",points_list)
    #print("2 middle vals:",points_list[4],points_list[5],"their average:",((points_list[4]+points_list[5])/2))

    return (points_list[4]+points_list[5])/2


def init_points_lists(player_points, points_list, x_points_list, y_points_list):
    counter = 0
    for p in player_points:
        points_list.append(player_points.get(p))
        if counter < 5:
            x_points_list.append(player_points.get(p))
        elif counter >= 5:
            y_points_list.append(player_points.get(p))
        
        counter += 1

    points_list.sort()
    #len 10s
    x_points_list.sort()
    y_points_list.sort()
    zone1_points_list.sort()
    zone2_points_list.sort()
    #len 5s
    #lowest to highest

    #print("points_list:",points_list, "x_points_list:",x_points_list,"y_points_list:",y_points_list)

    #purely functional
    return None

def val_search_key(dict, val, command = "MULT"):
    players_list = []
    for player in dict:
        if dict.get(player) == val:
            if command == "ONE":
                #print("ONE command.")
                return player
            else:
                players_list.append(player)
    else:
        return players_list

def team_high_scorers(player_points,x_points_list, y_points_list):
    high_x_points = x_points_list[4]
    high_y_points = y_points_list[4]
    #the last = the biggest, list is sorted.
    high_x_player = val_search_key(player_points,high_x_points, "ONE")
    high_y_player = val_search_key(player_points,high_y_points, "ONE")
    return high_x_player + ", " + high_y_player

def all_high_scorers(player_points,points_list):
    first_high_points, second_high_points = points_list[9],points_list[8]
    first_high_player = val_search_key(player_points, first_high_points, "ONE")
    second_high_player = val_search_key(player_points, second_high_points, "ONE")

    return first_high_player + ", " + second_high_player

def calc_total_scores(x_points_list, y_points_list):
    x_points_total = 0
    y_points_total = 0
    for i in x_points_list:
        x_points_total += i
        #no need for specifics, since this is brute i val add-ons w/o details
    for i in y_points_list:
        y_points_total += i

    return str(max(x_points_total, y_points_total)) + ", " + str(min(x_points_total, y_points_total))

def all_low_scorers(player_points, points_list):
    low_points = points_list[0]
    low_players_list = val_search_key(player_points, low_points)
    return list_to_output_string(low_players_list)

def x_high_percenter(x_player_goals, x_player_attempts):
    high_percenter_list = []
    high_percent = 0

    for player in x_player_goals:
        goals = x_player_goals.get(player)
        attempts = x_player_attempts.get(player)
        percent = goals / attempts
        if percent > high_percent:
            high_percenter_list.clear()
            high_percenter_list.append(player)
            high_percent = percent
        elif percent == high_percent:
            high_percenter_list.append(player)
        else:
            pass
    
    return list_to_output_string(high_percenter_list)

def y_low_percenter(y_player_goals, y_player_attempts):
    low_percenter_list = []
    low_percent = 2 #1 is whole -- goofy

    for player in y_player_goals:
        goals = y_player_goals.get(player)
        attempts = y_player_attempts.get(player)
        percent = goals / attempts
        if percent < low_percent:
            low_percenter_list.clear()
            low_percenter_list.append(player)
            low_percent = percent
        elif percent == low_percent:
            low_percenter_list.append(player)
        else:
            pass
    
    #print(low_percenter_list)
    
    return list_to_output_string(low_percenter_list)
            

def calc_goals(val, zone2_points_list, zone1_points_list):
    total_goals = 0
    for n in range(4):
        #to accurately do zone points
        total_goals += int(val[n])

        if n == 1:
            zone2_points_list.append(int(val[n]))
        elif n == 0:
            #if Zone 1
            zone1_points_list.append(int(val[n]))
    return total_goals

def zone2_high_goalers(zone2_points_dict, zone2_points_list):
    #"points", but zone2 multipliers are just same -- do goal count

    high_goals = zone2_points_list[9]
    #print("high_goals:",high_goals)


    return list_to_output_string(val_search_key(zone2_points_dict, high_goals))

def zone1_high_goalers(zone1_points_dict, zone1_points_list):
    #"points", but zone2 multipliers are just same -- do goal count

    high_goals = zone1_points_list[9]
    #print("high_goals:",high_goals)


    return list_to_output_string(val_search_key(zone1_points_dict, high_goals))

def main():
    for l in range(10):
        player, val = input().strip().split(", ")
        print("\n"+player+", "+val)
        player_val[player] = val
        player_points[player] = calc_points(val)
        if l < 5:
            x_player_goals[player] = calc_goals(val, zone2_points_list, zone1_points_list)
            x_player_attempts[player] = calc_attempts(val)
        elif l >= 5:
            y_player_goals[player] = calc_goals(val, zone2_points_list, zone1_points_list)
            y_player_attempts[player] = calc_attempts(val)
        
        zone1_points_dict[player] = zone1_points_list[l]
        zone2_points_dict[player] = zone2_points_list[l]

    print("\n"+"OUTPUTS")

    init_points_lists(player_points, points_list, x_points_list, y_points_list)

    #1
    print(calc_total_points_mean(player_points))
    print(calc_total_points_median(points_list))

    print(team_high_scorers(player_points, x_points_list,y_points_list))
    print(all_high_scorers(player_points, points_list))
    print(calc_total_scores(x_points_list, y_points_list))
    print(all_low_scorers(player_points, points_list))
    print(x_high_percenter(x_player_goals, x_player_attempts))
    print(y_low_percenter(y_player_goals, y_player_attempts))
    print(zone2_high_goalers(zone2_points_dict, zone2_points_list))
    print(zone1_high_goalers(zone1_points_dict, zone1_points_list))


    
        


main()