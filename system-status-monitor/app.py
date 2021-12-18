import psutil
import os 
import resource

class SystemStatusMonitor:
    
    def __init__(self):
        print("Initializing parameters for System Status Monitor")
        self.process_instance = psutil.Process(os.getpid())
    
    def getCPUSpecificDetails(self):
        # Retrives the local CPU's in the Machine.
        no_cpucores = psutil.cpu_count()
        print("No of CPU Cores :: ",no_cpucores)
        # Retrives the CPU statistics.
        cpu_stats_details = psutil.cpu_stats()
        # retrives the context switches,interrupts and sys call details
        print("ctx_switches :: ",cpu_stats_details.ctx_switches)
        # retrives the interuppts
        print("interrupts :: ",cpu_stats_details.interrupts)
        # retrives the soft interuptts
        print("soft_interuppts :: ",cpu_stats_details.soft_interrupts)
        # retrives the sys calls
        print("syscalls :: ",cpu_stats_details.syscalls)
        # Retrives the CPU Frequency Details
        cpu_frequncy_details = psutil.cpu_freq()
        # Retrives the Current,Min and Max frequencies in Mhz.
        print(cpu_frequncy_details)
        
    def getMemoryUsage(self):
        """[Function which helps to find the memory usage of the system
        ]
        Returns:
            [int]: [Memory information of the system]
        """
        process_instance = self.process_instance
        # RSS is resident Set Side - Actual Physical Memory the process i using
        # VSS Virtual Memoru the process is using
        memory_usage = process_instance.memory_info().rss / 1024**2
        print("Memory usage details :: "+ str(memory_usage)+ " MB")
        memory_percentage= process_instance.memory_percent()
        print("Memory Usage in (%) :: "+str(memory_percentage*100))
        # Works only for Linux Machine
        resource_det = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
        print(resource_det)
        virtual_memory_details = psutil.virtual_memory()
        print("Virtual Memory Details :: ",virtual_memory_details)
        swap_memory_details = psutil.swap_memory()
        print("SWAP Memory details :: ",swap_memory_details)
        return memory_usage
    
    def getDiskSpecificDetails(self):
        disk_part_details = psutil.disk_partitions()
        print("Disk Partition Details :: ",disk_part_details)
        disk_usage_det = psutil.disk_usage("/")
        print("Disk Usage Details :: ",disk_usage_det)
        disk_partition_det = psutil.disk_partitions()
        print("Disk Partition Details :: ",disk_partition_det)
        
    def getNetworkSpecificDetails(self):
        try:
            net_io = psutil.net_io_counters()
            print("Network Stats :: ",net_io)
            # retrives the Socket Connection in the system as Tuples
            sock_connect_details = psutil.net_connections()
            print("Socket Connection Details :: ",sock_connect_details)
            # Address of Each Network Interface
            inteface_details = psutil.net_if_addrs()
            print("Network Address Details :: ",inteface_details)
        except Exception:
            print("Exception Occured while Exceuting the Method getNetworkSpecificDetails")

system_monitor_instance = SystemStatusMonitor()
print("Capturing Memory Uage details")
system_monitor_instance.getMemoryUsage()
print("Capturing CPU Sepcific Details")
system_monitor_instance.getCPUSpecificDetails()
print("Capturing Disk Sepcific Details")
system_monitor_instance.getDiskSpecificDetails()
print("Capturing IO Sepcific Details")
system_monitor_instance.getNetworkSpecificDetails()   