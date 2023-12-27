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
    parser.add_argument("-g", "--gen", help="generate a new password", metavar="")
    parser.add_argument("--length", help="specify length of password to be generated", default=12, type=int,
                        required=False, metavar="NUMBER")
    parser.add_argument("--a", help="generate passwords using only alphabets", required=False, metavar="")
    parser.add_argument("--a0", help="generate passwords using only alpha numerals", required=False,
                        metavar="")
    parser.add_argument("--all", help="generate passwords using alphanumerical and special characters",
                        required=False, metavar="")

    # For Encryption & Decryption
    # parser.add_argument()
    parser.add_argument("-f", "--file", help="input File", metavar="FILE")
    parser.add_argument("-e", "--enc", help="encrypt a file", metavar="")
    parser.add_argument("-d", "--dec", help="decrypt a file", metavar="")
    parser.add_argument("-o", "--out", help="output file to store encrypted or decrypted file",
                        required=False, metavar="FILE")

    arguments = parser.parse_args()
    print(arguments.file)
    print(arguments.out)