import pandas as pd
import traceback

class ContentFormatConverter:
    
    def __init__(self):
        print("Initializing Components")
        
    def read_json_file(self,input_json_path):
        outpt_df = None
        if input_json_path is not None:
            outpt_df = pd.read_json('data.json')
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
output_df = converter_inst.read_json_file(input_json_data_path)
csv_output_path = "outputs/output-data.csv"
df_csv = converter_inst.convert_contends_csv("CSV",output_df,csv_output_path)
