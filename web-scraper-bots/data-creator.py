import requests
from bs4 import BeautifulSoup
import json

class DataCreatorBot:
    
    def getSiteDataAsText(self,token_url):
        status_code = None
        output_content = None
        try:
            response_detail = requests.get(token_url,verify=False)
            if response_detail is not None:
                status_code = response_detail.status_code
                print("The response status code is :: ",status_code)
                output_content = response_detail.content
            else:
                print("failed to Access the Host")
        except Exception:
            print("failed to Access the Host")
        return status_code,output_content
    
    def write_contends_to_file(self,fileName,encoding_input,inputContent):
        with open(fileName, 'w', encoding=encoding_input) as file_ins:
            json.dump(inputContent,file_ins, ensure_ascii=False, indent=4)
    
    def parse_input_data(self,soup_instance):
        # Find the Second Table in the Page
        secondtable = soup_instance.findAll('table')[1]
        tr_list = secondtable.find_all('tr')
        completed_parsed_list = []
        for indv_tr_element in tr_list:
            indv_element = {}
            td_list = indv_tr_element.find_all("td")
            indv_element["SiteId"] = td_list[0].get_text()
            indv_element["SiteName"] = td_list[1].get_text()
            indv_element["SiteLink"] = td_list[2].get_text()
            anc_element = td_list[3].find('a')
            if anc_element is not None:
                indv_element["SiteRTILink"] = anc_element.get("href")
            completed_parsed_list.append(indv_element)
        print(completed_parsed_list)
        return completed_parsed_list
        
data_creator_instance = DataCreatorBot()
token_url = "https://rti.gov.in/rti/allministry.asp"
status_code,response_data = data_creator_instance.getSiteDataAsText(token_url)
soup_instance = BeautifulSoup(response_data, 'html.parser')
for a in soup_instance.find_all('a', href=True):
    print("Determined URL :: ",a['href'])

completed_parsed_list = data_creator_instance.parse_input_data(soup_instance)
file_path = "outputs/response-output.json"
encoding_input = "UTF-8"
data_creator_instance.write_contends_to_file(file_path,encoding_input,completed_parsed_list)
print("Completed Writing Contends to file")