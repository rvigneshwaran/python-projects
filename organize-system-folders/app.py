import random
import string
import os
import shutil

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
        file_list = [file_ins for file_ins in os.listdir(folderPath) if os.path.isfile(os.path.join(folder_path, file_ins)) and not file_ins.startswith('.')]
        file_consol = {}
        for indv_file in file_list:
            print(indv_file)
            complete_path = folderPath + indv_file
            file_name,file_extn = os.path.splitext(indv_file)
            file_extn = file_extn.replace(".","")
            if file_extn in file_consol:
                element = list(file_consol[file_extn])
                element.append(complete_path)
                file_consol[file_extn] = element
            else:
                type_file_list = []
                type_file_list.append(complete_path)
                file_consol[file_extn] = type_file_list
        return file_consol
    
    def move_organized_files(self,folder_path,organized_dict):
        if organized_dict is not None:
            for file_extension,file_list in organized_dict.items():
                for indv_file in file_list:
                    file_name = os.path.basename(indv_file)
                    new_path = folder_path + file_extension + "/"
                    updated_file_path = new_path + file_name
                    if os.path.exists(new_path):
                        shutil.move(indv_file,updated_file_path)
                    else:
                        os.makedirs(new_path)
                        shutil.move(indv_file,updated_file_path)
    

origanize_instance = OrganizeSystemFolders()            
folder_path = "/Users/blindspot/Desktop/organize-file-data/"
origanize_instance.create_files(folder_path,40)
organized_dict = origanize_instance.organize_files(folder_path)
origanize_instance.move_organized_files(folder_path,organized_dict)