from os import listdir
from os.path import isfile, join
import glob
import os
from os import walk

class ParseAllFiles:
    
    def __init__(self,pathName):
        print("Initiating all the components")
        if pathName is None:
            self.pathName = ""
            
    def walthrough_all_filesfolders(self,filterFileType):
        file_instance = []
        for (root, dirs, fileNameList) in walk(self.pathName):
            for file in fileNameList:
                if file.endswith(filterFileType):
                    file_instance.append(os.path.join(root,file))
        return file_instance
        
    def list_only_files(self):
        pathName = self.pathName
        onlyfiles = [file_ins for file_ins in listdir(pathName) if isfile(join(pathName, file_ins))]
        return onlyfiles
    
    def list_files_folder(self, doesIncludeAbsPath=False):
        return [os.path.abspath(x) if doesIncludeAbsPath else x for x in os.listdir(self.pathName)]
    
    def list_files_glob(self):
        return glob.glob(self.pathName)
    
    def print_line_separator(self,symbol="*",max_length=100):
        print(symbol * max_length)
    
file_ins = ParseAllFiles(None)
# List the file names using the listdir
print(file_ins.list_only_files())
file_ins.print_line_separator()

# List the file names using the walk
print(file_ins.walthrough_all_filesfolders(".py"))
file_ins.print_line_separator()

# List the file names using the glob module
print(file_ins.list_files_glob())
file_ins.print_line_separator()

# List the files and Folder names in the current directory using os Module
print(file_ins.list_files_folder(True))
file_ins.print_line_separator()