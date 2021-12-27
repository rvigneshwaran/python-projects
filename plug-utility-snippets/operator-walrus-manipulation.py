import string
import random
import datetime

character_list = string.ascii_letters

class OperatorWalrus:
    
    def __init__(self):
        print("Initializing Component for using the Walrus operator")
        lending_list = []
        for index,element in enumerate(range(10)):
            lending_dict = {}
            element = ''.join(random.choice(character_list) for index in range(10+index))
            lending_dict["id"] = id
            lending_dict["name"] = element
            place_l = self.generate_random_element(25)
            random.shuffle(place_l)
            lending_dict["place"] = ''.join(place_l)
            lending_dict["time"] =  datetime.datetime.now()
            lending_list.append(lending_dict)
        self.lending_list = lending_list
        
    def generate_random_element(self,length=10):
        return [random.choice(character_list) for index in range(length)]
        
    def walrus_usage(self):
        lending_list = self.lending_list
        if lending_list is not None and len(lending_list) > 0:
            for indv_element in lending_list:
                if name_element := indv_element.get("name"):
                    print("The value of the Name element is :: ",name_element)
                    
wal_instance = OperatorWalrus()
wal_instance.walrus_usage()
            