# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 18:54:00 2021

@author: pub
"""


import numpy as np
import pandas as pd
import tkinter.filedialog as fd
import tkinter as tk
import os



def upload_file():
    global fname
    global fname_csv
    global file_address
    file_address=fd.askopenfilenames(parent=CSVexport_system,title='Upload')
    fname=[os.path.split(file_address[index])[1] for index in np.arange(len(file_address))]
    list_var.set(fname)
    #fname_csv = [fname[index].replace('.SP','.csv') for index in range(len(fname))]
    
    
def export_file():
    for items in file_address:
        saving_path=items.replace('.SP','.csv')
        with open(items, 'rb') as f:
            line_index = 0
            output = []
            for lines in f:
                if line_index > 0:
                    line = lines.decode('utf-8')
                    line_edit = line.rstrip().replace('\t',' ')
                    line_edit1 = line_edit.split()
                    list1 = [float(items) for items in line_edit1]
                    output = np.append(output,list1)
                if lines == b'#DATA\r\n':
                    line_index = line_index + 1
            first_column = [output[index] for index in range(0, len(output),2)]
            second_column = [output[index] for index in range(1, len(output),2)]
            data_frame = {'first': first_column, 'second': second_column}
            data = pd.DataFrame(data_frame)
            data.to_csv(saving_path)
    

CSVexport_system=tk.Tk()
CSVexport_system.title("Export system")
CSVexport_system.geometry('1000x700')
title_label=tk.Label(CSVexport_system,text='Export system',font=('Times New Roman',27,'bold'))
title_label.place(relx=0.05,rely=0.04)


upload_button=tk.Button(CSVexport_system,text='Upload',font=('Times New Roman',17,'bold'),command=upload_file)
upload_button.place(relx=0.15,rely=0.13)


export_button=tk.Button(CSVexport_system,text='Export',font=('Times New Roman',17,'bold'),command=export_file)
export_button.place(relx=0.75,rely=0.73)

list_var=tk.StringVar()
list_box=tk.Listbox(CSVexport_system,listvariable=list_var,width=35,height=20)
list_box.place(relx=0.15,rely=0.25)


CSVexport_system.mainloop()