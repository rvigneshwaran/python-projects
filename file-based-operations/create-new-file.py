import traceback

class CreateNewFile:
    
    def __init__(self,newFileName):
        if newFileName is not None:
            self.new_file_name = newFileName
        else:
            self.new_file_name = "output-data/output-response.txt"
            
    def create_new_file(self):
        try:
            created_file_instance = open(self.new_file_name, "x")
            created_file_instance.close()
        except:
            print(traceback.format_exc())
            print("Exception Occured while executing the method create_new_file from CreateNewFile")

create_file_instance = CreateNewFile(None)
create_file_instance.create_new_file()