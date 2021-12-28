import pickle
from time import gmtime, strftime
import random
import string
import traceback 
import json

class SerializeDeserializeObjects:
    
    def __init__(self,max_length):
        print("Initializing Components")
        if max_length is None:
            self.max_length = 100
        else:
            self.max_length = max_length
    
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
            file_instance = open('store/complex_store.model', 'ab')
            pickle.dump(complex_store, file_instance)
            file_instance.close()
            print("Data Serialized Successfully !!!! ")
        except:
            print("Exception occured while executing the method persist_data_picke :: ",str(traceback.print_exc()))
            
    def retrive_persisted_data(self,fileName):
        try:
            file_instance = open('store/complex_store.model', 'rb')     
            complex_store = pickle.load(file_instance)
            result = json.dumps(complex_store,sort_keys=True, indent=4)
            print(result)
            file_instance.close()
            print("Data deserialzed Successfully !!!! ")
        except:
            print("Exception occured while executing the method persist_data_picke :: ",str(traceback.print_exc()))
            
object_instance = SerializeDeserializeObjects(None)
complex_store = object_instance.create_components()
print(complex_store[0:1])
object_instance.persist_data_pickle(complex_store)
object_instance.retrive_persisted_data("")