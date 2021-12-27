
input_list = [12,34,45,32,45,21,43,4,56,67,89,12,34,32,23,31,4,54,67,9,56,54]

class FindLargestElement:
    
    def __init__(self):
        print("Initializing Components")
        
    def find_largest_element(self,inputList,doesWithoutSort=False):
        if inputList is not None and not doesWithoutSort:
            inputList.sort()
            return inputList[-1]
        elif inputList is not None and doesWithoutSort:
            smallest_element = max(inputList)
            return smallest_element
        
    def find_smallest_element(self,inputList,doesWithoutSort=False):
        if inputList is not None and not doesWithoutSort:
            inputList.sort()
            return inputList[0]
        elif inputList is not None and doesWithoutSort:
            smallest_element = min(inputList)
            return smallest_element

        
largest_ins = FindLargestElement()
larg_num = largest_ins.find_largest_element(input_list)
print("The largest number in the list is :: ",larg_num)
small_num = largest_ins.find_smallest_element(input_list)
print("The smallest number in the list is :: ",small_num)

larg_num = largest_ins.find_largest_element(input_list,True)
print("W/O : Sort :: The largest number in the list is :: ",larg_num)
small_num = largest_ins.find_smallest_element(input_list,True)
print("W/O : Sort :: The smallest number in the list is :: ",small_num)