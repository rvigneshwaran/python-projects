import base64

class Base64EncoderDecoder:
    
    def encode_input_content(self,input_content):
        """[Method intended to Convert the Input String to Base 64 Format]

        Args:
            input_content ([String]): [Input String to be Encoded]

        Returns:
            [String]: [Encoded String by Base 64 Format]
        """
        byte_content = input_content.encode("ascii")
        encoded_string = base64.b64encode(byte_content)
        print("Encoded String :: ",encoded_string)
        return encoded_string
    
    def decode_input_content(self,encoded_string):
        """[Method intended to Decode the encoded Stirng using base 64 Lib]

        Args:
            encoded_string ([String]): [Encoded String to be decoded]

        Returns:
            [String]: [Decoded String]
        """
        decoded_byte = base64.b64decode(encoded_string)
        decoded_string = decoded_byte.decode("ascii")
        print("Decoded String :: ",decoded_string)
        return decoded_string
    
    def validate(self,decoded_input,original_input):
        """[Method intended to validate whether the decoded string is same as the original string]

        Args:
            decoded_input ([String]): [decoded string from the encoded string ]
            original_input ([Stirng]): [original input string which was encoded]

        Returns:
            [String]: [Whether the encoding is a success or not]
        """
        if decoded_input is not None and original_input is not None and decoded_input ==  original_input:
            return "The Encoding and Decoding of Contends is Success"
        else:
            return "Something got messsaged Up"
    
base64_instance = Base64EncoderDecoder()
input_string = "Tel Aviv, Israel"
encoded = base64_instance.encode_input_content(input_string)
decoded = base64_instance.decode_input_content(encoded)
print(base64_instance.validate(decoded,input_string))