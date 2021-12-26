import os
import traceback

class FileOperationDelete:
    
    def __init__(self,file_path):
        print("Initializing components")
        if file_path is not None:
            self.file_path = file_path
        else:
            self.file_path = "sample.text"
        
    def delete_file(self):
        try:
            os.remove(self.file_path)
            print("The File is removed Successfully")
        except:
            print("Exception occured while executing the method delete_file :: ")
            print(str(traceback.print_exc()))
            
delete_insta = FileOperationDelete(None)
delete_insta.delete_file()