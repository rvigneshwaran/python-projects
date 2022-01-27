import pyqrcode
from pyqrcode import QRCode
import calendar
import time

class QRCodeGenerator:
    
    def __init__(self):
        print("Initializing Components")
        
    def get_current_timestamp(self):
        time_instance = time.gmtime()
        return str(calendar.timegm(time_instance))
    
    def generate_qrcode(self,input_content,file_type,input_file_name):
        generated_code = pyqrcode.create(input_content)
        time_stamp = self.get_current_timestamp()
        output_file_name = "outputs/"+input_file_name+"_"+time_stamp
        if file_type == "svg":
            generated_code.svg(output_file_name+".svg",scale = 10)
            print("QR Code Generated for the Input content with file type :: "+file_type)
            
qrcode_instance = QRCodeGenerator()
input_content = "https://github.com/rvigneshwaran"
output_file_name = "rvigneshwaran-github"
qrcode_instance.generate_qrcode(input_content,"svg",output_file_name)
