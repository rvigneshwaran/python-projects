import traceback

class AppendtextFile:
    
    def __init__(self):
        print("Initializing Components ")
        
    def append_text_file(self,file_path,textToAppend):
        try:
            # Open the file in text mode "t" and append mode "a"
            fileInstance = open(file_path, "at")
            fileInstance.write(textToAppend)
            fileInstance.close()
            print("Completed appended the input file file to the existing text file")
        except:
            print("Exception occured while exceuting the method append_text_file")
            print(traceback.print_exc())
            
instance = AppendtextFile()
file_path = "input-data/sample.txt"
text_to_append = '''
Manchester United was formed in 1878 as Newton Heath LYR Football Club by the Carriage and Wagon department of the Lancashire and Yorkshire Railway (LYR) depot at Newton Heath.The team initially played games against other departments and railway companies, but on 20 November 1880, they competed in their first recorded match; wearing the colours of the railway company green and gold they were defeated 6-0 by Bolton Wanderers' reserve team.By 1888, the club had become a founding member of The Combination, a regional football league. Following the league's dissolution after only one season, Newton Heath joined the newly formed Football Alliance, which ran for three seasons before being merged with The Football League. This resulted in the club starting the 1892-93 season in the First Division, by which time it had become independent of the railway company and dropped the "LYR" from its name.[16] After two seasons, the club was relegated to the Second Division.
'''
instance.append_text_file(file_path,text_to_append)

