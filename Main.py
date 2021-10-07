from tkinter import filedialog
import moviepy.editor as mp
import tkinter as tk
import os
import pyperclip


def Convert_to_mp4(file): 
    old_filename = os.path.basename(file)
    name,ext = old_filename.split(".")
    des_path = os.getcwd()
    des_file = des_path + "\\" + name + ".mp4"
    clip = mp.VideoFileClip(file)
    clip.write_videofile(des_file)

def fileopener():
    path = fileopenDialog()
    pyperclip.copy(path.name)   # The moment user selects the path it will be copied to keyboard to send it as a parameter to Convert_to_mp4() 
    pathname.config(text=path.name)


def fileopenDialog():
    input = tk.filedialog.askopenfile()
    return input


def destination_file_opener():
    des_path = destinationDialog()
    des_name.config(text=des_path)
    os.chdir(des_path)

def destinationDialog():
    output = tk.filedialog.askdirectory()
    return output

if __name__ == "__main__":
    root = tk.Tk(className="Converter")
    root.geometry("800x800")
    # set 1
    B1 = tk.Button(root,text="Browse",padx=10,pady=10,command=fileopener)
    B1.place(x=200,y=100)
    Lbl1 = tk.Label(root,text="Location : ",font=("Helvetica",10))
    Lbl1.place(x=75,y=50)
    pathname = tk.Label(root,font=("Helvetica",12))
    pathname.place(x=150,y=50)
     # set 2
    Lbl2 = tk.Label(root,text="Destination : ",font=("Helvetica",10))
    Lbl2.place(x=75,y=275)
    B2 = tk.Button(root,text='Browse',padx=10,pady=10,command=destination_file_opener)
    B2.place(x=200,y=325)
    des_name = tk.Label(root,font=("Helvetica",12))
    des_name.place(x=155,y=275)
    # set 3
    B3 = tk.Button(root,text='Convert',padx=10,pady=10,command=lambda : Convert_to_mp4(pyperclip.paste()))
    B3.place(x=200,y=450)
    root.mainloop()