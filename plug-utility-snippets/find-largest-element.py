
input_list = [12,34,45,32,45,21,43,4,56,67,89,12,34,32,23,31,4,54,67,9,56,54]

class FindLargestElement:
    
    def __init__(self):
        print("Initializing Components")
        
    def find_largest_element(self,inputList):
        if inputList is not None:
            inputList.sort()
            return inputList[-1]

        
largest_ins = FindLargestElement()
larg_num = largest_ins.find_largest_element(input_list)
print("The largest number in the list is :: ",larg_num)
