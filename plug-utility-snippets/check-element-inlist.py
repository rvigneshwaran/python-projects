
input_list = [67,23,56,89,90,65]

class CheckElementInList:
    
    def __init__(self):
        print("Initializing Input Parameters")
        
    def check_element_list(self,checkElement):
        return checkElement in input_list
    
instance = CheckElementInList()
print("67 Present in the list :: ",instance.check_element_list(67))
print("60 Present in the list :: ",instance.check_element_list(60))

