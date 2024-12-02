"""
    Created on 2024-12-02

    @author: rvsPatrik
"""

import os
import shutil
import mapping

FOLDER_MAPPING = mapping.folder_mapping

fileTypes = list( FOLDER_MAPPING.keys() )
fileFormats = list( FOLDER_MAPPING.values() )

MY_PATH = r"C:\Users\rvspa\Desktop\Tester"

for file in os.scandir(MY_PATH):
    pass