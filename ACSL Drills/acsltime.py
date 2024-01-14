#lost 5mins

#everything since Jan 1 2019 00:00:00

#5/25, 2019, 12:00:00 = start
#1 day = 25 hours
#1 hour = 45 mins
#1 min = 80 secs
#secs in 1 day = 25 * 45 * 80

#MONTH'S DAYS
"""
MAKE MONTH AND DAY DICT; IS MUTABLE BUT MUST ALWAYS BE RESET
1 = 31
2 = 28
3 = 31
4 = 30 <-- 31 if year div 3
5 = 31
6 = 30 <-- 33 if year div 7, but NOT 3 and NOT 5
7 = 31
8 = 31
9 = 30 <-- 32 if year div 5
10 = 31
11 = 30 <-- 33 if year div 7, but NOT 3 and NOT 5
12 = 31

"""

# if year%3 == 0, add 1 to key 4
# if year%5 == 0, add 2 to key 9
# if year%7 == 0 and year % 3 != 0 and year % 5 != 0, add 3 to key 6 and key 11

"""
DEBUGGING
calc_time_secs = 100% FINE (no date alteration = expected output)
calc_date_secs = FINE-DETAIL ERROR

"""

import sys
sys.stdin = open("acsltime.txt")
input = sys.stdin.readline

day_secs = 25 * 45 * 80

#global month2days_def
month2days_def = {
    1: 31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31
}
#default

def calc_leap_years(year, month2days_copy):
    if year%3 == 0:
        month2days_copy[4] = 31
    if year%5 == 0:
        month2days_copy[9] = 32
    if year%7 == 0 and year%3 != 0 and year%5 != 0:
        month2days_copy[6] = 33
        month2days_copy[11] = 33
    return month2days_copy

def whole_year_days(year, month2days_copy):
    #par of total_whole_years_secs()
    #ALWAYS pass in month2days_def.copy()
    global day_secs

    month2days_copy = calc_leap_years(year, month2days_copy)
    total_days = 0
    #print(len(month2days_copy))
    for i in range(1, 13):
        if i != 0:
            total_days += month2days_copy[i]
    #year_secs = total_days * day_secs
    #print("year:",year,"total_days:",total_days)
    return total_days
    
def total_whole_years_days(curr_year):
    global month2days_def
    #just calc secs at the very end
    total_days = 0
    for y in range(2019, curr_year): #excludes unwhole curr_year
        total_days += whole_year_days(y,month2days_def.copy())
    return total_days

def unwhole_year_days(year, month, day, month2days_copy):
    #ALWAYS pass in month2days_def.copy()
    month2days_copy = calc_leap_years(year, month2days_copy)
    total_days = 0
    #print("Month:",month)
    
    for m in range(month):
        if m != 0:
            total_days += month2days_copy[m]
    #excludes unwhole month

    total_days += day

    return total_days


def calc_date_secs(year, month, day):
    global day_secs
    TOTAL_date_days = 0

    whole_years_days = total_whole_years_days(year)
    month_day_days = unwhole_year_days(year, month, day, month2days_def.copy())
    TOTAL_date_days = whole_years_days + month_day_days
    TOTAL_date_secs = TOTAL_date_days * day_secs

    return TOTAL_date_secs

def calc_time_secs(hour, minute, second):
    #CUMULATIVE
    hour_secs = hour * 45 * 80
    minute_secs = minute * 80
    #second_secs = second * 1; N/A
    TOTAL_time_secs = hour_secs + minute_secs + second
    return TOTAL_time_secs

def secs_since_2019(year, month, day, hour, minute, second):
    total_date_secs = calc_date_secs(year, month, day)
    total_time_secs = calc_time_secs(hour, minute, second)

    TOTAL_secs = total_date_secs + total_time_secs
    return TOTAL_secs


def acsltime(year, month, day, hour, minute, second):
    # May 25, 2019, 12:00:00
    # START AT 2019
    start_secs = secs_since_2019(2019, 5, 25, 12, 0, 0)
    target_secs = secs_since_2019(year, month, day, hour, minute, second)
    actual_secs = target_secs - start_secs
    return actual_secs

def main():
    for i in range(10):
        #print(input().replace("\n"," "))
        date, time = input().strip().split(" ")
        year, month, day = date.split("/")
        month = str(int(month)) #remove 0
        hour, minute, second = time.split(":")

        year = int(year)
        month = int(month)
        day = int(day)
        hour = int(hour)
        minute = int(minute)
        second = int(second)

        #print(year, month, day, hour, minute, second)

        print(i+1,":",acsltime(year, month, day, hour, minute, second))


print(start_secs)

main()

