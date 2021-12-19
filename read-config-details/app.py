import configparser
import traceback 

config_file_path = "../read-config-details/config/app-config.properties"
class ReadConfigDetails:

    def __init__(self):
        self.config_instance = configparser.ConfigParser()
        self.config_instance.read(config_file_path)
        
    def getAllSection(self):
        """ Method Intended to get all the sections from the config

        Returns:
            [list]: [returns the section names as list]
        """
        config_instance = self.config_instance
        section_list=None
        if config_instance is not None:
            section_list = config_instance.sections()
        return section_list
    
    def getSectionBykey(self,sectionName):
        """Method intended to get the individual section details by using the key,
        all the key and values under the section will be retrived

        Args:
            sectionName ([String]): [section name from the config file]

        Returns:
            [dict]: [returns the section details as dictionary]
        """""
        config_instance = self.config_instance
        indv_section = None
        section_list = self.getAllSection()
        if config_instance is not None and sectionName is not None and sectionName in section_list:
            indv_section = config_instance[sectionName]
        return indv_section
    
    def doesSectionHasKey(self,sectionName,key):
        """[Method intended to check whether the section has the option , if the section 
        has the option key the method will return true else false]

        Args:
            sectionName ([String]): [Section Name from the Config]
            key ([String]): [Option key name under the Section from Config file]

        Returns:
            [Boolean]: [Return True if present else it returns False]
        """
        config_instance = self.config_instance
        if config_instance is not None and config_instance.has_section(sectionName) and config_ins.has_option(key):
            return True
        return False
    
    def doesConfigHasSection(self,sectionName):
        """[Method Intended to verify whether the confg file has the section]

        Args:
            sectionName ([String]): [Section Name from the config file]

        Returns:
            [Boolean]: [returns True if Section is Present else it returns False]
        """
        config_instance = self.config_instance
        if config_instance is not None and config_instance.has_section(sectionName):
            return True
        return False
    
    def addSectionToConfig(self,sectionDict,sectionName):
        """[Method intended to add a new section to the config file]

        Args:
            sectionDict ([Dict]): [Newly added key value pairs under the section]
            sectionName ([String]): [Section name added to the config]
        """
        try:
            config_instance = self.config_instance
            if config_instance is not None:
                config_instance.add_section(sectionName)
            for key,value in sectionDict.items():
                config_instance.set(sectionName,key,value)
            file_instance = open(config_file_path,'w')
            config_instance.write(file_instance)
            file_instance.close()
        except Exception:
            print(traceback.format_exc())
            print("Exception Occured while adding new section to the config file")
    
    def getAllvaluesInConfig(self):
        """[Method Intended to get all the values from the Config file]

        Returns:
            [Dict]: [Complete Config as dictionary]
        """
        condolidated_dict = {}
        config_instance = self.config_instance
        if config_instance is not None:
            for indv_section in config_instance.sections():
                indv_dict = dict(config_instance[indv_section])
                condolidated_dict[indv_section] = indv_dict
        return condolidated_dict
    
    def removeSection(self,sectionName):
        """[Method intended to remove the section from the Config file using the Section name]

        Args:
            sectionName ([String]): [Section Name from the Config file]
        """
        config_instance = self.config_instance
        if config_instance is not None:
            config_instance.remove_section(sectionName)
            file_instance = open(config_file_path,'w')
            config_instance.write(file_instance)
            file_instance.close()
            print("Section Deleted from Config Sucessfully")
        
read_config_instance = ReadConfigDetails()
config_ins = read_config_instance.config_instance
# Get All the section details in the Config
print(read_config_instance.getAllSection())
# Get the Section details using the key
print(dict(read_config_instance.getSectionBykey("mysql")))
# Get all the values in the config 
print(read_config_instance.getAllvaluesInConfig())
# Add new section to the config file
section_name = "file-paths"
new_section = {}
new_section["log_path"] = "log/application-log.1.log"
new_section["response_path"] = "results/output-response.json"
new_section["input_file_path"] = "input/source-input-data.xlsx"
read_config_instance.addSectionToConfig(new_section,section_name)
print(read_config_instance.getAllSection())
# Check if the file has section
print("doesConfigHasSection :: ",read_config_instance.doesConfigHasSection(section_name))
# Remove the Newly created section from the config file
read_config_instance.removeSection(section_name)