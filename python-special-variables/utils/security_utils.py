import secrets
import random
import string

class SecurityUtils:
    
    def __init__(self):
        print("Initializing Components in Security Utils")
        
    def generate_security_key(self,key_type="hex",length=1024):
        security_key = None
        if key_type == "url_safe":
            security_key = secrets.token_urlsafe(length)
        elif key_type == "hex":
            security_key = secrets.token_hex(length)
        elif key_type == "random":
            security_key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
        return security_key