import tkinter as tk
from tkinter import ttk,font
import os
from src.PhantomCurator import PhantomCurator

class Controller:

        def __init__(self):
            self.root = tk.Tk()
            
            def log_reader():
                os.system("start notepad Enchiridion.txt")
            
            def file_sorter():
                    curator = PhantomCurator(self.textbox.get("1.0",'end-1c'))
                    curator.curate()
                    curator.log_file_movement()
            self.style= ttk.Style()
            self.style.configure('TButton',background='Black',foreground='green',font=('Verdana',8))

            
            self.root.geometry("1250x400")
            self.root.title("GUI")
            
            self.label = tk.Label(self.root, text = "Phantom Curator", font=('Verdana', 18),bg='green',fg='Black')
            self.label.pack(padx=10,pady=10)
            
            self.label2 = tk.Label(self.root,text="Directions: Type in the textbox the pathing for the folder you want to be sorted ex. C:/Users/Owner/Desktop/Homework after that press the button!", font= ('Verdana',12),bg='green',fg='Black')
            self.label2.place(x=20,y=50)
            
            self.textbox = tk.Text(self.root, font=('Verdana', 18), height=5, width=40)
            self.textbox.pack(pady=100,padx=100)
            self.textbox.place(x=335,y=100)
            
            self.button = ttk.Button(self.root, text="Click to Sort", command=file_sorter,style = 'TButton')
            self.button.place(x=450,y=250)

            self.button2 = ttk.Button(self.root,text="Click to Open Log File",command= log_reader, style='TButton')
            self.button2.place(x=600,y=250)
          
            self.root.mainloop()