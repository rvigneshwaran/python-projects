
class ApplicationUtils:
    
    def __init__(self):
        print("Initializing Components in Application Utils")
        
    @staticmethod
    def apply_string_functions(input_text):
        various_forms = {}
        if input_text is not None:
            various_forms["input_text"] = input_text
            format_upper = input_text.upper()
            various_forms["upper"] = format_upper
            format_lower = input_text.lower()
            various_forms["lower"] = format_lower
            format_title = input_text.title()
            various_forms["title"] = format_title
        return various_forms