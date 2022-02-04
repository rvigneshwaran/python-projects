import subprocess
import traceback 
import configparser
import json
import codecs
import re
from re import search
class ExecuteExternalProcess:
    
    def __init__(self,config_file_path):
        """[This is an Initialization Component]

        Args:
            config_file_path ([type]): [description]
        """
            
        print("Initializing Components")
        config_instance = configparser.ConfigParser()
        config_instance.read(config_file_path)
        self.config_instance = config_instance
        
    def convert_filecontents_utf8(self,input_file_name,output_file_name):
        BLOCKSIZE = 1048576
        with codecs.open(input_file_name, "r") as sourceFile:
            with codecs.open(output_file_name, "w", "utf-8") as targetFile:
                while True:
                    contents = sourceFile.read(BLOCKSIZE)
                    if not contents:
                        break
                    targetFile.write(contents)
                
    def write_contends_to_file(self,fileName,encoding_input,inputContent):
        """[This Method is intended to write the contends of the output to a file depends on the file type configured , the default output would be a json file and the input for any type of file would be a dictionary]

        Args:
            fileName ([type]): [description]
            encoding_input ([type]): [description]
            inputContent ([type]): [description]
        """
        with open(fileName, 'w', encoding=encoding_input) as file_ins:
            json.dump(inputContent,file_ins, ensure_ascii=False, indent=4)
            
    def find_between(self,input_content, first, last ):
        try:
            start = input_content.index(first) + len(first)
            end = input_content.index(last,start)
            return input_content[start:end]
        except ValueError:
            return None
        
    def find_element_list(self,input_list,first_element,last_element):
        element_content = None
        if input_list is not None and len(input_list) > 0:
            for index,element in enumerate(input_list):
                print("index :: "+str(index)+" Element :: "+element)
                element = ''.join(e for e in element if e.isalnum())
                if "NAME" in element:
                    print("Name is Present in the list at Index :: "+str(index))
            start_index = input_list.index(first_element)
            print("The Index of the start element :: "+first_element+" is :: "+str(start_index))
            end_index = input_list.index(last_element)
            print("The Index of the end element :: "+last_element+" is :: "+str(end_index))
            element_content = input_list[start_index:end_index]
            
        return element_content

    def read_text_file(self,file_name):
        read_data_content = None
        with open(file_name, 'r',encoding="utf-8") as file:
            read_data_content = file.read().replace('\n', '')
        return read_data_content
    
    def parse_text_file_output(self,text_file_content,command_executed):
        """[This function is intended to execute the individual command and the parse the documentation and get the details from
        the documentation and prepare the dictionary]

        Args:
            text_file_content ([str]): [Output of the command]
            command_executed ([str]): [what is the command executed]

        Returns:
            [dict]: [help content formulated as a dictionary]
        """
        command_output_cons = {}
        command_output_cons["executed_command"] = command_executed
        if text_file_content is not None and len(text_file_content) > 0:
            #text_file_content = text_file_content.lower()
            #print(text_file_content)
            try:
                text_conetnt_list = text_file_content.splitlines()
                text_file_content = [input_string.strip() for input_string in text_file_content]
                self.find_element_list(text_conetnt_list,"NAME","SYNOPSIS")
            except Exception as exception_instance:
                error_instance = str(traceback.format_exc())
                print("Exception Occured while executing the method parse_text_file_output :: "+error_instance)
        return command_output_cons
        
    def prepare_command_dict(self,command_list):
        command_output_list = [] 
        error_command_list = []
        if command_list is not None and len(command_list) > 0:
            for indv_command in command_list[0:1]:
                command_output_cons = {}
                try:
                    indv_command_mod = "man "+indv_command
                    text_file_content = self.execute_shell_command(indv_command_mod)
                    text_file_content = text_file_content.decode("utf-8")
                    command_output_cons = self.parse_text_file_output(text_file_content,indv_command)
                    print(command_output_cons)
                except Exception as except_instance:
                    error_ins = str(traceback.format_exc())
                    error_command_list.append(indv_command)
                    command_output_cons["executed_command"] = indv_command
                    command_output_cons["command_output"] = error_ins
                command_output_list.append(command_output_cons)
        return command_output_list,error_command_list
        
    def execute_shell_command(self,command_input):
        """[This Method Is intended to execute the command in th external and then create a dictionary out of the command output , The dictionary created is processes and then send according to the filter parameters]

        Returns:
            [type]: [description]
        """
        command_output = None
        try:
            subprocess_ins = subprocess.Popen(command_input, shell=True, stdout=subprocess.PIPE)
            command_output = subprocess_ins.stdout.read()
        except Exception as exec_instance:
            error_trace = str(traceback.format_exc())
            print("Exception occured while executing the method exeecute_command :: "+error_trace)
        return command_output
        
    def prepare_readme_file(self):
        """[This Method is Used to generate a read me file from the output configued as part of the config file on what are the parameters that should be present as part of the entitlement]

        Returns:
            [type]: [description]
        """        """"""
        return False

# Initialize and retrive config from the file.
config_file_path = "config/inter-config.properties"
service_trigger =  ExecuteExternalProcess(config_file_path)
# Load all the config data from the proprties 
config_ins = service_trigger.config_instance

# snippet to get the list of commands for which help can be executed
initial_command_input = config_ins.get("primaryConfigList","intialCommand")
help_appender = config_ins.get("primaryConfigList","helpappender")
response_output = service_trigger.execute_shell_command(initial_command_input)
response_output_plain = str(response_output.decode("utf-8"))
command_list =  response_output_plain.splitlines()
print("The Total commands available :: "+str(len(command_list)))

# execute the command and prepare a basic dictionary.
command_output_list,error_command_list = service_trigger.prepare_command_dict(command_list)
print(command_output_list)

# write the contends of the result to a file.
output_file_name = "outputs/response-output.json"
output_encodings = "utf-8"
service_trigger.write_contends_to_file(output_file_name,output_encodings,command_output_list)