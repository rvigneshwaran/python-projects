import keyword
import json
import traceback
from contextlib import redirect_stdout
import io

class GetKeywordDetails:
    
    def __init__(self):
        print("Initializing components in GetKeywordDetails")
        
    def getKeywordsAsList(self):
        keyword_list = keyword.kwlist
        print("Total No Of keywords retrived from the Module is :: ",len(keyword_list))
        return keyword_list
    
    def get_keyword_details(self,keyword_list):
        keyword_dict = {}
        if keyword_list is not None:
            for keyword_name in keyword_list:
                io_instance = io.StringIO()
                with redirect_stdout(io_instance):
                    help(keyword_name)
                content_value = io_instance.getvalue()
                keyword_dict[keyword_name] = content_value
        return keyword_dict
    
    def write_data_file(self,output_response):
        output_file = "outputs/response-data.json"
        try:
            if output_file is not None:
                with open(output_file, "w") as outfile:
                    json.dump(output_response, outfile,indent=4,)
        except:
            print("Exception occured while executing the method write_data_file")
            print(traceback.print_exc())

keyworrd_ins = GetKeywordDetails()
# Get the List of Python Keywords as list
keyword_list = keyworrd_ins.getKeywordsAsList()  
# Pass the value from the list to the helper method to get further details        
keyword_dict = keyworrd_ins.get_keyword_details(keyword_list)
# Write the contends of the response - data to json
keyworrd_ins.write_data_file(keyword_dict)