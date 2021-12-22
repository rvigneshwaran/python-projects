import time
from datetime import timedelta
from timeit import default_timer as timer
from pytictoc import TicToc

class TimeCheckExecutions:
    
    def add_elements_list(self,rangeMax = 100):
        final_list = []
        for indv_num in range(rangeMax):
            final_list.append(indv_num)
        return final_list
    
time_chk_ins = TimeCheckExecutions()

# using the time module to calculate elapsed time
start_time = time.time()
final_list = time_chk_ins.add_elements_list(500000)
end_time = time.time()
execution_time_frame = end_time - start_time
print("Time Taken to Execute using time.time() :: "+str(execution_time_frame) + " seconds")

# using the timer module to calculate elapsed time
start_time = timer()
final_list = time_chk_ins.add_elements_list(500000)
end_time = timer()
execution_time_frame = end_time - start_time
print("Time Taken to Execute using timer() :: "+str(execution_time_frame) + " seconds")

# Using processtime method in time module to calculate elapsed time
start_time = time.process_time()
final_list = time_chk_ins.add_elements_list(500000)
end_time = time.process_time()
execution_time_frame = end_time - start_time
print("Time Taken to Execute using process_time() :: "+str(execution_time_frame) + " seconds")

# using the TicToc Module to calculate the time elaspsed time 
time_instance = TicToc()
time_instance.tic()
final_list = time_chk_ins.add_elements_list(500000)
print("Time Taken to Execute using TicToc Module :: ")
time_instance.toc()
