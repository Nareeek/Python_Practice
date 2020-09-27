import os

print(os.getcwd(), '\n' * 2)

for filename in os.listdir(os.getcwd()):
    filesize = os.path.getsize(os.path.join(os.getcwd(), filename))

    print(filename.ljust(30), '-->', str(filesize).rjust(10), ' bytes')
