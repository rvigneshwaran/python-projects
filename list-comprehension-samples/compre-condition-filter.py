import warnings
warnings.filterwarnings("ignore")

input_list = [23,33,45,23,12,78,56,67,45,89,29,43,23,67]

class ConditionalFilter:
    
    def __init__(self):
        print("Initializing Components")
        
    def apply_conditional_filter(self,input_list,divis_element):
        filtered_list = []
        if input_list is not None:
            filtered_list = [element for element in input_list if element % divis_element == 0]
        return filtered_list
    
    def apply_conditional_filter_before(self,input_list,divis_element):
        filtered_list = []
        if input_list is not None:
            filtered_list = [element if element % divis_element == 0 else None for element in input_list]
        return filtered_list
    
cond_instance = ConditionalFilter()

# Filtered Element that are divisible by 2 in the input List
fil_list = cond_instance.apply_conditional_filter(input_list,2)
print(fil_list)

# Filtered Element :: Early Eval Levels
fil_list = cond_instance.apply_conditional_filter_before(input_list,2)
fil_list = list(filter((None).__ne__, fil_list))
print(fil_list)