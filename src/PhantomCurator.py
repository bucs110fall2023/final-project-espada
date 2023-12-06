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