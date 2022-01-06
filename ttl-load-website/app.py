from urllib.request import urlopen
import time 
import traceback
import certifi
import ssl

class TTLLoadWebsiteTimeAnalyzer:
    
    def __init__(self):
        print("Loading Components for the TTL Load Analyzer")
        
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