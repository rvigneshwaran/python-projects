import requests
from bs4 import BeautifulSoup
import traceback
import json

class Applicationutils:
    
    @staticmethod
    def getWebSiteContendsAsHTML(websiteURL):
        soup_instance = None
        response_detail = Applicationutils.getPageSourceAsResponse(websiteURL)
        if response_detail["status"] == "Success":
            response_content = response_detail["output_content"]
            soup_instance = BeautifulSoup(response_content, 'html.parser')
        return soup_instance
            
    @staticmethod
    def getPageSourceAsResponse(websiteURL):
        output_response = {}
        try:
            response_detail = requests.get(websiteURL,verify=False)
            status_code = response_detail.status_code
            if response_detail is not None and status_code == 200:
                output_response["status"] = "Success"
                output_response["output_content"] = response_detail.content
            else:
                output_response["status"] = "Failure"
                output_response["error_message"] = "Failed to Access host"
        except Exception:
            output_response["status"] = "Failure"
            output_response["error_message"] = str(traceback.print_exc())
        return output_response
    
    @staticmethod
    def write_contends_to_file(fileName,encoding_input,inputContent):
        with open(fileName, 'w', encoding=encoding_input) as file_ins:
            json.dump(inputContent,file_ins, ensure_ascii=False, indent=4)
            
    @staticmethod
    def write_contends_to_file(fileName,encoding_input,inputContent):
        with open(fileName, 'w', encoding=encoding_input) as file_ins:
            json.dump(inputContent,file_ins, ensure_ascii=False, indent=4)