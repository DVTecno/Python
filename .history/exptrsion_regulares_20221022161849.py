import string
import secrets
import random
import re
from tabnanny import check

def check_password(password):
    password_pattern="(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&/_=;:<>|#,\*\'\"\-\+\[\]])[A-Za-z\d@$!%*?&/_=;:<>|#,\*\'\"\-\+\[\]]{B,}$"
    return re.fullmatch(password_pattern, password) !=None

pass_characters = string.ascii_lowercase +\
                  string.ascii_uppercase +\
                  string.digits +\
                  string.punctuation

password=''.join(secrets.choice(pass_characters) for i in renge(0,random.randint(6,16)))
if check_password(password):
    print(f"El password {password} cumple con la politica")
else:
    print(f"El password {password} No cumple con la politica")



