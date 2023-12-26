#!/usr/bin/python3

"""
    This file handles all the file related operations
"""

import os


class FileHandler:
    def __init__(self, f_name = "password.enc"):
        self.__init__()
        self.filename = f_name

    def append_to_file(self, text):
        with open(self.filename, "w+") as f:
            f.write(text)
        return True

    def read_from_file(self):
        with open(self.filename, "r") as f:
            data = f.read()
        return data

