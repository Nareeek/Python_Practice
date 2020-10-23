'''
Write a program that walks through a folder tree and
searches for files with a certain file extension
(such as .pdf or .png or .jpg or .JPG).
Copy these files from whatever location they are
in to a new folder.
'''


import os, re, shutil

dest = r'D:\Python\find'

os.chdir(r'C:')

pattern = re.compile(r'.*\.((pdf)|(jpg)|(JPG)|(png))$') # (mp3)(mp4)(ico)(doc)(ppt)

for foldername, subfolders, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        if pattern.match(filename):
            #print(foldername, end=' -->')
            #print(filename)
            filename = os.path.join(foldername, filename)
            #size = os.path.getsize(filename)
            #if size < 70000:
                #continue
            shutil.copy(filename, dest)

print('Done.')

