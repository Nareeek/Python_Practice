import os

path = os.chdir("D:\\Python\\C++ Edu\\tasks")

i = 1
for file in os.listdir(path):
   new_file_name = 'main{}.cpp'.format(i)
   os.rename(file, new_file_name)
   i += 1
