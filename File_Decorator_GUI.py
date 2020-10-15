import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
import os,shutil


win=tk.Tk()  #calling constructor of tk
win.title("File_Decorator_GUI")  
#labels
file_location=ttk.Label(win,text='Enter Folder Location:')   # or we can use .pack()
file_location.grid(row=0,column=0,sticky=tk.W)

#Entry Box
file_path=tk.StringVar()# input store karne ke liye variable
file_entry=ttk.Entry(win,width=50,textvariable=file_path)   
file_entry.grid(row=0,column=1)
file_entry.focus() #by defalt cursor entry box me hoga

dict_extensions = {
    'Audio_extensions' : ('.mp3', '.m4a', '.wav', '.flac','.ape','.wv','.aiff'),
    'Video_extensions' : ('.mp4', '.mkv', '.MKV', '.flv', '.mpeg'),
    'Document_extensions' : ('.doc', '.pdf', '.txt'),
}
#path where we want to do  file decorator
# folderpath=input('Enter the folder or file location where you want to do file decorator:\n')

def file_finder(folder_path, file_extensions):
    # files = []
    # for file in os.listdir(folder_path):
    #     for extension in file_extensions:
    #         if file.endswith(extension):
    #             files.append(file)
    # return files
    return [file for file in os.listdir(folder_path) for extension in file_extensions if file.endswith(extension)]

#button
def action():   #action perform after submit
    filepath=file_path.get()
    # print(filepath)
    
    for extension_type, extension_tuple in dict_extensions.items():
        folder_name = extension_type.split('_')[0] + 'Files'
        folder_path = os.path.join(filepath, folder_name)
        try:     #file pahle se hoga 
            os.mkdir(folder_path)
        except FileExistsError:
            m_box.showerror('ERROR','Cannot create a file when that file already exists:\n'+
            'please remove or remane file named "AudioFiles", "VideoFiles" and "DocumentFiles"')
        else:
            for item in file_finder(filepath, extension_tuple):
                item_path = os.path.join(filepath,item)
                item_new_path = os.path.join(folder_path,item)
                shutil.move(item_path,item_new_path)

    file_entry.delete(0,tk.END) # after entry box it will clear the file_entry label
    
submit_button=ttk.Button(win,text='SUBMIT',command=action)#  jo command pass karenge us name ka func banana hoga
submit_button.grid(row=1,column=0)


win.mainloop()