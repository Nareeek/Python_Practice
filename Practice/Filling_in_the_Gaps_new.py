# Filling in the Gaps
# Write a program that finds all files with a given prefix, such as spam001.txt,
# spam002.txt, and so on, in a single folder and locates any gaps in the numbering
# (such as if there is a spam001.txt and spam003.txt but no spam002.txt).
# Have the program rename all the later files to close this gap.
# As an added challenge, write another program that can insert gaps
# into numbered files so that a new file can be added.


import sys
import os
import re

search_path = r'D:\Python\find\txt'
prefix = 'Lesson-'
suffix = 'txt'
yes = False


def gen_number(number1, number2, tail):
    global search_path, prefix, suffix, yes

    # start with 001
    if yes:
        with open(r'D:\Python\Python_Practice\Practice\test.txt', mode='a') as test:
            test.write('False')
        cur_file = prefix + str(1).rjust(3, "0") + tail + suffix
        if number1 != 1 and not os.path.exists(os.path.join(search_path, cur_file)):
            with open(cur_file, mode='a') as new_file:
                new_file.write('Hello World!')
                print(cur_file, ' was created!\n')
                yes = False
            sys.exit()

    for num in range(number1, number2 + 1):
        yield num
    else:
        while True:
            yield num
            num += 1


def generate_file(arg):
    global search_path, prefix, suffix, yes
    os.chdir(search_path)

    pattern_for_numbers = re.compile(f'^{prefix}(\\d\\d\\d)(.*){suffix}$')

    for file in os.listdir():
        if file.startswith(prefix) and file.endswith(suffix):
            first = int(pattern_for_numbers.findall(file)[0][0])
            break

    if first != 1:
        file = open(r'D:\Python\Python_Practice\Practice\test.txt', mode='r+')
        read = file.read()
        if read == 'True':
            check = input('Start with 001 yes/no  > ')
            if check == 'yes':
                yes = True
    else:
        file = open(r'D:\Python\Python_Practice\Practice\test.txt', mode='w')
        file.write('True')

        file.close()

    for file1, file2 in zip(os.listdir()[0:], os.listdir()[1:]):
        find = pattern_for_numbers.findall(file1)
        if file1.startswith(prefix) and file1.endswith(suffix):
            tail = find[0][1]
            cur_number1 = int(find[0][0]) + 1
            a = True
        else:
            a = False

        if file2.startswith(prefix) and file2.endswith(suffix):
            cur_number2 = int(pattern_for_numbers.findall(file2)[0][0])
            b = True
        else:
            b = False

        if a and b:
            for num in gen_number(cur_number1, cur_number2, tail):
                if arg == 'new':
                    cur_file_name = prefix + str(num).rjust(3, "0") + tail + suffix

                    if not os.path.exists(os.path.join(search_path, cur_file_name)):
                        with open(cur_file_name, mode='a') as new_file:
                            new_file.write('Hello World!')
                            print(cur_file_name, ' was created!\n')
                        sys.exit()


# argument = input('Enter a argv[1] ')
# if argument == 'new':
#     generate_file(argument)

if sys.argv[1] == 'new':
    generate_file(sys.argv[1])
