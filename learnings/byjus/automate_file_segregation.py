import os
import shutil
fromDirectory = 'C:/Users/reach/Downloads'
toDirectory = 'C:/Users/reach/Downloads'
list = os.listdir(fromDirectory)
for file in list:
    root,extension = os.path.splitext(file)
    if extension == '':
        continue
    if extension in ['.txt','.doc','.docx','.pdf']:
        path1 = fromDirectory + '/' + file                        #downloads/galaxy.png
        path2 = toDirectory + '/' + 'documentFiles'               #downloads/imageFiles
        path3 = toDirectory + '/' + 'documentFiles' + '/' + file  #downloads/imageFiles/galaxy.png
        if os.path.exists(path2):
            print("Moving" + file + "....")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving" + file + "....")
            shutil.move(path1,path3)