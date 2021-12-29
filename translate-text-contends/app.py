from translate import Translator
import traceback

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

instance =  TranslateContends()
source_lang = input("Enter the source language :: \n")
dest_lang =  input("Enter the destination language :: \n")
text_contends = input("Enter the text contends to translate :: \n")
output = instance.translate_contends(source_lang,dest_lang,text_contends)
print(output)
