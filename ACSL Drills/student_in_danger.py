import sys
sys.stdin = open("student_in_danger.txt")
input = sys.stdin.readline

from itertools import combinations

"""
Problem-solving plan
Given teacher's position [x,y],
every space w/ same x OR y is INDANGER.
UNLESS obstacle:
if LEFT of teacher:
if obs' x < teachers' x:
every space which space's x < obs will be SAFE.
similarly,
RIGHT -- elif obs' x > teachers' x:
if space's x > obs, space = SAFE

UP -- elif obs' y > teachers' y:
if space's y > obs, space = SAFE

DOWN -- elif obs' y < teachers' y:
if space's y < obs, space = SAFE

1. get ALL 3 Empty combinations (order does NOT matter; same-order dupes are counted as 1)
2. FILTER the ALL combinations to the only obs-useful ones (at least 1's x or y matches w/ teacher's)

"""

def filter_valid_obs_combos(obs_combos):
    for combo in obs_combos:
        pass



def student_in_danger(grid_list):
    empty_list = []
    teacher_list = []
    student_list = []

    for l in range(len(grid_list)):
        line = grid_list[l]
        for s in range(len(line)):
            space = line[s]
            if space == "X":
                empty_list.append((s, l))
            elif space == "T":
                teacher_list.append((s, l))
            elif space == "S":
                student_list.append((s, l))

    obs_combos = combinations(empty_list, 3)
    print("all obs_combos:",obs_combos)
    valid_obs_combos = filter_valid_obs_combos(obs_combos)
    


def main():
    #for test_case in range(int(input())):
    input()
    for test_case in range(1):
        grid_list = []
        for grid_len in range(int(input())):
            line_list = input().strip().split(" ")
            grid_list.append(line_list)
        #print("updated grid_list:",grid_list) all good!
        student_in_danger(grid_list)


main()