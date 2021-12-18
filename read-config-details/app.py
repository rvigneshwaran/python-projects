import configparser

class ReadConfigDetails:

    def __init__(self):
        self.config_instance = configparser.ConfigParser()
        self.config_instance.read("read-config-details/config/app-config.properties")
        

read_config_instance = ReadConfigDetails()
config_ins = read_config_instance.config_instance
sections = config_ins.sections()
print(sections)