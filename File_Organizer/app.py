"""
    Created on 2024-12-03

    @author: rvsPatrik
"""

import tkinter as tk
from tkinter import filedialog
from script import run_organizer

def select_directory():
    pass

def start_organizer():
    pass


root = tk.Tk()
root.title("File Organizer")

frame = tk.Frame(root)
frame.pack(pady=10)

label = tk.Label(frame,text="Select the folder you want to organize:")
label.grid(row = 0,column=0,padx=5,pady=5)

entry_path = tk.Entry(frame,width=40)
entry_path.grid(row=1,column=0,padx=5,pady=5)

btn_start = tk.Button(root,text="Start Organizer",command=start_organizer)
btn_start.pack(pady=10)

label_status = tk.Label(root, text = "", fg = "blue")
label_status.pack(pady=10)

root.mainloop()