import random
import string
import os

character_list = list(string.ascii_letters)

class OrganizeSystemFolders:
    
    def __init__(self):
        print("Initializing Components")
        
    def create_files(self,folderPath,file_count=20):
        file_formats_create = [".txt",".jpeg",".xlsx",".pptx",".pdf"]
        for indv_element in range(file_count):
            file_name = [random.choice(character_list) for element in range(15)]
            random.shuffle(file_name)
            file_name = "".join(file_name)
            updated_file_name = file_name+random.choice(file_formats_create)
            file_instance = open(folderPath+updated_file_name, "a+")
            file_instance.close()
        
    def organize_files(self,folderPath):
        file_list = os.listdir(folderPath)
        file_consol = {}
        for indv_file in file_list:
            complete_path = folderPath + indv_file
            file_name,file_extn = os.path.splitext(indv_file)
            file_extn = file_extn.replace(".","")
            if file_extn in file_consol:
                element = list(file_consol[file_extn])
                element.append(file_name)
                file_consol[file_extn] = complete_path
            else:
                type_file_list = []
                type_file_list.append(complete_path)
                file_consol[file_extn] = type_file_list
        return file_consol
    

origanize_instance = OrganizeSystemFolders()            
folder_path = "/Users/blindspot/Desktop/organize-file-data/"
origanize_instance.create_files(folder_path,40)
print(origanize_instance.organize_files(folder_path))