
class ReadTextFile:
    
    def __init__(self,inputFilePath):
        if inputFilePath is None:
            self.input_file_path = "/input-data/sample.txt"
        else:
            self.input_file_path =  inputFilePath
    
    def read_text_file(self,characterCountToread=20):
        """[read the contends of the text file , by default the file reads first 20 characters of the file]

        Returns:
            [string]: [read the contends of the file in one shot as string]
        """
        file_instance = open(self.input_file_path, "r") 
        # read first 20 characters in the input file
        data_read_fromfile = file_instance.read(characterCountToread)
        return data_read_fromfile
    
    def read_linebyline(self):
        """[Method intended to read a file line by line and create a list]

        Returns:
            [list]: [contends of the file as list]
        """
        file_instance = open(self.input_file_path, "r")
        line_byline = []
        while(True):
            line_instance = file_instance.readline()
            if not line_instance: 
                break 
            else:
                line_byline.append(line_instance.strip())
        return line_byline
    
read_file = ReadTextFile(None)
print(read_file.read_text_file(100))
print("*"*100)
print(read_file.read_linebyline())
    