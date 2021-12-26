import traceback

class CalculateWordCount:
    
    def __init__(self):
        print("Initializing Components")
        
    def get_words(self,input_path):
        words = []
        try:
            input_file_instance = open(input_path, "rt")
            output_data = input_file_instance.read()
            words = output_data.split()
        except:
            print("Exception Occured in the method get_words :: ")
            print(traceback.print_exc())
        return words
            
work_count = CalculateWordCount()
input_file_path = "/input-data/sample.txt"
word_count_list = work_count.get_words(input_file_path)
unique_words = set(word_count_list)
print("The Total No Of words in the input file is :: ",len(word_count_list))
print("The Total No Of Unique words in the input file is :: ",len(unique_words))