import pandas as pd
import traceback
import json

class ContentFormatConverter:
    
    def __init__(self):
        print("Initializing Components")
        
    def read_json_file(self,input_json_path):
        outpt_df = None
        try:
            file_instance = open(input_json_path)
            json_data = json.load(file_instance)
            input_json_colors = json_data["colors"]
            # TODO if its a nested JSON it has to recursively iterated to find out whether its an instance of a list or dict and then then the final json should be formed before sending the input to convert to csv.
            outpt_df = pd.DataFrame.from_records(input_json_colors)
        except:
            exception_trace = str(traceback.format_exc())
            print("Exception occured while executing the method read_json_file :: ",exception_trace)
        return outpt_df
    
    def convert_contends_csv(self,source_format,source_contends,output_path):
        df_csv = None
        try:
            if source_format is not None and source_format == "JSON":
                input_df = pd.DataFrame(source_contends)
                df_csv = input_df.to_csv(output_path,index=False)
                print("Converted to CSV and Write to file Success")
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
                file_instance.to_json(output_file_path, orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)
                print("Conversion to JSON Completed and Write to file Success")
        except:
            exception_trace = str(traceback.format_exc())
            print("Exception occured while executing the method convert_contends_csv :: ",exception_trace)
        return df_csv
    
converter_inst = ContentFormatConverter()

input_json_data_path = "inputs/input-data.json"
csv_output_path = "outputs/output-data.csv"
output_df = converter_inst.read_json_file(input_json_data_path)
if output_df is not None:
    print("The data is read from json successfully :: with dataframe length :: ",len(output_df))
    df_csv = converter_inst.convert_contends_csv("JSON",output_df,csv_output_path)
    
# Convert the created csv file to json again.
input_content_data = {}
input_content_data["source_format"] = "CSV"
input_content_data["source_file_path"] = csv_output_path
json_file_output = "outputs/output-data.json"
input_content_data["output_file_path"] = json_file_output
output_json = converter_inst.convert_contends_json(input_content_data)
