"""
    Created on 2024-12-03

    @author: rvsPatrik
"""

import os
import shutil
import pathlib
import sys
import json

try: 
    with open("mapping_file.json","r",encoding="utf-8") as file:
        folder_mapping = json.load(file)
        print("Custom json file laoded.\n")
except FileNotFoundError:
    print("Cant find custom json file in source folder.\n")

TWO_GB = 2*1024*1024*1024

def run_organizer(folder_path):
    pass