import os
import re


pattern = r'[\w\.-]+@[\w\.-]+'
for file in os.listdir(os.getcwd()):
    if file[-4:] == '.txt':
        file = open(file, 'r')
        for line in file.readlines():
            a = re.findall(pattern, line)
            if a: print(a)
            
        file.close()