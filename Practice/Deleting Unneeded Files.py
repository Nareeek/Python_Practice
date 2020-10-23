'''
Write a program that walks through a folder tree and searches for exceptionally
large files or folders—say, ones that have a file size of more than
100MB. (Remember, to get a file’s size, you can use os.path.getsize() from
the os module.) Print these files with their absolute path to the screen.
'''

import os, re, shutil


os.chdir(r'C:')

pattern = re.compile(r'.*\.((mp3)|(mp4)|(doc))$')

for foldername, subfolders, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        if pattern.match(filename):
            filename = os.path.join(foldername, filename)
            size = os.path.getsize(filename)
            if size < 100_000_000: # 100MB
                continue
            print(filename)

print('Done.')

