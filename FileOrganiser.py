import os
import shutil

# WRITE THE NAME OF THE DIRECTORY THAT NEEDS TO BE SORTED

path = input("ENTER THE PATH OF THE DIRECTORY TO BE SORTED")

# LIST WITH ALL THE FILE NAME THAT IS THERE IN THE DIRECTORY

list_of_files = os.listdir(path)

for file in list_of_files :
    name,ext = os.path.splitext(file)

    # THIS IS GOING TO STORE THE EXTENSION 

    ext = ext[1:]

    if ext == '':
        continue

    # THIS WILL MOVE THE FILE TO THE DIRECTORY WHERE THE EXTENSION ALREADY EXIST
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)

    else :
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)