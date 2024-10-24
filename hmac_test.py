import hashlib
import hmac
import os

def generate_salt(length=16):
    return os.urandom(length)

def hash_password(password, salt):
    phash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    return phash

def create_hmac(key, message):
    h = hmac.new(key, message.encode('utf-8'), hashlib.sha256)
    return h.hexdigest() 

def main():
    password = "secure_password"
    salt = generate_salt()
    hpass = hash_password(password, salt)
    
    print("Password:", password)
    print("Salt (hex):", salt.hex())
    print("Hashed Password (hex):", hpass.hex())
    
    secret_key = b'secret_key'
    msg = "Aditya"
    hmacr = create_hmac(secret_key, msg)
    print("HMAC (hex):", hmacr)  
    
if __name__ == "__main__":
    main()
