import tkinter as tk
from tkinter import ttk,font
import os
import shutil
import datetime
class PhantomCurator:
    def __init__(self, mypath):
        self.mypath = mypath
        self.messy_cabinet = os.listdir(self.mypath)
        self.curator_directories = {
            ".docx": "Documents_Curated",
            ".pdf": "Documents_Curated",
            ".txt": "Documents_Curated",
            ".pptx": "Documents_Curated",
            ".xlsx": "Documents_Curated",
            ".jpg": "Images_Curated",
            ".jpeg": "Images_Curated",
            ".png": "Images_Curated",
            ".gif": "Images_Curated",
            ".bmp": "Images_Curated",
            ".svg": "Images_Curated",
            ".mp3": "Audio_Curated",
            ".wav": "Audio_Curated",
            ".flac": "Audio_Curated",
            ".aac": "Audio_Curated",
            ".mp4": "Video_Curated",
            ".avi": "Video_Curated",
            ".mkv": "Video_Curated",
            ".mov": "Video_Curated",
            ".wmv": "Video_Curated",
            ".zip": "Archives_Curated",
            ".rar": "Archives_Curated",
            ".7z": "Archives_Curated",
            ".tar.gz": "Archives_Curated",
            ".exe": "Apps_Curated",
            ".msi": "Apps_Curated",
            ".app": "Apps_Curated",
            ".deb": "Apps_Curated",
            ".html": "Web_Curated",
            ".css": "Web_Curated",
            ".js": "Web_Curated",
            ".py": "Programming_Curated",
            ".java": "Programming_Curated",
            ".cpp": "Programming_Curated",

        }

    def curate(self):
        log_filename = "Enchiridion.txt"

        for file in self.messy_cabinet:
            for file_extension, directory in self.curator_directories.items():
                if file.lower().endswith(file_extension.lower()):
                    directory_path = os.path.join(self.mypath, directory)
                    if not os.path.exists(directory_path):
                        os.makedirs(directory_path, exist_ok=True)

                    source_file_path = os.path.join(self.mypath, file)
                    destination_file_path = os.path.join(directory_path, file)

                    self.log_file_movement(log_filename, file, source_file_path, destination_file_path)

                    shutil.move(source_file_path, destination_file_path)

    def log_file_movement(self, log_filename, file, source, destination):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"Timestamp: {timestamp}\n"
        log_entry += f"File: {file}\n"
        log_entry += f"Source: {source}\n"
        log_entry += f"Destination: {destination}\n"
        log_entry += "=" * 40  

        with open(log_filename, "a") as log_file:
            log_file.write(log_entry + "\n\n")
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

            
            self.root.geometry("1300x400")
            self.root.title("GUI")
            
            self.label = tk.Label(self.root, text = "Phantom Curator", font=('Verdana', 18),bg='green',fg='Black')
            self.label.pack(padx=10,pady=10)
            
            self.label2 = tk.Label(self.root,text="Directions: Type in the textbox the pathing for the folder you want to be sorted ex. C:/Users/Owner/Desktop/Homework after that press the button!", font= ('Verdana',12),bg='green',fg='Black')
            self.label2.place(x=20,y=50)
            
            self.textbox = tk.Text(self.root, font=('Verdana', 18), height=5, width=40)
            self.textbox.pack(pady=100,padx=100)
            self.textbox.place(x=100,y=100)
            
            self.button = ttk.Button(self.root, text="Click to Sort", command=file_sorter,style = 'TButton')
            self.button.place(x=150,y=250)

            self.button2 = ttk.Button(self.root,text="Click to Open Log File",command= log_reader, style='TButton')
            self.button2.place(x=300,y=250)
          
            self.root.mainloop()            
    def main():
        gui = PhantomCurator.Controller()
        gui.root.mainloop()

PhantomCurator.main()