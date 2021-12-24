# Importing Packages fromthe Util Package
from utils.application_utils import ApplicationUtils
from utils.security_utils import SecurityUtils
import os
class SpecialVariables:
    """[This Class will help everyone understand how Special Varaibales in Python Works]
    """
    def __init__(self):
        print("Initializing Objects for the class Special Varaiables")
        
    def apply_line_separator(self,defaultLen=75):
        print("*"*75)
        
special_ins  = SpecialVariables()    
# Helps us to know the name of the current class
print("__name__ convention of Current file :: = %s"%__name__)
print("__name__ convention app utils = %s"%ApplicationUtils.__name__)
special_ins.apply_line_separator()

# using Functions defined as part of Utils package
print(ApplicationUtils.apply_string_functions("Manchester United"))
sec_utils_ins = SecurityUtils()
print(sec_utils_ins.generate_security_key())
special_ins.apply_line_separator()

# helps us to retrive the path of the Module which is imported
print("Path :: = %s"%__file__)
parent_directry = os.path.join(os.path.dirname(__file__), '..')
print("Parent-Directory :: ",parent_directry)
current_directory = os.path.dirname(os.path.realpath(__file__))
print("Current-Directory :: ",current_directory)
abs_path = os.path.abspath(os.path.dirname(__file__))
print("Current-Directory-abs :: ",abs_path)
special_ins.apply_line_separator()

# Helps us to retrive the doc string from the Class.
print(SpecialVariables.__doc__)
special_ins.apply_line_separator()

print(special_ins.__class__)
special_ins.apply_line_separator()
#
print(SpecialVariables.__bases__)
special_ins.apply_line_separator()

print(SpecialVariables.__subclasses__())
special_ins.apply_line_separator()