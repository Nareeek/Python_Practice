import re, os, pprint

i = 1
dic = {}
for file in os.listdir(os.getcwd()):
    if file[-4:] == '.txt':
        dic[i] = file
        print(i, '.', file)
        i += 1

number = int(input('Choose the file (number): '))
print('\n')

pattern = r'[\w]+\.?'

file = open(dic[number], 'r')
read = file.read()

dic = {}
for word in re.findall(pattern, read):
    dic.setdefault(word, -1)
    dic[word] += 1
        
exists = False
count = 0
for x in dic:
    if dic[x] > 1:
        print(x, '->', dic[x])
        exists = True
        count += 1

print('total repeating word: ', count)

if not exists:
    print('Wow!, this file doesn\'t have a single duplicate word.')

file.close()