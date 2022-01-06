from urllib.request import urlopen
import time 
import traceback
import certifi
import ssl
from bs4 import BeautifulSoup
import requests
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
        response_contends = self.getPageSourceAsResponse(website_url)
        if response_contends is not None and response_contends["status"] == "Success":
            output_content = response_contends["output_content"]
            soup_instance = BeautifulSoup(output_content, 'html.parser')
            link_comp_list = soup_instance.find_all('a')
            for indv_element in link_comp_list[0:10]:
                print(indv_element['class'])
            #print(link_comp_list)
            
    def find_time_elapsed(self,startTime,website_url):
        currentTime = time.time()
        elapsed_time = currentTime-startTime
        print(f"The Time Taken to execute {website_url} is {elapsed_time}") 

    def check_connectivity(self,website_url):
        read_contends = None
        try:
            startTime = time.time()
            site_response = urlopen(website_url,context=ssl.create_default_context(cafile=certifi.where()))
            if site_response is not None:
                read_contends = site_response.read()
                self.find_time_elapsed(startTime,website_url)
        except Exception:
            error_response = str(traceback.format_exc())
            print(f"The Website {website_url} is not reachable with error response {error_response}")
        return read_contends
    
timeelap_ins = TTLLoadWebsiteTimeAnalyzer()
website_url = "https://en.wikipedia.org/wiki/Coimbatore"
timeelap_ins.check_connectivity(website_url)
timeelap_ins.get_alllinks(website_url)