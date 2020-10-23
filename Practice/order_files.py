import os, re, shutil


def order_files(folder):

    pattern = re.compile(r'^(Lesson-)(.*)(\d\d\d)(.*)(.pdf)$')

    os.chdir(folder)
    path = os.path.abspath('.')
    prev = '000'

    for file in os.listdir():
        find = pattern.findall(file)
        
        if find:
            if int(find[0][2]) - int(prev) > 1:
                num = str(int(prev) + 1)
                number = '00' + str(num)
                
                if len(number) > 3: number = number[-3:]
                
                head = find[0][0] + find[0][1]
                tail = find[0][3] + find[0][4]
                    
                rename = head + number + tail
                
                old = os.path.join(path, file)
                new = os.path.join(path, rename)
                shutil.move(old, new)
                
                prev = number
            else:
                prev = find[0][2]

order_files(r'D:\Python\find\pdf')
        
