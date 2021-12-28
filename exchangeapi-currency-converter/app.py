import requests
import traceback
import json

class CurrencyConverter:
    
    def __init__(self):
        print("Initializing Components ")
        
    def get_response_contends(self,websiteURL):
        output_response = {}
        try:
            response_detail = requests.get(websiteURL)
            status_code = response_detail.status_code
            if response_detail is not None and status_code == 200:
                output_response["status"] = "Success"
                response_content = response_detail.content.decode("utf-8") 
                contends = json.loads(response_content)
                output_response["output_content"] = contends["rates"]
            else:
                output_response["status"] = "Failure"
                output_response["error_message"] = "Failed to Access host"
        except Exception:
            output_response["status"] = "Failure"
            output_response["error_message"] = str(traceback.print_exc())
        return output_response
        
current_instance = CurrencyConverter()
websiteURL = "https://open.er-api.com/v6/latest/USD"
response = current_instance.get_response_contends(websiteURL)
print(response)