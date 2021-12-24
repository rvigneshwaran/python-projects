
class SpecialVariables:
    """[This Class will help everyone understand how Special Varaibales in Python Works !!!]
    """
    def __init__(self):
        print("Initializing Objects for the class Special Varaiables")

special_ins  = SpecialVariables()    
#Helps us to know the name of the current class
print("File Name :: = %s"%__name__)

# helps us to retrive the path of the Module which is imported
print("Path :: = %s"%__file__)

# Helps us to retrive the doc string from the Class.
print(SpecialVariables.__doc__)

print(special_ins.__class__)

#
print(SpecialVariables.__bases__)

print(SpecialVariables.__subclasses__())