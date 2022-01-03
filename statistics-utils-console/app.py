import statistics
import random
import json

class StatisticsComponents:
    
    def __init__(self):
        print("Initializing Components")
        
    def create_random_list(self,max_size,low_key,high_key):
        return [random.randint(low_key,high_key) for i in range(max_size)] 
        
    def get_stat_components(self,input_list):
        output_response = {}
        output_response["mean"] = statistics.mean(input_list)
        output_response["median"] = statistics.median(input_list)
        output_response["mode"] = statistics.mode(input_list)
        output_response["standard-deviation"] = statistics.stdev(input_list)
        output_response["variance"] = statistics.variance(input_list)
        return output_response
    
    def pretty_print(self,input_dict,indent_size=4):
        return json.dumps(input_dict,sort_keys=True, indent=indent_size)
    
stats_instance = StatisticsComponents()

# create a random list of postive and negative integers
list_size = 40
low_key = -100
high_key = 100
input_element_list = stats_instance.create_random_list(list_size,low_key,high_key)
print("The Input List :: ",input_element_list)
value_dict = stats_instance.get_stat_components(input_element_list)
print(stats_instance.pretty_print(value_dict))