#!/usr/bin/python3

"""
    This file handles the command line utility of the password manager tool
"""

from Cryptor_tool import SymEnc, PasswordGenerator
from file_manager import FileHandler
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Password manager is a command line utility for managing passwords")

    # For password generation
    parser.add_argument("-g", "--gen", help="generate a new password", action="store_true")
    parser.add_argument("-l", "--length", help="specify length of password to be generated", default=12,
                        type=int, required=False, metavar="NUMBER")
    parser.add_argument("--alpha", help="generate passwords using only alphabets", required=False,
                        action="store_true")
    parser.add_argument("--alpha-decimal", help="generate passwords using only alpha numerals",
                        required=False, action="store_true")
    parser.add_argument("--all", help="generate passwords using alphanumerical and special characters",
                        required=False, action="store_true")

    # For Encryption & Decryption
    parser.add_argument("-e", "--enc", help="encrypt a file", action="store_true")
    parser.add_argument("-d", "--dec", help="decrypt a file", action="store_true")
    parser.add_argument("-k", "--key", help="key to be used for encryption/decryption")
    parser.add_argument("-kf", "--key-file", help="use key from FILE for encryption/decryption",
                        metavar="FILE")
    parser.add_argument("-t", "--text", help="text to encrypt/decrypt", metavar="TEXT")
    parser.add_argument("-f", "--file", help="file to encrypt/decrypt", metavar="FILE")
    parser.add_argument("-o", "--out", help="output file to store decrypted/encrypted file",
                        required=False, metavar="FILE")

    arguments = parser.parse_args()

    # Generate password
    if arguments.gen:
        choice = 3
        if arguments.alpha:
            choice = 1
        if arguments.alpha_decimal:
            choice = 2
        if arguments.all:
            choice = 3
        obj_PassGen = PasswordGenerator(choice, arguments.length)
        print(f" Generated password: {obj_PassGen.generate()}")

    # Encrypt
    elif arguments.enc:
        if arguments.text is None and arguments.file is None:
            print(" Error: Encryption requires either a text (-t) or a file (-f) to encrypt")
            exit(0)
        obj_SymEnc = SymEnc(f_name=arguments.key_file, k=arguments.key)
        if arguments.text is not None:
            obj_SymEnc.encrypt_data("text", text=arguments.text)
            print(f" Encrypted data:\n{obj_SymEnc.encrypted_text}")

        if arguments.file is not None and arguments.out is not None:
            obj_SymEnc.encrypt_data("file", input_file=arguments.file, output_file=arguments.out)
            print(f" Wrote encrypted data to: {arguments.out}")
        else:
            print(" Error: Requires input file (-f) along with output file (-o)")
            exit(0)

    # Decrypt
    elif arguments.dec:
        if arguments.text is None and arguments.file is None:
            print(" Error: Decryption requires either a text (-t) or a file (-f) to decrypt")
            exit(0)
        obj_SymEnc = SymEnc(f_name=arguments.key_file, k=arguments.key)
        if arguments.text is not None:
            obj_SymEnc.encrypt_data("text", text=arguments.text)
            print(f" Decrypted data:\n{obj_SymEnc.encrypted_text}")

        if arguments.file is not None and arguments.out is not None:
            obj_SymEnc.encrypt_data("file", input_file=arguments.file, output_file=arguments.out)
            print(f" Wrote Decrypted data to: {arguments.out}")
        else:
            print(" Error: Requires input file (-f) along with output file (-o)")
            exit(0)


