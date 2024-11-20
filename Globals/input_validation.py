import hashlib, re

class InputValidation:
    def sha512_hash(string_to_hash):
        hashedPwd = hashlib.sha512(string_to_hash.encode('utf-8')).hexdigest()
        return hashedPwd

    def check_valid_email(email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if(re.fullmatch(regex, email)):
            return True
        return False