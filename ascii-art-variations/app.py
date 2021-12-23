import pyfiglet

class ASCIIArtVariations:
    
    def __init__(self):
        print("Initializing parameters for ASCII Art")
        
    def create_art_pyfiglet(self,config_params):
        output_response = None
        input_text = config_params["input_text"]
        if "font" in config_params:
            output_response = pyfiglet.figlet_format(input_text,font=config_params["font"])
        else:
            output_response = pyfiglet.figlet_format(input_text)
        print(output_response)
        
art_variations = ASCIIArtVariations()
config_params = {}
config_params["input_text"] = "Ronaldo"
art_variations.create_art_pyfiglet(config_params)
font_list = ["slant","3-d","3x5","5lineoblique","alphabet","banner3-D","doh","isometric1","letters","alligator","dotmatrix","bubble","bulbhead"]
for indv_font in font_list:
    print("Rendering ASCII Art for the font : "+indv_font+"\n")
    config_params["font"] = indv_font
    art_variations.create_art_pyfiglet(config_params)