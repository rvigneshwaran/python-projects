import json
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import requests
import traceback

class CheckWebsiteConnectivity:
    
    def __init__(self,input_file_path):
        if input_file_path is not None:
            file_instance = open(input_file_path)
            input_data = json.load(file_instance)
            self.input_data =  input_data
            file_instance.close()
            
    def check_website_connectivity_request(self,website_url):
        isWebSiteUp = True
        try:
            page = requests.get(website_url,verify=False)
            print(page.status_code)
        except Exception:
            isWebSiteUp = False
            print(f"The Website {website_url} is not reachable")
        return isWebSiteUp
    
    def check_website_connectivity_url(self,website_url):
        isWebSiteUp = True
        try:
            request_instance = Request(website_url)
            response_content = urlopen(request_instance)
        except HTTPError as error:
            print("Error Code :: ", error.code)
            isWebSiteUp = False
        except URLError as error:
            print("Error Code :: ", error.code)
            isWebSiteUp = False
        else:
            print ('Website is working fine')
        return isWebSiteUp
    
    def write_contends_to_file(self,fileName,encoding_input,inputContent):
        with open(fileName, 'w', encoding=encoding_input) as file_ins:
            json.dump(inputContent,file_ins, ensure_ascii=False, indent=4)
        print("Completed Writing the Response contends")
    
    def parse_file_contends(self):
        input_contends = self.input_data
        updated_contends_list = []
        response_file_name = "output/response-data.json"
        encoding_inp = "utf-8"
        if input_contends is not None and len(input_contends) > 0:
            for indv_contnds in input_contends[0:1]:
                website_url = indv_contnds["SiteLink"]
                print("Evaluating for the URL :: ",website_url)
                isWebsiteUp = self.check_website_connectivity_request(website_url)
                indv_contnds["isWebsiteUp"] = isWebsiteUp
                updated_contends_list.append(indv_contnds)
        self.write_contends_to_file(response_file_name,encoding_inp,updated_contends_list)

input_file_path_updated = "inputs/input-config.json"              
connect_inst = CheckWebsiteConnectivity(input_file_path_updated)
connect_inst.parse_file_contends()