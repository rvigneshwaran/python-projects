import string
import re

class ManageSpeceRegex:
    
    def __init__(self,inputText):
        print("Initializing Components")
        if inputText is not None:
            self.input_text = inputText
        else:
            self.input_text = '''
            
            
                Zlatan Ibrahimović 
                    Bosnian: born 3 October 1981 is a Swedish professional 
                    footballer who    plays as a striker for 
                        Serie A club 
                            AC Milan and the Sweden national team. 
            
                He is widely regarded as one of the greatest strikers of all time.Ibrahimović is one of the most    decorated 
                    active footballers in the world,[a] having won 31 trophies in his career.
            
                He has scored over 570 career goals, 
                    including more than 500 club goals,and has scored in each of the last four 
                        decades.
                
                
            '''
        
    def apply_line_separators(self,symbol="*",length=75):
        print(symbol*length)
        
    def console_output_contends(self,operationApplied,input_text):
        print(operationApplied + " :: " +input_text)
        self.apply_line_separators("*",100)
        
    def apply_basic_strip(self):
        input_string = self.input_text
        basic_strip = input_string.strip()
        self.console_output_contends("Basic Strip Operation :: ",basic_strip)
        lrstrip_conends = basic_strip.lstrip().rstrip()
        self.console_output_contends("Left and Right Strip Operation :: ",lrstrip_conends)
        joinWithSplit =  " ".join(input_string.split())
        self.console_output_contends("Join with Split Operation :: ",joinWithSplit)
        translate_ins = input_string.translate({ord(c): None for c in string.whitespace})
        self.console_output_contends("Using Translate to remove White Spaces :: ",translate_ins)
        
    def apply_regex(self):
        input_string = self.input_text
        # Match all the spaces using the Regular expression in the input strings
        match_spaces = re.sub(r"\s+", "", input_string)
        self.console_output_contends("Match All Spaces with Regex :: ",match_spaces)
        # Match all the starting spaces using the regular expression in the input string
        match_start_spaces = re.sub(r"^\s+", "", input_string)
        self.console_output_contends("Match Start Spaces with Regex :: ",match_start_spaces)
        # Match all the trailing spaces using the regular expression in the input string
        match_end_spaces = re.sub(r"\s+$", "", input_string)
        self.console_output_contends("Match End Spaces with Regex :: ",match_end_spaces)
        
instance = ManageSpeceRegex(None)
instance.apply_basic_strip()
instance.apply_regex()