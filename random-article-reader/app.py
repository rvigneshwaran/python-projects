import requests
from bs4 import BeautifulSoup
import warnings
import re

warnings.filterwarnings("ignore")

class RandomArticleReader:
    
    def __init__(self,browse_url):
        self.browse_url = browse_url
        
    def getPageContendsAsResponse(self):
        host_url = self.browse_url
        status_code = None
        output_content = None
        try:
            response_detail = requests.get(host_url,verify=False)
            if response_detail is not None:
                status_code = response_detail.status_code
                output_content = response_detail.content
            else:
                print("failed to Access the Host")
        except Exception:
            print("failed to Access the Host")
        return status_code,output_content

    def fetch_url_contends(self,soup_instance):
        contends_text = "No Luck, Run again to Get the Article Contends !!!!"
        contends = soup_instance.find("div",{"id":"toc","class":"toc"})
        if contends is not None:
            contends_text = contends.get_text()
        return contends_text
    
    def fetch_master_contends(self,soup_instance):
        contends_text,contends_element = None,None
        contends_element = soup_instance.find("div",{"class":"mw-parser-output"})
        if contends_element is not None:
            contends_text = contends_element.get_text()
        return contends_text,contends_element
    
    def print_lineseparator(self,symbol="*",length="75"):
        print(symbol*length)
    
browser_url = "https://en.wikipedia.org/wiki/Special:Random"
random_art = RandomArticleReader(browser_url)
status_code,output_content = random_art.getPageContendsAsResponse()
soup_instance = BeautifulSoup(output_content, 'html.parser')
contends_text = random_art.fetch_url_contends(soup_instance)
print(contends_text)
random_art.print_lineseparator("*",150)
contends_text,contends_element = random_art.fetch_master_contends(soup_instance)
print(re.sub('\s{2,}', ' ', contends_text))