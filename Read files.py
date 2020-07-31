# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 22:44:05 2020

@author: DC
"""

import tkinter as tk
from tkinter import filedialog
import pandas as pd

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue')
canvas1.pack()

def getExcel ():
    global result
    
    import_file_path = filedialog.askopenfilename()
    result = pd.read_excel (import_file_path)

    
browseButton_Excel = tk.Button(text='Import Excel File', command=getExcel, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=browseButton_Excel)

root.mainloop()

#result1= pd.read_excel(r'Test_Sheet1.xlsx')

