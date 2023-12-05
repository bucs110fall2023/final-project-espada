[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12872343&assignment_repo_type=AssignmentRepo)
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

#  Phantom Curator
## CS110 Final Project   Fall, 2023 

## Team Members

Hamid Ajose and Aidan Gonzalez

***

## Project Description

 A file sorting python script that sorts files and relates to the user the last time files in a directory were opened, and how they were sorted the last time the application was run.

***    

## GUI Design 

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. curates files into subdirectories based on their file extension
2. user inputted pathing in the GUI 
3. a log file to track movement of files done by the curate function
4. buttons in the gui to engage the curate function and to open the log file
5. creates folders for the sorted files to be placed into

### Classes

PhantomCurator: Contains the curate function which curates the files selected by the user into seperate folders based off of the curator_dictionary and contains the log_file_movement which allows for the movement of the files to be logged into the Enchiridion.txt file for the user to see
Controller: contains the GUI of the program with directions and buttons to engage the curate() function and a button for opening the Enchridion.txt file. Also has a textbox that allows for user inputted file pathing to direct the curate() function

## ATP
