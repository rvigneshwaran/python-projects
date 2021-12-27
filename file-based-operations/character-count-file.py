import traceback

class CharacterCountInFile:
    
    def __int__(self):
        print("Initializing Components")
        
    def count_characters_file(self,input_file):
        try:
            file_instance = open(input_file, "r")
            data = file_instance.read()
            number_of_characters = len(data)
            print('Total Characters in Input file is  :', number_of_characters)
        except:
            print("Exception Occured while exeuting the method count_characters_file")
            print(traceback.print_exc())
            
countchar_inss = CharacterCountInFile()
input_file = "/Users/blindspot/Desktop/python-projects/file-based-operations/input-data/sample.txt"
countchar_inss.count_characters_file(input_file)
