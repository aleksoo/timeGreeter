import sys

from timeContent import TimeContent
from welcomeMsg import welcomeMsg

def namePicker():
    name = ""
    if len(sys.argv) < 2:
        name = "Person"
    else:
        for i in range(1, len(sys.argv)):
            name += sys.argv[i]
            name += " " if len(sys.argv) > i+1 else ""
    return name
    

if __name__ == "__main__":
    name = namePicker()
    time = TimeContent(1)
    welcomeMsg(time, name)
    time.updateTime()
    welcomeMsg(time, name)