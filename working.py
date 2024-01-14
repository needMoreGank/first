import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(12time):
    try:
        starttime, endtime = 12time.split(" to ")
    except ValueError:
        return ValueError
    else:
        pass

    for time in starttime, endtime:
        if re.search("\d:\d\d\s[A|P]M"):
            pass
        else:
            return ValueError
        
        
        if "AM" in time:
            
        

if __name__ == "__main__":
    main()
