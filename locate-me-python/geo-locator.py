from geopy.geocoders import Nominatim
from geopy import geocoders
from geopy.distance import geodesic
import json
import traceback

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
    
    def calculate_distance(self,source_place,dest_place,units="km"):
        """[Method intended to calculate the distance between two place on Earth without considering the dimention time :)]

        Args:
            source_place ([string]): [Input the source from which the distance should be mesured]
            dest_place ([string]): [Inputs the destination to which the distance is mesured]
            units (str, string): [In Which Unit the method should produce output]. Defaults to "km".

        Returns:
            [Number]: [Produces the distance between the source and the destination location]
        """
        distance_value = None
        try:
            source = geolocator.geocode(source_place)
            source_coord = (source.latitude,source.longitude)
            print("The Coordinates for the source location :: "+source_place+" is "+str(source_coord))
            destination = geolocator.geocode(dest_place)
            dest_coord = (destination.latitude,destination.longitude)
            print("The Coordinates for the destination location :: "+dest_place+" is "+str(dest_coord))
            if units == "km":
                distance_value = geodesic(source_coord, dest_coord).kilometers
            elif units == "miles":
                distance_value = geodesic(source_coord, dest_coord).miles
            elif units == "m":
                distance_value = geodesic(source_coord, dest_coord).meters
        except:
            error_response = str(traceback.format_exc())
            print("Exception Occured while executing the method :: calculate_distance "+error_response)
        return distance_value
        
geo_locate = GeoLocatorComponent()
coord_inst = geo_locate.decode_coord_byplace("Coimbatore")
print("Decoded :: ",coord_inst)
geo_locate.apply_separator()

coord_input = "11.028,76.902"
located_place = geo_locate.decode_place(coord_input)
print(geo_locate.pretty_print(located_place))
geo_locate.apply_separator()

source_place = "Coimbatore"
destination_place = "Chennai"
units = "km"
distance_value = geo_locate.calculate_distance(source_place,destination_place,units)
print("The distance between source :: "+source_place+" and destination place :: "+destination_place+ " is :: "+str(distance_value) + " "+ units)
geo_locate.apply_separator()