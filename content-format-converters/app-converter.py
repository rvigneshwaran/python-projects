import pandas as pd
import traceback
import json
from flatten_json import flatten

class ContentFormatConverter:
    
    def __init__(self):
        print("Initializing Components")
        
    def read_json_file(self,input_json_path,can_flatten_json):
        outpt_df = None
        input_json_colors = None
        try:
            file_instance = open(input_json_path)
            json_data = json.load(file_instance)
            if can_flatten_json:
                input_json_colors = flatten(json_data)
                input_data = json.dumps(input_json_colors)
                input_json_colors =  json.loads(input_data)
                output_list = []
                output_list.append(input_json_colors)
                input_json_colors = output_list
            else:
                input_json_colors = json_data["colors"]
            outpt_df = pd.DataFrame.from_records(input_json_colors)
        except:
            exception_trace = str(traceback.format_exc())
            print("Exception occured while executing the method read_json_file :: ",exception_trace)
        return outpt_df
    
    def convert_contends_csv(self,input_content_data):
        df_csv = None
        source_format = input_content_data["source_format"]
        input_file_path = input_content_data["source_file_path"]
        output_file_path = input_content_data["output_file_path"]
        can_flatten_json = input_content_data["can_flatten_json"]
        try:
            if source_format == "JSON":
                read_df = self.read_json_file(input_file_path,can_flatten_json)
                read_df.to_csv(output_file_path,index=False)
                print("Data Converted to CSV Successfully")
        except:
            exception_trace = str(traceback.format_exc())
            print("Exception occured while executing the method convert_contends_csv :: ",exception_trace)
        return df_csv

    def convert_contends_json(self,input_content_data):
        df_csv = None
        source_format = input_content_data["source_format"]
        source_file_path = input_content_data["source_file_path"]
        output_file_path = input_content_data["output_file_path"]
        try:
            if source_format == "CSV":
                file_instance = pd.DataFrame(pd.read_csv(source_file_path, sep = ",", header = 0, index_col = False))
                file_instance.to_json(output_file_path, orient = "records",indent=4)
                print("Data Converted to JSON Successfully")
        except:
            exception_trace = str(traceback.format_exc())
            print("Exception occured while executing the method convert_contends_csv :: ",exception_trace)
        return df_csv
    
converter_inst = ContentFormatConverter()

# Convert the different type of input json files to a CSV
input_content_data = {}
source_format = "JSON"
input_content_data["source_format"] = source_format
source_file_path = "inputs/input-data.json"
input_content_data["source_file_path"] = source_file_path
output_file_path = "outputs/output-data.csv"
input_content_data["output_file_path"] = output_file_path
input_content_data["can_flatten_json"] = False
df_csv = converter_inst.convert_contends_csv(input_content_data)

# Convert the created csv file to json again.
input_content_data = {}
input_content_data["source_format"] = "CSV"
input_content_data["source_file_path"] = "outputs/output-data.csv"
json_file_output = "outputs/output-data.json"
input_content_data["output_file_path"] = json_file_output
output_json = converter_inst.convert_contends_json(input_content_data)