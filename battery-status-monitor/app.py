import psutil
from utils import applicationutils

if __name__ == "__main__":
    # returns a tuple
    battery = psutil.sensors_battery()
    print("Battery percentage : ", battery.percent)
    print("Power plugged in : ", battery.power_plugged)
    # converting seconds to hh:mm:ss
    print("Battery left : ", applicationutils.convertTime(battery.secsleft))