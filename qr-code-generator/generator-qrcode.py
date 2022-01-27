import qrcode
import calendar
import time

class QRCodeGenerator:
    
    def __init__(self):
        print("Initializing components")
        qrcode_instance = qrcode.QRCode(version = 1,box_size = 10,border = 5)
        self.qrcode_instance = qrcode_instance
        
    def get_current_timestamp(self):
        """[Method Intended to geerate a Timestamp as Stirng ]

        Returns:
            [str]: [Generate the Timestamp component as String]
        """
        time_instance = time.gmtime()
        return str(calendar.timegm(time_instance))
        
    def save_generated_qrcode(self,code_instance,output_file_name):
        """[Method Intended to save the Generated QR Code in to a file to the putputs Folder]

        Args:
            code_instance ([qrcode]): [instance of the QR Code to generate]
            output_file_name ([str]): [file path of the outpt file name]
        """
        if code_instance is not None:
            code_instance.save(output_file_name)
            
    def get_value(self,input_dict,input_key):
        """[Get the Value from the dictionary using the key else returns null]

        Args:
            input_dict ([dict]): [Input dictionary where the key should be searched and then the value of the key should be return]
            input_key ([str]): [Key from the dictionary]

        Returns:
            [str]: [value]
        """
        return input_dict[input_key] if input_key in input_dict else None

    def apply_customizations(self,customize_dict,qrcode_instance):
        """[Method Intended to add Customizations using the Custmize dictionary]

        Args:
            customize_dict ([dict]): [Customization Dictionary Configured ]
            qrcode_instance ([qrcode]): [Instance of QR Code]

        Returns:
            [rqcode]: [qrcode instance with the customizations configured]
        """
        #TODO Configure the below values as JSON in a config file, So that the configurations can be scaled up and included
        fill_color_value = "red"
        back_color_value = "white"
        if customize_dict is not None and len(customize_dict) > 0:
            if self.get_value(customize_dict,"fill_color") is not None:
                fill_color_value = self.get_value(customize_dict,"fill_color")
            if self.get_value(customize_dict,"back_color") is not None:
                back_color_value = self.get_value(customize_dict,"back_color")
        code_instance = qrcode_instance.make_image(fill_color = fill_color_value,back_color = back_color_value)
        return code_instance
    
    def code_generator(self,input_content,customize_dict):
        """[Method Intended to Generate the QRCode ]

        Args:
            input_content ([str]): [Input content for which the QR Code is Generated]
            customize_dict ([dict]): [Customizations Dictionary which contains the configurable items as part of the module]
        """
        qrcode_instance = self.qrcode_instance
        qrcode_instance.add_data(input_content)
        qrcode_instance.make(fit = True)
        code_instance = self.apply_customizations(customize_dict,qrcode_instance)
        output_file = "outputs/"+"qr_code_generated_"+self.get_current_timestamp()+".png"
        code_instance.save(output_file)
        
instance = QRCodeGenerator()
input_data_content = "https://github.com/rvigneshwaran?tab=repositories"
customize_dict = {}
customize_dict["fill_color"] = "blue"
customize_dict["back_color"] = "white"
instance.code_generator(input_data_content,customize_dict)
print("QR Code Generated for the Input Content Configured")
