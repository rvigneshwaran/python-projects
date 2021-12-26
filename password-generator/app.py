import random
import string

lstring_list = list(string.ascii_lowercase)
ustring_list = list(string.ascii_uppercase)
digits_list = list(string.digits)
char_list = list("!@#$%^&*()")

class PasswordGenerator:
    
    def generate_password(self,password_length):
        console_list = digits_list + lstring_list + ustring_list + char_list
        random.shuffle(console_list)
        password = [random.choice(console_list) for element in range(password_length)]
        random.shuffle(password)
        final_pass = "".join(password)
        print("The password is -> ",final_pass)
        return final_pass
        
    def create_rand_coll(self,possbile_char_list,size):
        return [random.choice(possbile_char_list) for element in range(size)]
        
    def generate_custom_password(self,password_length,lostring_lenth,upstring_lenth,digits_length):
        char_lenth = password_length - (lostring_lenth + upstring_lenth + digits_length)
        lstringpass_list = self.create_rand_coll(lstring_list,lostring_lenth)
        ustringpass_list = self.create_rand_coll(ustring_list,upstring_lenth)
        digitspass_list = self.create_rand_coll(ustring_list,upstring_lenth)
        charpass_list = [random.choice(char_list) for element in range(char_lenth)]
        password = lstringpass_list + ustringpass_list + digitspass_list + charpass_list
        random.shuffle(password)
        final_pass = "".join(password)
        print("The password is -> ",final_pass)
        return final_pass

    def generateNPasswords(self,maxPasswords,password_length):
        password_list_contends = []
        for index in range(maxPasswords):
            password_list_contends.append(self.generate_password(password_length))
        return password_list_contends
            

# Generate a password with control over only password length.  
passgen_instance = PasswordGenerator()
password_length = int(input("Please Enter the Length of Your Password: "))
passgen_instance.generate_password(password_length)

# Generate a Custom Password with User's choice of No of Digits and Characters.
password_length = int(input("Please Enter the Length of Your Password : "))
ustring_length = int(input("Please Enter No. of of Upper case Alphabets Needed : "))
lstring_length = int(input("Please Enter No. ofLower case Alphabets Needed : "))
digits_length = int(input("Please Enter No. of Digits Needed : "))
total_passwords = int(input("Enter the No. of passwords that needs to be Generated : "))
if (password_length > (ustring_length + lstring_length + digits_length)):
    passgen_instance.generate_custom_password(password_length,lstring_length,
                                              ustring_length,digits_length)
else:
    print("Enter Alphabet length and Digits Length Less than Total Length")
if total_passwords > 0:
    passgen_instance.generateNPasswords(total_passwords,password_length)