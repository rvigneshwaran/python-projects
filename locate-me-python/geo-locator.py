from geopy.geocoders import Nominatim
import json

geolocator = Nominatim(user_agent="GeoLocatorComponent")

class GeoLocatorComponent:
    
    def __init__(self):
        print("Team is lost , Loading to locate the team in Earth")
        
    def apply_separator(self,max_size=100):
        print("*" * max_size)
        
    def decode_coord_byplace(self,place_name):
        """[Get the complete address of the location using the place name]

        Args:
            place_name ([String]): [name of the place]

        Returns:
            [string]: [complete address of the place]
        """
        location = geolocator.geocode(place_name)
        return location
    
    def pretty_print(self,input_dict,indent_size=4):
        """[Apply Indendation for the dict using the json module]

        Args:
            input_dict ([dict]): [input dictionary where the indendation and formatiing is going to be applied]
            indent_size (int, optional): [Spacing Config]. Defaults to 4.

        Returns:
            [type]: [description]
        """
        return json.dumps(input_dict,sort_keys=True, indent=indent_size)
        
    def decode_place(self,coordinates):
        """[Find the place decoding the coordinates]

        Args:
            coordinates ([string]): [lat and long of the places as comma separated string type]

        Returns:
            [str]: [returns the complete address of the place with place,city and state]
        """
        address = None
        location_ins = geolocator.reverse(coordinates)
        if location_ins is not None :
            address = location_ins.raw
        return address
        
geo_locate = GeoLocatorComponent()
coord_inst = geo_locate.decode_coord_byplace("Coimbatore")
print("Decoded :: ",coord_inst)
geo_locate.apply_separator()
coord_input = "11.028,76.902"
located_place = geo_locate.decode_place(coord_input)
print(geo_locate.pretty_print(located_place))
geo_locate.apply_separator()