#!/usr/bin/python3

"""
    This file handles all the file related operations
"""

import os
import random


class FileHandler:
    def __init__(self, f_name="".join([chr(random.randint(97, 121)) for x in range(5)])+".txt"):
        self.filename = f_name

    def write_to_file(self, text):
        with open(self.filename, "w") as f:
            f.write(text)

    def append_to_file(self, text):
        with open(self.filename, "w+") as f:
            f.write(text)

    def read_from_file(self):
        with open(self.filename, "r") as f:
            data = f.read()

