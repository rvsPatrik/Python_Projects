"""
    Created on 2024-12-03

    @author: rvsPatrik
"""

import tkinter as tk
from tkinter import filedialog
from script import run_organizer
import json

def select_directory():
    folder = filedialog.askdirectory()
    if folder:
        entry_path.delete(0,tk.END)
        entry_path.insert(0,folder)

def start_organizer():
    folder = entry_path.get()

    if folder:
        try:
            run_organizer(folder)
            label_status.config(text="Organizing completed.",fg="green")
        except Exception as e:
            label_status.config(text=f"Error: {e}",fg = "red")
    else:
        label_status.config(text="Select a valid directory.",fg = "red")

root = tk.Tk()
root.title("File Organizer")

frame = tk.Frame(root)
frame.pack(pady=10)

label = tk.Label(frame,text="Select the folder you want to organize:")
label.grid(row = 0,column=0,padx=5,pady=5)

entry_path = tk.Entry(frame,width=40)
entry_path.grid(row=1,column=0,padx=5,pady=5)

browse_button = tk.Button(root,text="Browse Folder",command=select_directory)
browse_button.pack(pady=10)

btn_start = tk.Button(root,text="Start Organizer",command=start_organizer)
btn_start.pack(pady=10)

label_status = tk.Label(root, text = "", fg = "blue")
label_status.pack(pady=10)

root.mainloop()