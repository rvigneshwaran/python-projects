import traceback
import os

class DirectoryOperations:
    
    def __init__(self):
        print("Initializing Components")
        
    def create_drectory(self,directory_name):
        try:
            if not os.path.isdir(directory_name):
                os.mkdir(directory_name)
                print("Directory Created Successfully")
            else:
                print("The Folder with the same name is present in the path")
        except:
            print("Exception occured while creating a new directory")
            print(traceback.print_exc())
        
    def delete_directory(self,directory_name):
        try:
            if not os.path.isdir(directory_name):
                os.rmdir(directory_name)
                print("Directory Removed Successfully")
        except:
            print("Exception occured while removing the directory")
            print(traceback.print_exc())
            
operations_ins = DirectoryOperations()
directory_path = "./operations-dir"
operations_ins.create_drectory(directory_path)
operations_ins.delete_directory(directory_path)