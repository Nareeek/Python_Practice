import os

os.chdir(r'D:\Python\C++ Edu')

for folderName, subfolders, filenames in os.walk(os.getcwd()):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)
        

            
    print('\n')