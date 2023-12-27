#!/usr/bin/python3

"""
    This file is responsible for taking care of all password encryption & decryption related tasks
"""

from cryptography.fernet import Fernet


class SymEnc:
    def __init__(self, f_name="sym_key.key", k=None):
        if k is None:
            self.key = Fernet.generate_key()
        else:
            self.key = k

        self.encrypted_text = ""
        self.filename = f_name
        self.f_obj = Fernet(self.key)

    def display_sym_key(self):
        print("Generated key: ", self.key.decode())

    def put_sym_key_to_file(self, file_name):
        with open(file_name, "w") as f:
            f.write(self.key.decode())

    def get_sym_key_from_file(self, file_name):
        with open(file_name, "r") as f:
            got_key = f.read()
        print("Got key: ", got_key)

    def encrypt_file(self, file_name):

        with open(file_name, "r") as f:
            data = f.read()

        # Encrypt whole file content
        encrypted_data = self.f_obj.encrypt(data.encode())

        with open(file_name+".enc", "w") as f:
            f.write(encrypted_data.decode())

        print(f"Data of {file_name} encrypted and stored in {file_name}.enc")

    def decrypt_file(self, file_name):
        with open(file_name, "r") as f:
            encrypted_data = f.read()

        # Decrypt whole file
        decrypted_text = self.f_obj.decrypt(encrypted_data.encode())

        with open(file_name+".dec", "w") as f:
            f.write(decrypted_text.decode())

        print(f"Decrypted data in {file_name}.dec")

