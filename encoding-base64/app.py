import base64

class Base64EncoderDecoder:
    
    def encode_input_content(self,input_content):
        byte_content = input_content.encode("ascii")
        encoded_string = base64.b64encode(byte_content)
        print("Encoded String :: ",encoded_string)
        return encoded_string
    
    def decode_input_content(self,encoded_string):
        decoded_byte = base64.b64decode(encoded_string)
        decoded_string = decoded_byte.decode("ascii")
        print("Decoded String :: ",decoded_string)
        return decoded_string
    
base64_instance = Base64EncoderDecoder()
input_string = "Tel Aviv, Israel"
encoded = base64_instance.encode_input_content(input_string)
base64_instance.decode_input_content(encoded)