import requests
import traceback
import json
import sys
class CurrencyConverter:
    
    def __init__(self):
        print("Initializing Components ")
        
    def calculate_currency(self,currency_dict,source_currency,destination_currency):
        output = None
        currency_dict = currency_dict["output_content"]
        if source_currency and destination_currency in currency_dict:
            src_cur_value = currency_dict[source_currency]
            dest_cur_value = currency_dict[destination_currency]
            output = (1 / src_cur_value) * dest_cur_value
        else:
            print("The Provided Source or Destination Currency is NOT PART OF THE EXCHANGE")
        return output
        
    def get_response_contends(self,websiteURL):
        output_response = {}
        try:
            response_detail = requests.get(websiteURL)
            status_code = response_detail.status_code
            if response_detail is not None and status_code == 200:
                output_response["status"] = "Success"
                response_content = response_detail.content.decode("utf-8") 
                contends = json.loads(response_content)
                self.write_data_file(contends)
                output_response["output_content"] = contends["rates"]
            else:
                output_response["status"] = "Failure"
                output_response["error_message"] = "Failed to Access host"
        except Exception:
            output_response["status"] = "Failure"
            output_response["error_message"] = str(traceback.print_exc())
        return output_response
    
    def write_data_file(self,output_response):
        output_file = "outputs/response-data.json"
        try:
            if output_file is not None:
                with open(output_file, "w") as outfile:
                    json.dump(output_response, outfile,indent=4)
        except:
            print("Exception occured while executing the method write_data_file")
            print(traceback.print_exc())

args_length = len(sys.argv)
if args_length == 3:
    source_currency = sys.argv[1]
    destination_currency = sys.argv[2]
    current_instance = CurrencyConverter()
    websiteURL = "https://open.er-api.com/v6/latest/USD"
    currency_dict = current_instance.get_response_contends(websiteURL)
    output = current_instance.calculate_currency(currency_dict,source_currency,destination_currency)
    print("The source currency :: "+source_currency+" is "+str(output)+ " times the destination currency :: "+destination_currency)
else:
    print("Please provide source and destination currency as part of program")