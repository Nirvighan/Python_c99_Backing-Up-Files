import os
import shutil

source = input("ENTER SOURCE FOLDER PATH")
destination = input("ENTER DESTINATION FOLDER PATH")

source = source + '/'
destination = destination + '/'

list_of_files = os.listdir(source)

for file in list_of_files:
    shutil.move((source+file),destination)





