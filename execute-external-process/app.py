import subprocess
import traceback 
import configparser
import json

class ExecuteExternalProcess:
    
    def __init__(self,config_file_path):
        print("Initializing Components")
        config_instance = configparser.ConfigParser()
        config_instance.read(config_file_path)
        self.config_instance = config_instance
        
    def write_contends_to_file(self,fileName,encoding_input,inputContent):
        """[This Method is intended to write the contends of the output to a file depends on the file type configured , the default output would be a json file and the input for any type of file would be a dictionary]

        Args:
            fileName ([type]): [description]
            encoding_input ([type]): [description]
            inputContent ([type]): [description]
        """
        with open(fileName, 'w', encoding=encoding_input) as file_ins:
            json.dump(inputContent,file_ins, ensure_ascii=False, indent=4)
        
    def prepare_command_dict(self,command_list):
        command_output_list = [] 
        error_command_list = []
        if command_list is not None and len(command_list) > 0:
            for indv_command in command_list[0:3]:
                command_output_cons = {}
                try:
                    indv_command = "help "+indv_command+" > sample_command.txt"
                    command_output = self.execute_shell_command(indv_command)
                    if command_output is not None and len(command_output) > 0:
                        command_output_cons["executed_command"] = indv_command
                        command_output_cons["command_output"] = command_output
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

config_file_path = "config/inter-config.properties"
service_trigger =  ExecuteExternalProcess(config_file_path)
config_ins = service_trigger.config_instance
initial_command_input = config_ins.get("primaryConfigList","intialCommand")
response_output = service_trigger.execute_shell_command(initial_command_input)
response_output_plain = str(response_output.decode("utf-8"))
command_list =  response_output_plain.splitlines()
print("The Total commands available :: "+str(len(command_list)))
command_output_list,error_command_list = service_trigger.prepare_command_dict(command_list)
output_file_name = "outputs/response-output.json"
output_encodings = "utf-8"
print(command_output_list)
service_trigger.write_contends_to_file(output_file_name,output_encodings,command_output_list)