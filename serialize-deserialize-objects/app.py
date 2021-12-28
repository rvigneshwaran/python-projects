import pickle
from time import gmtime, strftime
import random
import string
import traceback 
import json

class SerializeDeserializeObjects:
    
    def __init__(self,max_length,file_name):
        print("Initializing Components")
        if max_length is None:
            self.max_length = 100
        else:
            self.max_length = max_length
        self.file_name = file_name
    
    def create_random_names(self,max_size=10):
        choice_of_letters = [random.choice(string.ascii_letters) for index in range(max_size)]
        random.shuffle(choice_of_letters)
        return ''.join(choice_of_letters)
        
    def create_components(self):
        response_list = []
        for index,element in enumerate(range(self.max_length)):
            response_data = {}
            response_data["id"] = index
            random_digit = int(random.choice((string.digits)))
            response_data["name"] = self.create_random_names(random_digit)
            response_data["time"] = strftime("%Y-%m-%d %H:%M:%S", gmtime())
            response_list.append(response_data)
        return response_list
    
    def persist_data_pickle(self,complex_store):
        try:
            file_instance = open(self.file_name, 'wb')
            pickle.dump(complex_store, file_instance)
            file_instance.close()
            print("Data Serialized Successfully !!!! ")
        except:
            print("Exception occured while executing the method persist_data_picke :: ",str(traceback.print_exc()))
            
    def write_data_file(self,output_response):
        output_file = "outputs/response-data.json"
        try:
            if output_file is not None:
                with open(output_file, "w") as outfile:
                    json.dump(output_response, outfile,indent=4,)
        except:
            print("Exception occured while executing the method write_data_file")
            print(traceback.print_exc())

    def retrive_persisted_data(self):
        try:
            file_instance = open(self.file_name, 'rb')     
            complex_store = pickle.load(file_instance)
            if complex_store is not None:
                result = json.dumps(complex_store)
                json_result = json.loads(result)
                self.write_data_file(json_result)
                print("Data deserialzed Successfully !!!! ")
            else:
                print("Data NOT deserialzed Successfully !!!! ")
            #file_instance.close()
        except:
            print("Exception occured while executing the method persist_data_picke :: ",str(traceback.print_exc()))

file_name = 'store/complex_store.model'            
object_instance = SerializeDeserializeObjects(100,file_name)
complex_store = object_instance.create_components()
if complex_store is not None:
    print(complex_store[0:1])
    object_instance.persist_data_pickle(complex_store)
    object_instance.retrive_persisted_data()