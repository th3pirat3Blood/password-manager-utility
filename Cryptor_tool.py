#!/usr/bin/python3

"""
    This file is responsible for taking care of all password encryption & decryption related tasks
"""

from cryptography.fernet import Fernet
import string
import random


class SymEnc:
    def __init__(self, f_name=None, k=None):
        if k is None and f_name is None:
            self.key = Fernet.generate_key().decode()
            key_file = "".join([chr(x) for x in range(65, 90)]) + ".key"
            with open(key_file, "w") as f:
                f.write(self.key)
            print(f" Key written to {key_file}")
        elif f_name is not None:
            # extract key from file
            with open(f_name, "r") as f:
                self.key = f.read()
        elif k is not None:
            self.key = k

        self.encrypted_text = ""
        self.decrypted_text = ""
        self.f_obj = Fernet(self.key)

    def encrypt_data(self, choice, text=None, input_file=None, output_file=None):
        if choice == "text":
            self.encrypted_text = self.f_obj.encrypt(text.encode()).decode()
        if choice == "file":
            with open(input_file, "r") as f:
                data = f.read()
            self.encrypted_text = self.f_obj.encrypt(data.encode()).decode()
            with open(output_file, "w") as f:
                f.write(self.encrypted_text)

    def decrypt_data(self, choice, text=None, input_file=None, output_file=None):
        if choice == "text":
            self.decrypted_text = self.f_obj.decrypt(text.encode()).decode()
        if choice == "file":
            with open(input_file, "r") as f:
                data = f.read()
            self.decrypted_text = self.f_obj.decrypt(data.encode()).decode()
            with open(output_file, "w") as f:
                f.write(self.decrypted_text)


class PasswordGenerator:
    def __init__(self, choice=3, length=12):
        self.length = length
        if choice == 1:
            self.charset = string.ascii_letters
        if choice == 2:
            self.charset = string.ascii_letters + string.digits
        if choice == 3:
            self.charset = string.ascii_letters + string.digits + "~`!@#$%^&*()_-+=?/<>{}[]"

    def generate(self):
        password = "".join([self.charset[random.randint(0, len(self.charset)-1)] for x in range(self.length)])
        return password

