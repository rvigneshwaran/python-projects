import traceback

class WriteTextToFile:
    
    def __init__(self,filePath):
        if filePath is not None:
            self.file_path = filePath
        else:
            self.file_path = "output-data/output-response.txt"
            
    def writeContendsFile(self,textContends):
        try:
            text_file_instance = open("sample.txt", "w")
            response_con = text_file_instance.write(textContends)
            print("The Contends has been writtern to file Successfully :: ",response_con)
            text_file_instance.close()
        except:
            print("Exception occured while executing the method writeContendsFile :: ")
            print(traceback.format_exc())
            
write_ins = WriteTextToFile(None)
text_contends = """
Cristiano Ronaldo is a part of Real Madrid's legacy and will forever be remember as one of the great icons throughout the club's history.
"""
write_ins.writeContendsFile(text_contends)
            
        