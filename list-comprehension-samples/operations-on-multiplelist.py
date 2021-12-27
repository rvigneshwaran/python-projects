

class OperationOnMultipleList:
    
    def __init__(self):
        print("Initializing Components")
        
    def create_tuple(self,input_list1,input_list2):
        # Create tuple using List Comprehensions
        return [(index,value) for index in input_list1 for value in input_list2]
    
    def multiply_list_elements(self,input_list1,input_list2):
        return [l1element_1 * l2element_1 for l1element_1 in input_list1 for l2element_1 in input_list2]

instance = OperationOnMultipleList()

input_list1 = ["FW","MF","DF","GK"]
input_list2 = ["CRISTIANO RONALDO","Juan Manuel MATA","Luke SHAW","David DE GEA","Paul POGBA","Marcus RASHFORD"] 
print(instance.create_tuple(input_list1,input_list2))
print("*"*100)

input_list1 = [2,4,6,8]
input_list2 = [10,20,30,40] 
print(instance.multiply_list_elements(input_list1,input_list2))
print("*"*100)

# Set default values to all the elements in the dict
input_list = ["x","y","z"]
default_value = 10
default_dict = {input_list[index] : default_value for index in range(0,len(input_list))}
print(default_dict)
print("*"*100)