import sys
sys.stdin = open("cabbage_in_danger.txt")
open = sys.stdin.readline

from itertools import combinations
import copy


def grid_print(grid_list):
    for line in grid_list:
        for space in line:
            print(space + " ", end="")
        print("")
    print("")



def cabbage_in_danger(grid_list):
    empty_list = [] #0
    wall_list = [] #1
    fire_list = [] #2

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    for l in range(len(grid_list)):
        #print("l:",l)
        line = grid_list[l]
        for s in range(len(line)):
            #print(len(line),s)
            space = line[s]
            #print("s:",s,"l:",l)
        
            if space == "0":
                empty_list.append((s,l))
            elif space == "1":
                wall_list.append((s,l))
            elif space == "2":
                fire_list.append((s,l))
    
    #print(empty_list)

    combos_list = combinations(empty_list, 3)
    max_safe_count = 0
    #curr_grid_list = copy.deepcopy(grid_list)
    #print(combos_list)

    # 1: mold the graph w/ desired coords
    # 2: 

    #coord_duo = list(combos_list)[0]
    #for coord_combo in combos_list:
    for i in range(2):
        coord_combo = list(combos_list)[0]
        #print(coord_combo)
        curr_safe_count = 0
        #for every PACKAGE of 3 coords
        curr_grid_list = copy.deepcopy(grid_list)


        #for every combo:
        for x, y in coord_combo:
            curr_grid_list[y][x] = "1"
        

        for l in range(len(curr_grid_list)):
            curr_safe_count = 0
            #traverse list to look for fire space
            #print(l)
            line = curr_grid_list[l]
            #print(line)
            for s in range(len(line)):
                space = line[s]
                #print(space)
                #print(space)
                x, y = s, l
                if space == "2":
                    #print(x,y,"is a fire space")
                    #fire space
                    for dir in range(4):
                        curr_x = x + dx[dir]
                        curr_y = y + dy[dir]
                        #print("curr_x:",curr_x,"curr_y:",curr_y)
                        if curr_x < 0 or curr_x >= len(line) or curr_y < 0 or curr_y >= len(curr_grid_list):
                            #out of bounds
                            #print("out of bounds")
                            continue
                    #y always comes first

                        if curr_grid_list[curr_y][curr_x] == "0" or curr_grid_list[curr_y][curr_x] == "2":
                            #empty; fire can spread OR fire is already there
                            curr_grid_list[curr_y][curr_x] = "2"
                            continue

                        elif curr_grid_list[curr_y][curr_x] == "1":
                            #print(curr_y,curr_x,"is a wall -- no action taken")
                            #wall! fire is stopped in this direction.
                            continue
                    
                    print("updated curr_grid_list after coords(", x , y, "):")
                    grid_print(curr_grid_list)
        

            #print("updated curr_grid_list:")
            #grid_print(curr_grid_list)

        for line in curr_grid_list:
            for space in line:
                if space == "0":
                    curr_safe_count += 1

        if curr_safe_count > max_safe_count:
            print("max_safe_count UPDATED! old:",max_safe_count,"new:",curr_safe_count)
            print("curr_grid_list for this combo:")
            grid_print(curr_grid_list)
        max_safe_count = max(max_safe_count, curr_safe_count)




    return max_safe_count




        
        
        



        
    


    



def main():
    ver_len, hor_len = input().split(" ")
    ver_len = int(ver_len)
    hor_len = int(hor_len)
    grid_list = []
    for v in range(ver_len):
        #print(v)
        line = input().split(" ")
        grid_list.append(line)
    #print("updated grid_list:",grid_list)
    print("\nGiven grid:")
    grid_print(grid_list)
    print(cabbage_in_danger(grid_list))

main()