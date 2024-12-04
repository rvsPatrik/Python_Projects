"""
    Created on 2024-12-03

    @author: rvsPatrik
"""

import os
import shutil
import pathlib
import sys
import json

TWO_GB = 2*1024*1024*1024

script_dir = os.path.dirname(os.path.abspath(__file__))

mapping_file = os.path.join(script_dir, "folder_mapping.json")

try:
    with open(mapping_file, "r", encoding="utf-8") as file:
        folder_mapping = json.load(file)
    print("Loaded folder mapping from JSON file.")
except FileNotFoundError:
    print(f"Mapping file not found. It's expected location: {mapping_file}")
    sys.exit()

def run_organizer(folder_path):

    for file in os.scandir(folder_path):
        if file.is_dir():
            if not os.listdir(file.path):
                os.rmdir(file.path)
                print(f"Removed empty folder: {file.path}")
            continue
        fileName = pathlib.Path(file)
        if fileName.name == "organizer_log.txt":
            continue

        if not file.is_file():
            continue

        fileFormat = fileName.suffix.lower()
        src = str(fileName)

        target_folder = None
        for folder,extensions in folder_mapping.items():
            if fileFormat in extensions:
                target_folder = folder
                break

        if not target_folder:
            with open("unknown_files.txt","a",encoding="utf-8") as err_file:
                err_file.write(f"- {fileFormat}\t{fileName}")    
            continue

        if target_folder == "Video":
            file_size = os.path.getsize(src)
            if file_size > TWO_GB:
                target_folder = "Movies"  

        target_path = os.path.join(folder_path,target_folder)
        os.makedirs(target_folder,exist_ok=True)

        dest = os.path.join(target_path,fileName.name)

        if os.path.exists(dest):
            base, ext = os.path.splitext(fileName.name)
            dest = os.path.join(target_path,f"{base}_copy{ext}")

        shutil.move(src, dest)
        print(f"Moved {fileName} to {target_path}")

        log_file = os.path.join(folder_path,"organizer_log.txt")

        with open(log_file,"a",encoding="utf-8") as log:
            log.write(f"Moved {fileName} to {dest}\n")