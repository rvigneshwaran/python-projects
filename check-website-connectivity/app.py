import json
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import requests
import pandas as pd
import configparser
import warnings
warnings.filterwarnings("ignore")

config_file_path = "config/app-config.properties"
config_instance = configparser.ConfigParser()
config_instance.read(config_file_path)
class CheckWebsiteConnectivity:
    
    def __init__(self,input_file_path,time_out_config):
        """[Initializing parameters Before the Main Loagic Starts]

        Args:
            input_file_path ([String]): [File Path of the Input file which we are going to parse]
            time_out_config ([String]): [time out config for validating the connectivity]
        """
        if input_file_path is not None:
            file_instance = open(input_file_path)
            input_data = json.load(file_instance)
            self.input_data =  input_data
            self.time_out_config = time_out_config
            file_instance.close()
            
    def check_website_connectivity_request(self,website_url):
        """[Method Intended to validate the web connectivity using the request lib]

        Args:
            website_url ([String]): [Web Site URL to validate]

        Returns:
            [Boolean]: [returns True if the site is up else returns False]
        """
        isWebSiteUp = True
        try:
            site_response = requests.get(website_url,verify=False)
            if site_response.status_code != 200:
                isWebSiteUp = False
        except Exception:
            isWebSiteUp = False
            print(f"The Website {website_url} is not reachable")
        return isWebSiteUp
    
    def check_website_connectivity_url(self,website_url):
        """[Method Intended to test the website connectivity using the URL lib]

        Args:
            website_url ([String]): [Web site to be evaluated]

        Returns:
            [Boolean]: [returns True if the site is Up else False]
        """
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
        """[Method Intended to write the contends in a file]

        Args:
            fileName ([String]): [File Path with the File Name of the Output file]
            encoding_input ([String]): [Type of Encoding that should be applied]
            inputContent ([List]): [List of Dictionary content that should be writtern to the file]
        """
        with open(fileName, 'w', encoding=encoding_input) as file_ins:
            json.dump(inputContent,file_ins, ensure_ascii=False, indent=4)
        print("Completed Writing the Response contends")
    
    def test_site_connectivity(self,response_file_name,encoding_inp):
        """[Method Inetnded to Iterate through the list and evaluate the 
        connectivity of the list one by one]

        Args:
            response_file_name ([String]): [Out put file Name]
            encoding_inp ([type]): [Encoding which the file has to be writtern]

        Returns:
            [List]: [Output which has the status of the website connectivity]
        """
        input_contends = self.input_data
        updated_contends_list = []
        if input_contends is not None and len(input_contends) > 0:
            for indv_contnds in input_contends[0:5]:
                website_url = indv_contnds["SiteLink"]
                print("Evaluating for the URL :: ",website_url)
                isWebsiteUp = self.check_website_connectivity_request(website_url)
                indv_contnds["isWebsiteUp"] = isWebsiteUp
                updated_contends_list.append(indv_contnds)
        self.write_contends_to_file(response_file_name,encoding_inp,updated_contends_list)
        return updated_contends_list
    
    def write_contends_toXlsx(self,inputFileName,contendsList):
        """[Method Intended to write the contends in a Xlsx file]

        Args:
            inputFileName ([String]): [file name of the output file]
            contendsList ([List]): [contends that should be writtern in the file]
        """
        if contendsList is not None and len(contendsList) > 0:
            content_df = pd.DataFrame(contendsList)
            writer_instance = pd.ExcelWriter(inputFileName)
            content_df.to_excel(writer_instance,index=False)
            writer_instance.save()
            print("Output contends write to xlsx file complete")

# load the onfig Contends from the config file
inp_jsonfile_path = config_instance.get("app-config-data","inp_jsonfile_path")
out_xlsx_filepath = config_instance.get("app-config-data","out_xlsx_filepath")
out_json_filepath = config_instance.get("app-config-data","out_json_filepath")
encoding = config_instance.get("app-config-data","encoding")
time_out_config = config_instance.get("app-config-data","time_out_config")

connect_inst = CheckWebsiteConnectivity(inp_jsonfile_path,time_out_config)
updated_contends_list = connect_inst.test_site_connectivity(out_json_filepath,encoding)

# Write the contends to an excel file
updated_contends_list = connect_inst.write_contends_toXlsx(out_xlsx_filepath,updated_contends_list)