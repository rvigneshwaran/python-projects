import sys
import argparse

class CommandLineArgs:
    
    def console_separators(self,symbol="*",size=75):
        print(symbol*size)
        
args_ins = CommandLineArgs()

# retriving Command Line Args as list of values using Sys Module
print("The Command Line Args are :: ",sys.argv)
# Iterating Command Line Args
arg_list = len(sys.argv)
if arg_list > 0:
    for index,each_arg in enumerate(sys.argv):
        print("The Value of argument "+str()+" is :: "+str(each_arg))
args_ins.console_separators()

# retriving the command line args using ArgParser
message = "Add Length of the Tree"
arg_parsins = argparse.ArgumentParser(description = message)
# How Do we add optionl arugument as part of the code 
arg_parsins.add_argument("-o", "--canParseFromFile", help = "Can Input be retrived from the default file ?")
arg_parsins.parse_args()

# How the Command Line args picked and used in the code 
if arg_parsins.canParseFromFile:
    print("canParseFromFile :: ",arg_parsins.canParseFromFile)
args_ins.console_separators()