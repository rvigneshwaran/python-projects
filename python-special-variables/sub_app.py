from app import SpecialVariables

class SubSpecialVariables(SpecialVariables):
    
    def apply_line_separator(self,defaultLen=100):
        print("*"*defaultLen)