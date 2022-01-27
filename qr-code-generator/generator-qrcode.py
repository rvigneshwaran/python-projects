import qrcode
import calendar
import time

class QRCodeGenerator:
    
    def __init__(self):
        print("Initializing components")
        
    def get_current_timestamp(self):
        """[Method Intended to geerate a Timestamp as Stirng ]

        Returns:
            [str]: [Generate the Timestamp component as String]
        """
        time_instance = time.gmtime()
        return str(calendar.timegm(time_instance))
        
    def save_generated_qrcode(self,code_instance,output_file_name):
        if code_instance is not None:
            code_instance.save(output_file_name)
        
    
    def code_generator(self,input_content):
        code_instance = qrcode.make(input_content)
        output_file = "outputs/"+"qr_code_generated_"+self.get_current_timestamp()+".png"
        code_instance.save(output_file)
        
instance = QRCodeGenerator()
input_data_content = "https://github.com/rvigneshwaran?tab=repositories"
instance.code_generator(input_data_content)
print("QR Code Generated for the Input Content Configured")