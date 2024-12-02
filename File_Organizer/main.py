"""
    Created on 2024-12-02

    @author: rvsPatrik
"""

import os
import shutil
import pathlib

folder_mapping = {
    "Web" : [".html",".xhtml",".htm"],
    "Photos" : [".jpeg",".png",".gif",".jpg",".bmp"],
    "Audio" : [".mp3",".m4p",".raw",".vox"],
    "Video" : [".avi",".mkv",".mp4",".wmv",".webm"],
    "Shortcuts" : [".url",".lnk"],
    "Compressed" : [".rar",".7zip",".iso",".tar",".gz",".xar",".rz",".zip"],
    "Documents" : [".txt",".xml",".docx",".ppt",".db",],  #might need changing
}

fileTypes = list( folder_mapping.keys() )
fileFormats = list( folder_mapping.values() )

MY_PATH = r"C:\Users\rvspa\Desktop\Tester"

TWO_GB = 2*1024*1024*1024

for file in os.scandir(MY_PATH):

    if file.is_dir() :
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

    if not target_folder :
        print(f"File {fileName} has an unknown extension: {fileFormat}")
        with open("unknown_files.txt","a",encoding="utf-8") as err_file:
            err_file.write(f"- {fileFormat}\t{fileName}\n")
        continue

    if target_folder == "Video":
        file_size = os.path.getsize(src)
        if file_size > TWO_GB:
            target_folder = "Movies"

    target_path = os.path.join(MY_PATH,target_folder)

    os.makedirs(target_path, exist_ok=True)

    dest = os.path.join(target_path,fileName.name)

    if os.path.exists(dest):
        base,ext = os.path.splitext(fileName.name)
        dest = os.path.join(target_path,f"{base}_copy{ext}")
    
    shutil.move(src, dest)
    print(f"Moved {fileName} to {target_path}")

    log_file = os.path.join(MY_PATH,"organizer_log.txt")

    with open(log_file,"a",encoding="utf-8") as log:
        log.write(f"Moved {fileName} to {dest}\n")