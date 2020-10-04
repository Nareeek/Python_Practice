import re

document = open('document.txt')
read = document.read()
document.close()


pattern = r'([\w.]+)|\n'

a = re.findall(pattern, read)
temp = a[:]

def Input(word):
    if word[-1] not in '.,!?-%':
        if word[-1] in 'aeiouAEIOU':
            return input('Enter an {}:\n'.format(word))
        else:
            return input('Enter a {}:\n'.format(word))
    else:
        if word[-2] in 'aeiou':
            return input('Enter an {}:\n'.format(word[:-1])) + word[-1]
        else:
            return input('Enter a {}:\n'.format(word[:-1])) + word[-1]
        

n = int(input('How many word you want to replace? '))
List = [input('Enter a {} checking word:\n'.format(word + 1)) for word in range(n)]
    

for x in temp:
    if x == '':
        a[a.index(x)] = '\n'
        
    for word in List:
        pattern = '({})\.?'.format(word)
        if re.match(pattern, x):
            a[a.index(x)] = Input(x)
            
            
res = prev = ''
for x in a:
    if prev == '\n' and x != '\n':
        res += x
    else:
        res += ' ' + x
    prev = x


document1 = open('document1.txt', 'w')
document1.write(res[1:])
document1.close()
print(res[1:])
        
