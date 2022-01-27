from bs4 import BeautifulSoup
from applicationutils import Applicationutils
import json

import warnings
warnings.filterwarnings("ignore")

class MoneyControlScraper:
    
    def __init__(self):
        print("Loading components for MoneyControlScraper")
        
    def find_content_key(self,soup_instance):
        heading_list = []
        indv_category = None
        if soup_instance is not None:
            heading_data = soup_instance.find_all('th')
            for individual_header in heading_data:
                if individual_header.find("span") is not None:
                    indv_category = individual_header.find("span").get_text()
                else:
                    heading_list.append(individual_header.get_text())
        return indv_category,heading_list
        
    def parse_main_contends(self,soup_instance):
        if soup_instance is not None:
            consolidated_fund_list = []
            detail_table_list = soup_instance.find_all("table",{"class":"mctable1","width":"100%"})
            print("The Total Found :: ",len(detail_table_list))
            for indv_table in detail_table_list:
                mutual_fund_details = {}
                indv_category,heading_list = self.find_content_key(indv_table)
                mutual_fund_details["fund_type"] = indv_category
                mutual_fund_details["headings_list"] = heading_list
                console_fund_list = []
                table_row_list = indv_table.find_all("tr")
                for indv_trelement in table_row_list:
                    indv_fund_details = {}
                    detail_td_list = indv_trelement.find_all("td")
                    for index,indv_td in enumerate(detail_td_list):
                        if indv_td.find("a") is not None:
                            anc_element = indv_td.find("a",{"class":"robo_medium"})
                            if anc_element is not None:
                                fund_name = anc_element.get_text()
                                print("Exceuting Parsing for the fund :: "+fund_name)
                                indv_fund_details["fund_name"] = fund_name
                                if anc_element.has_attr('title'):
                                    indv_fund_details["fund_title"] = anc_element["title"]
                                if anc_element.has_attr('href'):
                                    indv_fund_details["fund_link"] = anc_element["href"]
                        else:
                            index = index - 1
                            indv_fund_details[heading_list[index]] = indv_td.get_text()
                    if indv_fund_details is not None and len(indv_fund_details) > 0:
                        console_fund_list.append(indv_fund_details)
                mutual_fund_details["fund_details"] = console_fund_list
                consolidated_fund_list.append(mutual_fund_details)
        return consolidated_fund_list
        
money_ins = MoneyControlScraper()
website_url = "https://www.moneycontrol.com/mutualfundindia/"
soup_instance = Applicationutils.getWebSiteContendsAsHTML(website_url)
consolidated_fund_list = money_ins.parse_main_contends(soup_instance)
output_file = "outputs/mutual-funds-data.json"
Applicationutils.write_contends_to_file(output_file,"utf-8",consolidated_fund_list)