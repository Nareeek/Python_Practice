import sys


# sys.exit() (terminate the whole program)
def sys_exit():
    while True:
            print('Type exit - sys.exit()')
            response = input()
            if response == 'exit':
                    sys.exit()
                    print('You typed ' + response + '.')
    print('after sys.exit()')




# break (only terminate the current loop)
def breaking():
    while True:
            print('Type exit - break')
            response = input()
            if response == 'exit':
                    break
                    print('You typed ' + response + '.')
    print('part program after breaking')


while 1:
    try:
        choose = int(input("Choose\n1.for sys.exit()\n2.for break\n> "))
    except:
        print('type a number')
        choose = 0
    if choose == 1:
        print('sys.exit() - terminate the whole program:\n')
        sys_exit()
    elif choose == 2:
        print('break statement - terminate only the current loop:\n')
        breaking()
        break
    else:
        if choose != 0:
            print('there is no choise with that number')
        print('\n')
        continue
        
