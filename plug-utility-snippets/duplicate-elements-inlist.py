
class FindDuplicatesInList:
    
    input_list = [23,45,23,45,67,89,34,23,56,67,45,90,98,23,32,23,34,43]
    
    def __init__(self):
        print("Initializing parameters")
        
    def find_duplicates(self,inputList):
        duplicate_elements,filtered_input = set(),set()
        if inputList is not None and len(inputList) > 0:
            for input in inputList:
                if input in filtered_input:
                    duplicate_elements.add(input)
                filtered_input.add(input)
        return duplicate_elements,filtered_input
    
    def find_duplicates_occr(self,inputList):
        duplicate_dict = {}
        filtered_input = set()
        if inputList is not None and len(inputList) > 0:
            for input in inputList:
                if input in filtered_input and input in duplicate_dict:
                    duplicate_occurence = duplicate_dict[input]
                    duplicate_occurence+=1
                    duplicate_dict[input] = duplicate_occurence
                elif input in filtered_input and input not in duplicate_dict:
                    duplicate_dict[input] = 1
                filtered_input.add(input)
        return duplicate_dict
    
    def find_duplicates_index(self,inputList):
        duplicate_dict = {}
        filtered_input = set()
        if inputList is not None and len(inputList) > 0:
            for index,input in enumerate(inputList):
                if input in filtered_input and input in duplicate_dict:
                    index_list = duplicate_dict[input]
                    index_list.append(index)
                    duplicate_dict[input] = index_list
                elif input in filtered_input and input not in duplicate_dict:
                    index_list = []
                    index_list.append(index)
                    duplicate_dict[input] = index_list
                filtered_input.add(input)
        return duplicate_dict
    

instance = FindDuplicatesInList()
print("Elements in the Original Element :: ",instance.input_list)
duplicate_list = instance.find_duplicates(instance.input_list)
print("Duplicate Elements in the list :: ",duplicate_list)
duplicate_element_occurence = instance.find_duplicates_occr(instance.input_list)
print("Duplicate Elements Occurence :: ",duplicate_element_occurence)
duplicate_element_index = instance.find_duplicates_index(instance.input_list)
print("Duplicate Elements Index :: ",duplicate_element_index)