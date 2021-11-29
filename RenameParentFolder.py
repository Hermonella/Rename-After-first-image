import os
import exifread
import re


# Root_Folder = "C:\WORKFOLDER\Rename After first image\Testmappe\Importerte bilder"
Root_Folder = input("Root Folder: ")
File_Extension = ".jpg",".jpeg",".png",".tiff",".JPG",".JPEG",".PNG",".TIFF"
Folder_List = os.listdir(Root_Folder)

Check_for_aldready_dated_folders_patter = "^\d\d\d\d[-]\d\d[-]\d\d"

# print(Folder_List) 

def Get_Exif_Date_Taken(Folder_To_Rename, Image_With_Exif):
    with open(Folder_To_Rename + "\\" + Image_With_Exif, "rb") as image:
        tags = exifread.process_file(image, stop_tag="EXIF DateTimeOriginal")
        dateTaken = tags["EXIF DateTimeOriginal"]
        return dateTaken


for folder in Folder_List:
    if not re.match(Check_for_aldready_dated_folders_patter, folder[:10]):
        Folder_To_Rename = Root_Folder + "\\" + folder
        Image_List = [_ for _ in os.listdir(Folder_To_Rename) if _.endswith(File_Extension)]
        Image_With_Exif = Image_List[0]
        date_Taken = str(Get_Exif_Date_Taken(Folder_To_Rename, Image_With_Exif))[:10].strip().replace(":","-")
        Folder_New_Name = date_Taken + " - " + folder
        os.rename(Folder_To_Rename, Root_Folder + "\\" + Folder_New_Name)
        print(Folder_New_Name)

