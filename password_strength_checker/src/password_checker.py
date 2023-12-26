import re
import math


def check_password_strength(password):

    # checks length of pass
    if len(password) < 8:
        return "Weak! Password must be at least 8 characters long."
    

    #checks for how complex the password is...

    if not any(char.isupper() for char in password) or \
       not any(char.islower() for char in password) or \
       not any(char.isdigit() for char in password) or \
       not any(char in "!@#$%^&*()-_+=<>,.?/:;{}[]" for char in password):
        return "Weak password! Password should contain a mix of uppercase letters, lowercase letters, digits, and also special characters."



    # check for common passwords
    common_passwords = ["password", "123456", "qwerty", "abc123"]
    if password.lower() in common_passwords:
        return "Weak password! Please refrain from using common passwords."
    
    #calculate entropy
    entropy = -sum((password.count(char) / len(password)) * math.log2(password.count(char) / len(password)) for char in set(password)) 
    if entropy < 3:
        return "Weak: Low entropy, please try a different password."
    
    return "Strong: Password meets all criteria."