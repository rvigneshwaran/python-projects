import requests
from bs4 import BeautifulSoup


class WebScraperBot:
    
    def __init__(self,host_url):
        self.host_url = host_url
        
    def getServiceDetails(self):
        host_url = self.host_url
        status_code = None
        output_content = None
        try:
            response_detail = requests.get(host_url)
            if response_detail is not None:
                status_code = response_detail.status_code
                print("The response status code is :: ",status_code)
                output_content = response_detail.content
                #print("The response from the page is :: ",output_content)
            else:
                print("failed to Access the Host")
        except Exception:
            print("failed to Access the Host")
        return status_code,output_content
        
    def getAllLinksfromPage(self):
        return ""

host_url = "https://en.wikipedia.org/wiki/Christiano_Ronaldo"
scraper_instance = WebScraperBot(host_url)
status_code,output_content = scraper_instance.getServiceDetails()
soup_instance = BeautifulSoup(output_content, 'html.parser')
# Pretty Print all the contends of the Page content Parsed
#print(soup_instance.prettify())
# Find the list of all paragraph Tags in the Page
print(soup_instance.find_all('p'))