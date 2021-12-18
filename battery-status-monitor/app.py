import psutil
from applicationutils import applicationutils

class BatteryStatusMonitor:
    
    def __init__(self):
        self.battery_instance = psutil.sensors_battery()
        
    def getBatteryStatus(self):
        """ Function which help in getting the status of the battery from the 
        battery sensor instance.
        """
        if self.battery_instance is not None:
            battery_instance = self.battery_instance
            print("Battery percentage : ", battery_instance.percent)
            print("Power plugged in : ", battery_instance.power_plugged)
            print("Battery left : ", applicationutils.convertTime(battery_instance.secsleft))

if __name__ == "__main__":
    battery_status_monitor = BatteryStatusMonitor()
    battery_status_monitor.getBatteryStatus()