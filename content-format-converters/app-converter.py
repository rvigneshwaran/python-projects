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
            outpt_df = pd.DataFrame.from_records(input_json_colors)
        except:
            exception_trace = str(traceback.format_exc())
            print("Exception occured while executing the method read_json_file :: ",exception_trace)
        return outpt_df
    
    def convert_contends_csv(self,source_format,source_contends,output_path):
        df_csv = None
        try:
            if source_format is not None and source_format == "CSV":
                input_df = pd.DataFrame(source_contends)
                df_csv = input_df.to_csv(output_path,index=False)
                print("Converted to CSV and Write to file Success")
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
    df_csv = converter_inst.convert_contends_csv("CSV",output_df,csv_output_path)
