from urllib.request import urlopen
import time 
import traceback
import certifi
import ssl
from bs4 import BeautifulSoup
import requests
import json

import warnings
warnings.filterwarnings("ignore")
class TTLLoadWebsiteTimeAnalyzer:
    
    def __init__(self):
        print("Loading Components for the TTL Load Analyzer")
        
    def getPageSourceAsResponse(self,websiteURL):
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
        
    def get_alllinks(self,website_url):
        link_content_list = []
        response_contends = self.getPageSourceAsResponse(website_url)
        if response_contends is not None and response_contends["status"] == "Success":
            output_content = response_contends["output_content"]
            soup_instance = BeautifulSoup(output_content, 'html.parser')
            link_comp_list = soup_instance.find_all('a')
            for indv_element in link_comp_list:
                link_detail = indv_element.get("href")
                title_detail = indv_element.get("title")
                if link_detail is not None and title_detail is not None:
                    linked_detail_dict = {}
                    linked_detail_dict["link_detail"] = "https://en.wikipedia.org"+link_detail
                    linked_detail_dict["link_title"] = title_detail
                    link_content_list.append(linked_detail_dict)
            print(link_content_list)
            return link_content_list
            
    def find_time_elapsed(self,startTime,website_url):
        currentTime = time.time()
        elapsed_time = currentTime-startTime
        print(f"The Time Taken to execute {website_url} is {elapsed_time}")
        return elapsed_time
    
    def write_contends_to_file(self,fileName,encoding_input,inputContent):
        with open(fileName, 'w', encoding=encoding_input) as file_ins:
            json.dump(inputContent,file_ins, ensure_ascii=False, indent=4)

    def check_connectivity(self,website_url):
        elapsed_time = None
        try:
            startTime = time.time()
            site_response = urlopen(website_url,context=ssl.create_default_context(cafile=certifi.where()))
            if site_response is not None:
                read_contends = site_response.read()
                elapsed_time = self.find_time_elapsed(startTime,website_url)
        except Exception:
            error_response = str(traceback.format_exc())
            print(f"The Website {website_url} is not reachable with error response {error_response}")
        return elapsed_time
    
timeelap_ins = TTLLoadWebsiteTimeAnalyzer()
website_url = "https://en.wikipedia.org/wiki/Coimbatore"
timeelap_ins.check_connectivity(website_url)
contends_link_list = timeelap_ins.get_alllinks(website_url)
consolidated_time_list = []
if contends_link_list is not None and len(contends_link_list) > 0:
    '''
    TODO As of now this list has been limited to 100, This can be extended to maximum 
    and this below logic should be writtern recursive in order to get more data about the
    initial query up.
    '''
    for indv_link_detail in contends_link_list[:100]:
        service_detail = indv_link_detail["link_detail"]
        link_title = indv_link_detail["link_title"]
        elapsed_time = timeelap_ins.check_connectivity(service_detail)
        indv_link_detail["time-taken-toload"] = elapsed_time
        consolidated_time_list.append(indv_link_detail)
output_file_name = "outputs/response-output.json"
encoding = "utf-8"
timeelap_ins.write_contends_to_file(output_file_name,encoding,consolidated_time_list)