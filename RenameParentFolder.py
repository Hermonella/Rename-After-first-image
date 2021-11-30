import os
import exifread
import re



Root_Folder = "C:\WORKFOLDER\Rename After first image\Testmappe\Importerte bilder"
# Root_Folder = input("Root Folder: ")
File_Extension = ".jpg",".jpeg",".png",".tiff",".JPG",".JPEG",".PNG",".TIFF"
Folder_List = os.listdir(Root_Folder)

Check_for_aldready_dated_folders_pattern = "^\d\d\d\d[-]\d\d[-]\d\d"

# print(Folder_List) 

def Get_Exif_Date_Taken(Image_List):
    for items in Image_List:
        try:
            with open(items, "rb") as image:
                tags = exifread.process_file(image, stop_tag="EXIF DateTimeOriginal")
                dateTaken = tags["EXIF DateTimeOriginal"]
                return dateTaken
        except: continue


for folder in Folder_List:
    if not re.match(Check_for_aldready_dated_folders_pattern, folder[:10]):
        Folder_To_Rename = Root_Folder + "\\" + folder
        # Image_List = [_ for _ in os.listdir(Folder_To_Rename) if _.endswith(File_Extension)]
        Image_List = []
        for item in os.listdir(Folder_To_Rename):
            if item.endswith(File_Extension):
                Image_List.append(os.path.join(Folder_To_Rename, item))
        
        if len(Image_List) == 0:
            for root, dirs, files in os.walk(Folder_To_Rename):
                for item in files: 
                    if item.endswith(File_Extension):
                        Image_List.append(os.path.join(root, item))
        
        #Det er EXIF delen som trenger full path til bilde.
        if not len(Image_List) == 0:
            Image_With_Exif = Image_List[0]
            # date_Taken = str(Get_Exif_Date_Taken(Image_With_Exif))[:10].strip().replace(":","-")
            date_Taken = str(Get_Exif_Date_Taken(Image_List))[:10].strip().replace(":","-")
            if not date_Taken == "None":
                Folder_New_Name = date_Taken + " - " + folder
                #Trenger ikke tenke på Folder_To_Rename. Denne blir riktig.
                os.rename(Folder_To_Rename, Root_Folder + "\\" + Folder_New_Name)
                print(Folder_New_Name)
        else: pass

