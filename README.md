## What is the purpose of this script:

When you run this script you will be asked to give a Root directory. This is the folder that contains all the folders you want to rename.
It will then loop through all the folders and retrieve the "Date taken" EXIF data from the first image it finds.
Like this: 

    -> Root_Folder
    ----->Folder 1  <- and rename this folder --------------
                                                           |
    ----------> Image.jpg  <-- Take exif data from here ----

The folder will then be given a name in this format: 
YYYY-MM-DD - Original_Name (example: 2021-12-02 - Folder 1)

It also support "Folders in folders", if the first folder does not contain any images with "Date-Taken" data it will continue into sub-folders.
If it does not find any useful data, it will ignore that folder and continue.

## This script will also remove the PATH_LENGTH limit om windows.
This is to remove the problem with accessing folders with really long names.

## How to use:

Start the script either from terminal, or with EXE file.
When it ask for "Root Folder" paste in a link to the folder containing the folders you want to rename. 


## Compability:

Windows: Tested   ✓  
MacOS:   Untested 🛇  
Linux:      Untested 🛇
