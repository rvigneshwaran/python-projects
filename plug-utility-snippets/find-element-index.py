
input_list = [12,34,45,32,45,21,43,4,56,67,89,12,34,32,23,31,4,54,67,9,56,54]

class FindElementIndex:
    
    def __init__(self):
        print("Initializing Components")
        
    def find_element_index(self,inputList,element):
        if inputList is not None and element in inputList:
            element_index = inputList.index(element)
            return element_index
        else:
            print("The element :: "+str(element)+ " is not present in the list")
        
index_ins = FindElementIndex()
# Search the Index of the element
element = 89
element_indx = index_ins.find_element_index(input_list,element)
print("The Index of the element "+str(element)+" in the list is :: ",str(element_indx))
# if the element is present in the list multiple times, the index method will return the first occurence index , the remaining occurences are ignored/skipped
element = 32
element_indx = index_ins.find_element_index(input_list,element)
print("The Index of the element "+str(element)+" in the list is :: ",str(element_indx))
# if en element is not present in the list it returns value error
element = 200
element_indx = index_ins.find_element_index(input_list,element)
print("The Index of the element "+str(element)+" in the list is :: ",str(element_indx))
# We can handle this in two ways , here below are steps
# 1. We can use the "in" to check whether the element is present in the list first and then we can retrive the index of the element
# 2. We can use a try except block and then catch the valueerror to determine the same.