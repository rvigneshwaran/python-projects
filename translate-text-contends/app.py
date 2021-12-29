from translate import Translator
import traceback
import json
class TranslateContends:
    
    def __init__(self):
        print("Initilizing Translator Contends")
        
    def translate_contends(self,source_lang,dest_lang,text_contends):
        output_response = {}
        output_response["source_language"] = source_lang
        output_response["destination_language"] = dest_lang
        try:
            trans_instance = Translator(from_lang= source_lang,to_lang=dest_lang)
            response_ins = trans_instance.translate(text_contends)
            output_response["response_output"] = response_ins
            output_response["status"] = "Success"
        except:
            output_response["status"] = "Failure"
            error_response = str(traceback.format_exc())
            output_response["error_message"] = error_response
            print("Exception occured while executing the method translate_contends with :: "+error_response)
        return output_response
    
    def read_json_file(self,input_file):
        output_response = []
        try:
            input_file_instance = open(input_file)
            output_response = json.load(input_file_instance)
            input_file_instance.close()
        except:
            print("Exception occured while executing the method read_json_file")
            print(traceback.print_exc())
        return output_response
    
    def write_data_file(self,output_response):
        output_file = "outputs/response-data.json"
        existing_contends = self.read_json_file(output_file)
        try:
            if output_file is not None:
                with open(output_file, "w") as outfile:
                    json.dump(output_response, outfile,indent=4,ensure_ascii=False)
        except:
            print("Exception occured while executing the method write_data_file")
            print(traceback.print_exc())

instance =  TranslateContends()
# Enter the Source Language which you are going to enter the text
source_lang = input("Enter the source language :: \n")
# Enter the destination lanaguage which we are going to traslate the contebds
dest_lang =  input("Enter the destination language :: \n")
text_contends = input("Enter the text contends to translate :: \n")
# Method Call to Translate the text contends to the destination language
output = instance.translate_contends(source_lang,dest_lang,text_contends)
print(output)
# Write the contends in the json file
instance.write_data_file(output)
