#!/usr/bin/python3

"""
    This file handles the command line utility of the password manager tool
"""

from Cryptor_tool import SymEnc
from file_manager import FileHandler
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Password manager is a command line utility for managing passwords")

    # For password generation
    parser.add_argument("-g", "--gen", help="generate a new password", action="store_true")
    parser.add_argument("--length", help="specify length of password to be generated", default=12, type=int,
                        required=False, metavar="NUMBER")
    parser.add_argument("--alpha", help="generate passwords using only alphabets", required=False,
                        action="store_true")
    parser.add_argument("--alpha-decimal", help="generate passwords using only alpha numerals", required=False,
                        action="store_true")
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

    if arguments.gen:
        # Todo: Generate password based on other arguments
        print("Generate password")
        if arguments.alpha:
            pass
    elif arguments.enc:
        # Todo: Encrypt something
        print("Encrypt something")
    elif arguments.dec:
        # Todo: Decrypt something
        print("Decrypt something")

